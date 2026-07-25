# SQL and databases

## Environment route

- Prefer native Windows for SQL Server, SSMS, Access, and Windows-only database clients.
- MySQL, PostgreSQL, SQLite, and cross-platform clients may run on the current host when the assignment accepts them.
- Record DBMS version, client, database name, schema state, and whether sample data was supplied or created.

Use synthetic course data. Do not import workplace or personal records.

## Execution sequence

1. Show or describe the starting schema.
2. Run DDL before DML that depends on it.
3. Insert a small, deterministic dataset.
4. Execute each required query separately.
5. Verify affected rows, result rows, constraints, and object creation.
6. Preserve the exact SQL submitted in the report.

## Minimum evidence

- Connection target without exposed credentials.
- SQL text and successful execution state.
- Result grid with column names and row count.
- Object browser or metadata query for tables, views, indexes, or procedures when relevant.
- Error and correction when troubleshooting materially changed the solution.

## Result analysis

Name the clause responsible for the output:

- join condition and matched keys;
- filter predicate;
- grouping key and aggregate;
- subquery relationship;
- constraint or transaction behavior.

Do not use a result grid without the query, claim data changed without an affected-row count, or hide an error behind a later screenshot.
