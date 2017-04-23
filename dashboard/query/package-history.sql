DECLARE @folderNamePattern NVARCHAR(100) = ?;
DECLARE @projectNamePattern NVARCHAR(100) = ?;
DECLARE @packageNamePattern NVARCHAR(100) = ?;

WITH cte AS 
(
	SELECT TOP (50)
		e.execution_id, 
		e.project_name,
		e.package_name,
		e.environment_name,
		e.project_lsn,
		e.status,
		e.start_time,
		e.end_time,
		elapsed_time_min = datediff(ss, e.start_time, e.end_time) / 60.,	
		avg_elapsed_time_min = avg(datediff(ss, e.start_time, e.end_time) / 60.) OVER (ORDER BY e.start_time ROWS BETWEEN 5 PRECEDING AND CURRENT ROW)
	FROM 
		catalog.executions e
	WHERE 
		e.status IN (2,7)
	AND
		e.folder_name LIKE @folderNamePattern
	AND
		e.package_name like @packageNamePattern
	AND
		e.project_name LIKE @projectNamePattern
	ORDER BY 
		e.execution_id DESC
)
SELECT
	execution_id, 
	project_name,
	package_name,
	environment_name,
	project_lsn,
	[status],
	start_time = format(start_time, 'yyyy-MM-dd HH:mm:ss'),
	end_time = format(CASE WHEN end_time IS NULL THEN dateadd(minute, cast(CEILING(avg_elapsed_time_min) AS int), start_time) ELSE end_time end, 'yyyy-MM-dd HH:mm:ss'),
	elapsed_time_min = format(CASE WHEN end_time IS NULL THEN avg_elapsed_time_min ELSE elapsed_time_min end, '#,0.00'),
	avg_elapsed_time_min = format(avg_elapsed_time_min, '#,0.00'),
	percent_complete = format(100 * (DATEDIFF(ss, start_time, SYSDATETIMEOFFSET()) / 60.) / avg_elapsed_time_min, '#,0.00'),
	has_expected_values = CASE WHEN end_time IS NULL THEN 1 ELSE 0 END
FROM
	cte
ORDER BY
	execution_id DESC