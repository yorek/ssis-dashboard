SELECT
	f.folder_id,
	f.name, 
	project_id, 
	p.folder_id, 
	p.name, 
	p.[description] 
FROM 
	[catalog].projects p
INNER JOIN
	[catalog].folders f ON p.folder_id = f.folder_id