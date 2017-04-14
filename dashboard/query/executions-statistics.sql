declare @hourspan int = ?;
with numbers as 
(
	select
		n = row_number() over (order by a.object_id)
	from
		sys.all_columns a cross join sys.all_columns b
), calendar as
(
	select distinct 
		cast(dateadd(hour, n * -1, sysdatetime()) as date) as calendar_date
	from
		numbers
	where 
		n <= @hourspan
), executions as 
(
	select
		[created_date] = cast(e.created_time as date),
		*
	from
		[catalog].executions e
	where
		cast(e.created_time as date) is not null
)
select
	c.[calendar_date],
	created_packages = count(e.execution_id),
	executed_packages = sum(case when e.start_time is not null then 1 else 0 end),
	succeeded_packages = sum(case when e.[status] = 7 then 1 else 0 end),
	failed_packages = sum(case when e.[status] = 4 then 1 else 0 end)
from
	calendar c 
left join
	executions e on e.created_date = c.calendar_date
group by
	c.[calendar_date]
