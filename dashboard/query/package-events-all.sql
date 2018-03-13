DECLARE @executionId BIGINT = ?;

SELECT 
	CAST(message_time AS VARCHAR(100)) as message_time,
	[message],
	package_name,
	package_path,
	subcomponent_name,
	execution_path
FROM 
	[catalog].event_messages
WHERE
	operation_id = @executionId

