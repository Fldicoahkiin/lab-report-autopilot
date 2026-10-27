[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Workspace,
    [string]$Requirements,
    [string]$SystemPython
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"

$PythonVersion = "3.12.10"
$WorkspacePath = [System.IO.Path]::GetFullPath($Workspace)
$RuntimePath = Join-Path $WorkspacePath ".lab-report-runtime"
$PrivatePythonPath = Join-Path $RuntimePath "python-$PythonVersion"

if (-not $Requirements) {
    $Requirements = Join-Path (Split-Path -Parent $PSScriptRoot) "requirements.txt"
}
$Requirements = [System.IO.Path]::GetFullPath($Requirements)

[void][System.IO.Directory]::CreateDirectory($WorkspacePath)
[void][System.IO.Directory]::CreateDirectory($RuntimePath)

function Invoke-ProcessWithTimeout {
    param(
        [Parameter(Mandatory = $true)]
        [string]$FilePath,
        [string]$Arguments = "",
        [int]$TimeoutSeconds = 300
    )

    $StartInfo = New-Object System.Diagnostics.ProcessStartInfo
    $StartInfo.FileName = $FilePath
    $StartInfo.Arguments = $Arguments
    $StartInfo.UseShellExecute = $false
    $StartInfo.CreateNoWindow = $true
    $StartInfo.RedirectStandardOutput = $true
    $StartInfo.RedirectStandardError = $true

    $Process = New-Object System.Diagnostics.Process
    $Process.StartInfo = $StartInfo
    if (-not $Process.Start()) {
        throw "Unable to start process: $FilePath"
    }

    $StandardOutput = $Process.StandardOutput.ReadToEndAsync()
    $StandardError = $Process.StandardError.ReadToEndAsync()
    if (-not $Process.WaitForExit($TimeoutSeconds * 1000)) {
        try {
            $Process.Kill()
        }
        catch {
        }
        throw "Process timed out: $FilePath"
    }

    [System.Threading.Tasks.Task]::WaitAll(
        [System.Threading.Tasks.Task[]]@($StandardOutput, $StandardError)
    )
    $Result = [PSCustomObject]@{
        ExitCode = $Process.ExitCode
        StdOut = $StandardOutput.Result
        StdErr = $StandardError.Result
    }
    $Process.Dispose()
    return $Result
}

function Test-PythonExecutable {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        return $false
    }

    try {
        $Result = Invoke-ProcessWithTimeout `
            -FilePath $Path `
            -Arguments '-X utf8 -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)"' `
            -TimeoutSeconds 20
        return $Result.ExitCode -eq 0
    }
    catch {
        return $false
    }
}

function Find-WorkingPython {
    $Probe = 'import sys; print(sys.executable); print(sys.version_info.major); print(sys.version_info.minor)'

    foreach ($Name in @("py.exe", "python.exe", "python3.exe")) {
        $Command = Get-Command $Name -ErrorAction SilentlyContinue | Select-Object -First 1
        if (-not $Command) {
            continue
        }

        $Prefix = if ($Name -eq "py.exe") { "-3 " } else { "" }
        try {
            $Result = Invoke-ProcessWithTimeout `
                -FilePath $Command.Source `
                -Arguments "$Prefix-X utf8 -c `"$Probe`"" `
                -TimeoutSeconds 20
        }
        catch {
            continue
        }

        if ($Result.ExitCode -ne 0) {
            continue
        }

        $Lines = @(
            $Result.StdOut -split "\r?\n" |
                ForEach-Object { $_.Trim() } |
                Where-Object { $_ }
        )
        if ($Lines.Count -ge 3 -and
            [int]$Lines[1] -eq 3 -and
            [int]$Lines[2] -ge 10 -and
            (Test-PythonExecutable $Lines[0])) {
            return $Lines[0]
        }
    }

    return $null
}

function Get-InstallerSpec {
    $Architecture = if ($env:PROCESSOR_ARCHITEW6432) {
        $env:PROCESSOR_ARCHITEW6432
    }
    else {
        $env:PROCESSOR_ARCHITECTURE
    }

    switch ($Architecture.ToUpperInvariant()) {
        "AMD64" {
            return @{
                File = "python-$PythonVersion-amd64.exe"
                Sha256 = "67b5635e80ea51072b87941312d00ec8927c4db9ba18938f7ad2d27b328b95fb"
            }
        }
        "ARM64" {
            return @{
                File = "python-$PythonVersion-arm64.exe"
                Sha256 = "377ac8fd478987940088e879441e702a71b53164d2a1e6f1d51ff77a7e470258"
            }
        }
        "X86" {
            return @{
                File = "python-$PythonVersion.exe"
                Sha256 = "fdfe385b94f5b8785a0226a886979527fd26eb65defdbf29992fd22cc4b0e31e"
            }
        }
        default {
            throw "Unsupported Windows architecture: $Architecture"
        }
    }
}

