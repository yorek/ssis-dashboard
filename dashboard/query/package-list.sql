DECLARE @hourspan INT = ?;
DECLARE @asOfDate DATETIME2 = NULLIF(?, 'NOW');
DECLARE @folderNamePattern NVARCHAR(100) = ?;
DECLARE @projectNamePattern NVARCHAR(100) = ?;
DECLARE @statusFilter INT = ?;
DECLARE @executionCount INT = ?;

SET @asOfDate = ISNULL(@asOfDate, SYSDATETIME());

with cteWE as
(
	select 
		operation_id, event_name, event_count = count(*)
	from 
		[catalog].event_messages 
	where
		event_name in ('OnError', 'OnWarning')
	group by
		operation_id, event_name
),
cteKPI as
(
	select
		operation_id,
		[errors] = OnError,
		warnings = OnWarning
	from
		cteWE
	pivot
		(
			sum(event_count) for event_name in (OnError, OnWarning)
		) p
),
cteLoglevel as
(
	select
		execution_id,
		cast(parameter_value as int) as logging_level
	from
		[catalog].[execution_parameter_values]
	where
		parameter_name = 'LOGGING_LEVEL'
)
select top (@executionCount)
	e.execution_id, 
	e.project_name,
	e.package_name,
	e.project_lsn,
	environment = isnull(e.environment_folder_name, '') + isnull('\' + e.environment_name,  ''), 
	e.status, 
	start_time = format(e.start_time, 'yyyy-MM-dd HH:mm:ss'),
	end_time = format(e.end_time, 'yyyy-MM-dd HH:mm:ss'),
	elapsed_time_min = format(datediff(ss, e.start_time, e.end_time) / 60., '#,0.00'),
	k.warnings,
	k.errors,
	l.logging_level
from 
	[catalog].executions e 
left outer join
	cteKPI k on e.execution_id = k.operation_id
left outer join
	cteLoglevel l on e.execution_id = l.execution_id
where 
	e.folder_name like @folderNamePattern
and
	e.project_name like @projectNamePattern
and
	e.created_time >= dateadd(hour, -@hourspan, @asOfDate)
and
	(e.[status] = @statusFilter or @statusFilter = 0)
order by 
	e.execution_id desc
option
	(recompile)
;