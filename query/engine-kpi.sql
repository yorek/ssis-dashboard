DECLARE @hourspan INT = ?;
DECLARE @projectNamePattern NVARCHAR(100) = ?;

WITH cte AS
(
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
)
SELECT
	status_description = t.d,
	status_count = ISNULL(c.status_count, 0)
FROM
	(VALUES 
		(1, 'created'),
		(2, 'running'),
		(3, 'cancelled'),
		(4, 'failed'),
		(5, 'pending'),
		(6, 'halted'),
		(7, 'succeeded'),
		(8, 'stopping'),
		(9, 'completed'),
		(0,  'executed')
	) T(c,d)
LEFT JOIN 
	cte c ON t.c = status_code
OPTION
	(RECOMPILE)