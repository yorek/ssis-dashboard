IF (SERVERPROPERTY('EDITION') = 'SQL Azure') 
BEGIN
	SELECT [server_name] = 'DEMO', [service_name] = 'DEMO'
END ELSE BEGIN
	EXEC('SELECT [server_name] = @@SERVERNAME, [service_name] = @@SERVICENAME')
END