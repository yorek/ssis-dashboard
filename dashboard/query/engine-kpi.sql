DECLARE @hourspan INT = ?;
DECLARE @asOfDate DATETIME2 = NULLIF(?, 'NOW');
DECLARE @folderNamePattern NVARCHAR(100) = ?;
DECLARE @projectNamePattern NVARCHAR(100) = ?;

SET @asOfDate = ISNULL(@asOfDate, SYSDATETIME());

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
	e.start_time >= DATEADD(HOUR, -@hourspan, @asOfDate)
GROUP BY 
	e.[status]
WITH
	ROLLUP
