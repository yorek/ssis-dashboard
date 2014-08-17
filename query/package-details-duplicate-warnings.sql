DECLARE @executionId BIGINT = ?;

SELECT 
	message_time,
	[message],
	package_name,
	package_path,
	subcomponent_name,
	execution_path
FROM 
	[catalog].event_messages
WHERE
	operation_id = @executionId
AND
	event_name = 'OnWarning'
AND
	[message] LIKE '%duplicate%' 

