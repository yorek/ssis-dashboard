SQL Server Integration Services Dashboard v 0.6.7 Beta
=========================================

The purpose of this project is to provide a web-based, user-friendly, useful and nice looking SQL Server Integration Services Dashboard and a set of REST API to monitor execution of SQL Server Integration Services Packages.

![Sample Screenshot](https://cloud.githubusercontent.com/assets/2612362/4003128/76e6869e-2973-11e4-9629-2bf45acd1141.png)

## Supported Environments

* SQL Server 2012
* SQL Server 2014
* SQL Server 2016
* SQL Server 2017
* SSIS on Azure Data Factory V2 (https://docs.microsoft.com/en-us/azure/data-factory/)

## Documentation

* [Install, Configure & Run](docs/installation.md)
* [Docker Support](docs/docker.md)
* [Release Notes](docs/release-notes.md)
* [Roadmap](docs/roadmap.md)
* [Contribute](docs/contribute.md)

## Used Platforms & Tools 

SSIS Dashboard has been built using:

* Python 3.6: https://www.python.org/ 
* Flask 0.12.2: http://flask.pocoo.org/ 
* PyODBC 4.0.17: https://github.com/mkleehammer/pyodbc
* SB Admin 2 Template: http://startbootstrap.com/template-overviews/sb-admin-2/

The IDE used to build the project is Visual Studio 2017 (that's why you can see the `runserver.py` file), though now I'm also using Visual Studio Code  