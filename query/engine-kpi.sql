DECLARE @hourspan INT = ?;
DECLARE @projectNamePattern NVARCHAR(100) = ?;

SELECT
	status_code = ISNULL(e.[status], 0),
	status_count = COUNT(*)
FROM
	[catalog].executions e
WHERE
	e.project_name LIKE @projectNamePattern
AND
	e.start_time >= DATEADD(HOUR, -@hourspan, SYSDATETIME())
GROUP BY 
	e.[status]
WITH
	ROLLUP
