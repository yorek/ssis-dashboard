# Docker Support

Execution of SSIS Dashboard in a Docker container is fully supported. 

Download and install Docker (Community Edition is enough):

[Docker](http://www.docker.com)

Once Docker is running, pull the docker image:

```
docker pull yorek/ssis-dashboard
```

## Create configuration file
After image is downloaded, create a `config.cfg` configuration file just by copying and pasting the `config.py` file. Remove all the options you don't want to change. Make sure that you use an ODBC driver that is actually loaded on the docker image. You can get a list of available ODBC drivers via running the container and querying pyodbc directly:

```
docker run -it yorek/ssis-dashboard python3
```

and once you are into the container:

```
import pyodbc
pyodbc.drivers()
exit()
```

the result will be something like:

```
['ODBC Driver 13 for SQL Server']
```

That's the driver you want to use in your connection string to connect to SQL Server or Azure SQL, for example:

```
DRIVER={ODBC Driver 13 for SQL Server};SERVER=localhost;DATABASE=SSISDB;UID=;PWD=
```

# Run Dashboard
You can now run it using the following options

```
docker run -d -p 5000:5000 --name ssis-dashboard -e DASHBOARD_CONFIG=config.cfg -v <path-of-created-config.cfg>:/usr/src/app/dashboard/config.cfg yorek/ssis-dashboard
```

Once the container is running you can connect to the dashboard via the following url:

```
http://localhost:5000/
```
