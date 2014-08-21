DECLARE @packageNamePattern NVARCHAR(100) = ?;
DECLARE @projectNamePattern NVARCHAR(100) = ?;

SELECT TOP (15)
	e.execution_id, 
	e.project_name,
	e.package_name,
	e.project_lsn,
	e.status,
	e.start_time,
	e.end_time,
	elapsed_time_min = datediff(ss, e.start_time, e.end_time) / 60.
FROM 
	catalog.executions e 
WHERE 
	e.status IN (2,7)
AND
	e.package_name like @packageNamePattern
AND
	e.project_name LIKE @projectNamePattern
ORDER BY 
	e.execution_id DESC