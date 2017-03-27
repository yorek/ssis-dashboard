declare @executionId bigint = ?;

select 
	object_type,
	object_type_desc = 
		case object_type 
			when 20 then 'Project'
			when 30 then 'Package'
			when 50 then 'System'
			else 'Unknown'
		end,
	parameter_data_type,
	parameter_name,
	parameter_value = cast(parameter_value as nvarchar(max)),
	sensitive,
	[required], 
	value_set,
	runtime_override
from 
	[catalog].[execution_parameter_values] 
where 
	[execution_id] = @executionId