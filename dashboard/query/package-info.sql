DECLARE @executionId BIGINT = ?;

SELECT 
	folder_name, 
	project_name, 
	package_name, 
	project_lsn 
FROM 
	[catalog].executions 
WHERE	
	execution_id = @executionId;
