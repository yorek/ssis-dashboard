declare @executionIdFilter bigint = ?;

select
	es.statistics_id,
	e.package_name,
	e.package_path,
	es.execution_path,
	e.executable_name,
	start_time = format(es.start_time, 'yyyy-MM-dd HH:mm:ss'),
	end_time = format(es.end_time, 'yyyy-MM-dd HH:mm:ss'),
	execution_duration_min = datediff(minute, es.start_time, es.end_time),
	execution_duration_sec = datediff(second, es.start_time, es.end_time),
	[status] = es.execution_result
from
	[catalog].[executables] e 
inner join
	[catalog].[executable_statistics] es on e.executable_id = es.executable_id and e.execution_id = es.execution_id
where
	es.execution_id = @executionIdFilter
order by
	es.start_time