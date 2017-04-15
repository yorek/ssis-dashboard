DECLARE @executionIdFilter BIGINT = ?;

WITH 
ctePRE AS 
(
	SELECT * FROM catalog.event_messages em 
	WHERE em.event_name IN ('OnPreExecute')
	
), 
ctePOST AS 
(
	SELECT * FROM catalog.event_messages em 
	WHERE em.event_name IN ('OnPostExecute')
),
cteFINAL AS
(
	SELECT		
		rn = ROW_NUMBER() OVER (PARTITION BY b.event_message_id ORDER BY e.event_message_id),
		b.event_message_id,
		b.message_source_type,
		b.package_path,
		b.package_name,
		b.execution_path,
		b.message_source_name,
		pre_message_time = b.message_time,
		post_message_time = e.message_time
	FROM
		ctePRE b
	LEFT OUTER JOIN
		ctePOST e ON b.operation_id = e.operation_id AND b.package_name = e.package_name AND b.message_source_id = e.message_source_id AND e.event_message_id > b.event_message_id
	WHERE
		b.operation_id = @executionIdFilter
	AND
		b.package_path = '\Package'
)
SELECT
	event_message_id,
	message_source_type,
	package_name,
	package_path,
	execution_path,
	message_source_name,
	pre_message_time = format(pre_message_time, 'yyyy-MM-dd HH:mm:ss'),
	post_message_time = format(post_message_time, 'yyyy-MM-dd HH:mm:ss'),
	elapsed_time_min = datediff(mi, pre_message_time, post_message_time)
FROM
	cteFINAL
WHERE
	rn = 1
AND
	CHARINDEX('\', execution_path, 2) > 0
ORDER BY
	event_message_id desc
;
