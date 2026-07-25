# Computer architecture and simulators

## Environment route

- Use the named circuit, CPU, assembly, or HDL simulator.
- Prefer its native Windows build for common Windows-only teaching software. On another host, use any available Windows VM or authorized remote lab.
- Record simulator version, project file, clock or step mode, input values, and component names.

## Execution sequence

1. State the expected state transition or calculation.
2. Build or load the smallest required circuit or program.
3. Set deterministic inputs.
4. Run one clock, instruction, or test vector at a time.
5. Record registers, buses, flags, memory, signals, or output pins.
6. Compare observed values with the hand calculation or truth table.

## Minimum evidence

- Complete circuit or program context.
- Input values and clock/instruction point.
- Readable register, signal, waveform, or memory values.
- Expected-value calculation.
- Comparison of expected and observed results.

## Result analysis

Name values in the correct radix and width. Explain carry, overflow, sign, control signal, or timing behavior when relevant.

Do not infer correctness from a wiring screenshot alone, mix hexadecimal and decimal values without labels, or crop out the clock/test-vector context.
