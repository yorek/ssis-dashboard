SQL Server Integration Services Dashboard v 0.6.4 Beta
=========================================

The purpose of this project is to provide a web-based, user-friendly, useful and nice looking SQL Server Integration Services Dashboard and a set of REST API to monitor execution of SQL Server Integration Services Packages.

![Sample Screenshot](https://cloud.githubusercontent.com/assets/2612362/4003128/76e6869e-2973-11e4-9629-2bf45acd1141.png)

Installation procedure is here: https://github.com/yorek/ssis-dashboard#installation-procedure

## Release Notes

### v 0.6.5 Beta

* Moved to Roboto font for better readability
* Navigation menu correctly sort items (Issue #19)
* Started using pylint to have cleaner code

### v 0.6.4 Beta

* Updated to Python 3
* Dropped usage of MetisMenu in favor of SmartMenus
* Added package execution chart
* Moved the package execution details in a dedicated page
* Added the ability to display all events
* Added a page to show parameters execution values and parameter overrides
* Code cleanup and refactored

### v 0.6.3 Beta

* Added first support to show/hide navigation panel
* Included Environment informations in package list (Issue #5)
* Upgraded to Font Awesome v 4.5.0
* Upgraded to Bootstrap 3.3.6
* Added refresh page button

### v 0.6.1 Beta

* Updated Morris.js to v 0.5.1
* Updated MetisMenu to v 1.1.1
* Added information on "Child" Packages
* Added more detail to the "Package Execution History" page. Also added an estimated end time / elapsed time for running packages, using a moving average of 7 steps.
* Added navigation sidebar in the main page that shows available folders and projects
* Added support for folders and project filtering
* Changed configuration file in order to comply with Python/Flask standards
* Cleaned Up code in order to follow Python best pratices (still a lot to do :))

### v 0.5.2 Beta

Added support for "\*" wildcard in project names. Now you can filter a specific project name using an url like: 
```
http://<yourserver>/project/MyPro*
```
Added initial support for Package Execution History. Just click on a package name and you'll see its latest 15 executions

### v 0.4 Beta

First public release

## Current Release 

In the current release, no REST interface has been implemented yet.
Priority has been put to the web interface. From the web interface the page with detailed and historical information on a single package is still missing.

## Supported Environments

* SQL Server 2012
* SQL Server 2014
* SQL Server 2016

## Roadmap 

### Current
* HTML5, Bootstrap-Based, Web Interface, directly querying database
* REST API

### vNext
* Change Web Interface to use JQuery to invoke REST APIs to get data from DB. 
* Remove any direct query to the database from the website dashboard

## Platforms & Tools 

SSIS Dashboard has been built using:

* Python 3.5: https://www.python.org/ 
* Flask 0.12.1: http://flask.pocoo.org/ 
* PyODBC 3.0.10: https://github.com/mkleehammer/pyodbc
* SB Admin 2 Template: http://startbootstrap.com/template-overviews/sb-admin-2/

The IDE used is the phenomenal Visual Studio 2013 with the Python addin "Python Tools For Visual Studio"

https://pytools.codeplex.com/

## Installation Procedure

### Install Python 
Download Python 3.5 and install using default options from https://www.python.org/ website.
At the end of the installation process you'll have a `C:\Python35` folder.
Also the Anaconda distribution is supported.

### Get SSIS Dashboard Files
Get the SSIS Dashboard source files from GitHub

https://github.com/yorek/ssis-dashboard 

For example store them into 
```
c:\ssis-dashboard
```
folder.
	
### Configure SSIS Dashboard
All you have to do put the correct connection string in the 
```
config.py 
```
file. That's it.

### Install Requirements
In order for SSIS Dashboard to run, the micro-framework Flask and PyODBC have to be installed. It's easy as doing this
```
cd c:\ssis-dashboard
c:\<python-install-folder>\Scripts\pip.exe install -r requirements.txt
```
provided that you downloaded the SSIS Dashboard source files into a directory named `ssis-dashboard` in the `C:` drive.

Please note that the above installation steps install the packages in the global catalog. If you are already using Python it's better to create a virtual environment and have the package installed there.
	
### Run SSIS Dashboard
After pip has finished its work, it's time to run the web app.  Again it's as easy as doing this:
```
cd c:\ssis-dashboard
c:\<python-install-folder>\python.exe runserver.py
```
now you can open your preferred browser and point to 
```
http://locahost:5555/
```
and voilà, SSIS Dashboard running for you.

If you want to be able to access the dashboard also from a different address than "localhost", you just have to set the `SERVER_HOST` environment variable, before running the app:

```
set SERVER_HOST=myserver.domain.name
cd c:\ssis-dashboard
c:\<python-install-folder>\python.exe runserver.py
```



	
