DECLARE @projectNamePattern NVARCHAR(100) = '%'--EPSON-Data-%'
DECLARE @packageNamePattern NVARCHAR(100) = '%';
DECLARE @executionIdFilter BIGINT = NULL;

DECLARE @executionId BIGINT, @packageName NVARCHAR(1000) 
SELECT 
	TOP 1 @executionId = e.execution_id, @packageName = e.package_name 
FROM 
	[catalog].executions e
WHERE 
	e.project_name LIKE @projectNamePattern
AND
	e.package_name LIKE @packageNamePattern
AND
	e.execution_id = ISNULL(@executionIdFilter, e.execution_id)
ORDER BY 
	e.execution_id DESC
OPTION
	(RECOMPILE);

-- Show successfull execution history
SELECT TOP 15
	e.execution_id, 
	e.project_name,
	e.package_name,
	e.project_lsn,
	e.status, 
	status_desc = CASE e.status 
						WHEN 1 THEN 'Created'
						WHEN 2 THEN 'Running'
						WHEN 3 THEN 'Cancelled'
						WHEN 4 THEN 'Failed'
						WHEN 5 THEN 'Pending'
						WHEN 6 THEN 'Ended Unexpectedly'
						WHEN 7 THEN 'Succeeded'
						WHEN 8 THEN 'Stopping'
						WHEN 9 THEN 'Completed'
					END,
	e.start_time,
	e.end_time,
	elapsed_time_min = datediff(ss, e.start_time, e.end_time)
FROM 
	catalog.executions e 
WHERE 
	e.status IN (2,7)
AND
	e.package_name = @packageName
ORDER BY 
	e.execution_id DESC