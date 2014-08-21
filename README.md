SQL Server Integration Services Dashboard
=========================================

The purpose of this project is to provide a web-based, user-friendly, useful and nice looking SQL Server Integration Services Dashboard and a set of REST API to monitor execution of SQL Server Integration Services Packages.
An online working demo version is available here: http://ssis-dashboard.azurewebsites.net/

##Version 

v 0.5.1 Beta

##Release Notes

v 0.5.1 Beta
Added support for "*" wildcard in project names. Now you can filter a specific project name using an url like: http://<yourserver>/project/MyPro*
Added initial support for Package Execution History. Just click on a package name and you'll see its latest 15 executions

v 0.4 Beta
First public release

##Current Release 

In the current release, no REST interface has been implemented yet.
Priority has been put to the web interface. From the web interface the page with detailed and historical information on a single package is still missing.

##Supported Environments

SQL Server 2012
SQL Server 2014

##Roadmap 

v 1.0
HTML5, Bootstrap-Based, Web Interface, directly querying database
REST API

V 1.1
Change Web Interface to use JQuery to invoke REST APIs to get data from DB. 
Remove any direct query to the database from the website dashboard

##Platforms & Tools 

SSIS Dashboard has been built using:

* Python 2.7.5: https://www.python.org/ 
* Flask 0.10.1: http://flask.pocoo.org/ 
* PyODBC 3.0.7: https://code.google.com/p/pyodbc/
* SB Admin 2 Template: http://startbootstrap.com/template-overviews/sb-admin-2/

The IDE used is the phenomenal Visual Studio 2013 with the Python addin "Python Tools For Visual Studio"

https://pytools.codeplex.com/

##Installation Procedure

###Install Python 
Download Python 2.7.5 and install using default options from https://www.python.org/ website.
At the end of the installation process you'll have a `C:\Python27` folder

###Install PIP
Download and install the pip, one of the most used Python package managers. First of all the "get-pip.py" script has to be downloaded. It can be done using PowerShell
```
Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile C:\Python27\get-pip.py
```
or `curl` or `wget` it fouy prefer (both are aliases for the above PowerShell command, if you don't really want to also install one of them)
Once downloaded, just run it:
```
cd c:\Python27
python get-pip.py
```
Done.
If you want more detailed installation instruction, please refer to pip's main documentation:
http://pip.readthedocs.org/en/latest/installing.html#install-pip


###Install PyODBC
Download PyODBC 3.0.7 (pyodbc-3.0.7.win32-py2.7.exe) from 
	
https://code.google.com/p/pyodbc/downloads/list 

and install it using the default options.
	
###Get SSIS Dashboard Files
Get the SSIS Dashboard source files from GitHub

https://github.com/yorek/ssis-dashboard 

For example store them into 
```
c:\ssis-dashboard
```
folder.
	
###Configure SSIS Dashboard
All you have to do put the correct connection string in the 
```
config.txt 
```
file. That's it.

###Install Requirements
In order for SSIS Dashboard to run, the micro-framework Flask has to be installed. It's easy as doing this
```
cd c:\ssis-dashboard
c:\python27\Scripts\pip.exe install -r requirements.txt
```
provided that you downloaded the SSIS Dashboard source files into a directory named `ssis-dashboard` in the `C:` drive
	
###Run SSIS Dashboard
After pip has finished its work, it's time to run the web app.  Again it's as easy as doing this:
```
cd c:\ssis-dashboard
c:\Python27\python.exe app.py
```
now you can open your preferred browser and point to 
```
http://locahost:5555/
```
or the correct address name, and voilà, SSIS Dashboard running for you.
	