function Install-PrivatePython {
    $Python = Join-Path $PrivatePythonPath "python.exe"
    if (Test-PythonExecutable $Python) {
        return $Python
    }

    $Spec = Get-InstallerSpec
    $Installer = Join-Path $RuntimePath $Spec.File
    $Download = "https://www.python.org/ftp/python/$PythonVersion/$($Spec.File)"
    $NeedsDownload = -not (Test-Path -LiteralPath $Installer -PathType Leaf)

    if (-not $NeedsDownload) {
        $ActualHash = (Get-FileHash -LiteralPath $Installer -Algorithm SHA256).Hash.ToLowerInvariant()
        $NeedsDownload = $ActualHash -ne $Spec.Sha256
    }

    if ($NeedsDownload) {
        $Protocols = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
        if ([enum]::IsDefined([Net.SecurityProtocolType], "Tls13")) {
            $Protocols = $Protocols -bor [Net.SecurityProtocolType]::Tls13
        }
        [Net.ServicePointManager]::SecurityProtocol = $Protocols
        try {
            Invoke-WebRequest `
                -UseBasicParsing `
                -Uri $Download `
                -OutFile $Installer `
                -TimeoutSec 120
        }
        catch {
            throw "Could not download CPython from python.org ($Download): $($_.Exception.Message). " +
                "If the host already provides a Python 3.10+ runtime off PATH, re-run with -SystemPython <path> to that python.exe instead of downloading."
        }
    }

    $ActualHash = (Get-FileHash -LiteralPath $Installer -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($ActualHash -ne $Spec.Sha256) {
        throw "Python installer checksum verification failed: $Installer"
    }

    $InstallLog = Join-Path $RuntimePath "python-install.log"
    $Arguments = @(
        "/quiet"
        "InstallAllUsers=0"
        "TargetDir=`"$PrivatePythonPath`""
        "PrependPath=0"
        "AppendPath=0"
        "Include_launcher=0"
        "InstallLauncherAllUsers=0"
        "AssociateFiles=0"
        "Shortcuts=0"
        "Include_doc=0"
        "Include_test=0"
        "Include_tcltk=0"
        "Include_pip=1"
        "Include_dev=1"
        "Include_exe=1"
        "Include_lib=1"
        "/log `"$InstallLog`""
    ) -join " "

    $Result = Invoke-ProcessWithTimeout `
        -FilePath $Installer `
        -Arguments $Arguments `
        -TimeoutSeconds 600
    if ($Result.ExitCode -ne 0 -or -not (Test-PythonExecutable $Python)) {
        throw "Workspace Python installation failed. See: $InstallLog"
    }
    return $Python
}

function New-IsolatedPython {
    param(
        [string]$SourcePython,
        [string]$Directory
    )

    $Python = Join-Path $Directory "Scripts\python.exe"
    if (Test-PythonExecutable $Python) {
        return $Python
    }

    $Result = Invoke-ProcessWithTimeout `
        -FilePath $SourcePython `
        -Arguments "-X utf8 -m venv `"$Directory`"" `
        -TimeoutSeconds 180
    if ($Result.ExitCode -ne 0 -or -not (Test-PythonExecutable $Python)) {
        throw "Could not create a virtual environment with ${SourcePython}: $($Result.StdErr.Trim())"
    }
    return $Python
}

$ExternalVenv = Join-Path $RuntimePath "venv"
$PrivateVenv = Join-Path $RuntimePath "venv-$PythonVersion"
$Python = Join-Path $ExternalVenv "Scripts\python.exe"
$Source = "existing-venv"

if (-not (Test-PythonExecutable $Python)) {
    $Python = Join-Path $PrivateVenv "Scripts\python.exe"
    $Source = "private-venv"
}

if (-not (Test-PythonExecutable $Python)) {
    if ($SystemPython) {
        # The caller chose this interpreter to avoid the download, so never replace it silently.
        if (-not (Test-PythonExecutable $SystemPython)) {
            throw "-SystemPython is not a working Python 3.10+ executable: $SystemPython"
        }
        $SourcePython = $SystemPython
    }
    else {
        $SourcePython = Find-WorkingPython
    }
    if ($SourcePython) {
        try {
            $Python = New-IsolatedPython -SourcePython $SourcePython -Directory $ExternalVenv
            $Source = "system-python"
        }
        catch {
            if ($SystemPython) {
                throw
            }
            # stdout carries the runtime JSON, so diagnostics go to stderr.
            [Console]::Error.WriteLine("$($_.Exception.Message) Installing a workspace Python instead.")
        }
    }
}

if (-not (Test-PythonExecutable $Python)) {
    $PrivatePython = Install-PrivatePython
    $Python = New-IsolatedPython -SourcePython $PrivatePython -Directory $PrivateVenv
    $Source = "workspace-python"
}

$RequirementsHash = ""
if (Test-Path -LiteralPath $Requirements -PathType Leaf) {
    $RequirementsHash = (Get-FileHash -LiteralPath $Requirements -Algorithm SHA256).Hash.ToLowerInvariant()
    $Marker = Join-Path (Split-Path -Parent $Python) "..\requirements.sha256"
    $InstalledHash = if (Test-Path -LiteralPath $Marker -PathType Leaf) {
        [System.IO.File]::ReadAllText($Marker).Trim()
    }
    else {
        ""
    }

    if ($InstalledHash -ne $RequirementsHash) {
        $Result = Invoke-ProcessWithTimeout `
            -FilePath $Python `
            -Arguments "-X utf8 -m pip install --disable-pip-version-check -r `"$Requirements`"" `
            -TimeoutSeconds 600
        if ($Result.ExitCode -ne 0) {
            throw "Dependency installation failed: $($Result.StdErr.Trim())"
        }
        [System.IO.File]::WriteAllText(
            $Marker,
            $RequirementsHash,
            (New-Object System.Text.UTF8Encoding($false))
        )
    }
}

$RuntimeInfo = [ordered]@{
    python = [System.IO.Path]::GetFullPath($Python)
    source = $Source
    workspace = $WorkspacePath
    requirements_sha256 = $RequirementsHash
}
$RuntimeJson = $RuntimeInfo | ConvertTo-Json
[System.IO.File]::WriteAllText(
    (Join-Path $RuntimePath "runtime.json"),
    $RuntimeJson,
    (New-Object System.Text.UTF8Encoding($false))
)
$RuntimeInfo | ConvertTo-Json -Compress
