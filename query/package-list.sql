DECLARE @hourspan INT = ?;
DECLARE @projectNamePattern NVARCHAR(100) = ?;
DECLARE @statusFilter INT = ?;

WITH cteWE AS
(
	SELECT 
		operation_id, event_name, event_count = COUNT(*)
	FROM 
		[catalog].event_messages 
	WHERE
		event_name IN ('OnError', 'OnWarning')
	GROUP BY
		operation_id, event_name
),
cteKPI AS
(
	SELECT
		operation_id,
		[errors] = OnError,
		warnings = OnWarning
	FROM
		cteWE
	PIVOT
		(
			SUM(event_count) FOR event_name IN (OnError, OnWarning)
		) p
)
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
	start_time = format(e.start_time, 'yyyy-MM-dd HH:mm:ss'),
	end_time = format(e.end_time, 'yyyy-MM-dd HH:mm:ss'),
	elapsed_time_min = datediff(ss, e.start_time, e.end_time) / 60.,
	k.warnings,
	k.errors
FROM 
	[catalog].executions e 
LEFT OUTER JOIN
	cteKPI k ON e.execution_id = k.operation_id
WHERE 
	e.project_name LIKE @projectNamePattern
AND
	e.start_time >= DATEADD(HOUR, -@hourspan, SYSDATETIME())
AND
	(e.[status] = @statusFilter or @statusFilter = 0)
ORDER BY 
	e.execution_id DESC
OPTION
	(RECOMPILE)
;