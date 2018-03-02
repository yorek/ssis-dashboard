# Docker Support

Execution of SSIS Dashboard in a Docker container is fully supported. 

Download and install Docker (Community Edition is enough):

[Docker](http://www.docker.com)

Once Docker is running, pull the docker image:

```
docker pull yorek/ssis-dashboard
```

after image is downloaded, create a `config.cfg` configuration file just by copying and pasting the `config.py` file. Remove all the options you don't want to change. Make sure tha

run it using the following options

```
docker run -d -p 5000:5000 --name ssis-dashboard -e DASHBOARD_CONFIG=config.cfg -v <path-of-created-config.cfg>:/usr/src/app/dashboard/config.cfg yorek/ssis-dashboard
```

Once the container is running you can connect to the dashboard via the following url:

```
http://locahost:5000/
```