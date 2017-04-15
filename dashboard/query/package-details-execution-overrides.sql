declare @executionId bigint = ?;

select 
	property_path,
	property_value = cast(property_value as nvarchar(max))
from 
	[catalog].[execution_property_override_values] 
where 
	[execution_id] = @executionId
