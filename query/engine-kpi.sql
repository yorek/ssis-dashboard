DECLARE @hourspan INT = ?;
DECLARE @folderNamePattern NVARCHAR(100) = ?;
DECLARE @projectNamePattern NVARCHAR(100) = ?;

SELECT
	status_code = ISNULL(e.[status], 0),
	status_count = COUNT(*)
FROM
	[catalog].executions e
WHERE
	e.folder_name LIKE @folderNamePattern
AND
	e.project_name LIKE @projectNamePattern
AND
	e.start_time >= DATEADD(HOUR, -@hourspan, SYSDATETIME())
GROUP BY 
	e.[status]
WITH
	ROLLUP
