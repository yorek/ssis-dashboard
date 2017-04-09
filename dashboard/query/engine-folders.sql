SELECT 
	f.folder_id, 
	f.[name], 
	[description] 
FROM 
	[catalog].folders f
WHERE 
	EXISTS (SELECT * FROM [catalog].projects p WHERE p.folder_id = f.folder_id)