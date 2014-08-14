SQL Server Integration Services Dashboard
=========================================

The purpose of this project is to provide a web-based, user-friendly, useful and nice looking SQL Server Integration Services Dashboard and a set of REST API to monitor execution of SQL Server Integration Services Packages.

***
*** Version 
***

v 0.1 Alpha

***
*** Platforms & Tools 
***

SSIS Dashboard has been built using:

Python 2.7.5: https://www.python.org/ 
Flask 0.10.1: http://flask.pocoo.org/ 
PyODBC 3.0.7: https://code.google.com/p/pyodbc/
SB Admin 2 Template: http://startbootstrap.com/template-overviews/sb-admin-2/

The IDE used is the phenomenal Visual Studio 2013 with the Python addin "Python Tools For Visual Studio"

https://pytools.codeplex.com/

***
*** Installation Procedure
***

1. Install Python 2.7.5
	Download Python 2.7.5 and install using default options from https://www.python.org/ website.
	At the end of the installation process you'll have a C:\Python27 folder

2. Install PIP
	Download and install the pip, one of the most used Python package managers. First of all the "get-pip.py" script has to be downloaded. It can be done using PowerShell

	Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile C:\Python27\get-pip.py

	or cUrl or wget it fouy prefer (both are aliases for the above PowerShell command, if you don't really want to also install one of them)
	Once downloaded, just run it:

	cd c:\Python27
	python get-pip.py

	Done.
	If you want more detailed installation instruction, please refer to pip's main documentation:
	http://pip.readthedocs.org/en/latest/installing.html#install-pip


3. Install PyODBC 3.0.7
	Download PyODBC 3.0.7 (pyodbc-3.0.7.win32-py2.7.exe) from 
	
	https://code.google.com/p/pyodbc/downloads/list 

	and install it using the default options.
	
4. Get SSIS Dashboard Files
	Get the SSIS Dashboard source files from GitHub
	
	https://github.com/yorek/ssis-dashboard 

	For example store them into 
	
	c:\ssis-dashboard

	folder.
	
5. Configure SSIS Dashboard
	All you have to do put the correct connection string in the 
	
	config.txt 
	
	file. That's it.

5. Install Requirements
	In order for SSIS Dashboard to run, the micro-framework Flask has to be installed. It's easy as doing this
	
	cd c:\ssis-dashboard
	c:\python27\Scripts\pip.exe install -r requirements.txt

	provided that you downloaded the SSIS Dashboard source files into a directory named ssis-dashboard in the C: drive
	
6. Run SSIS Dashboard
	After pip has finished its work, it's time to run the web app.  Again it's as easy as doing this:
	
	cd c:\ssis-dashboard
	c:\Python27\python.exe app.py
	
	now you can open your preferred browser and point to 
	
	http://<your-machine-ip>:5555/
	
	and voilà, SSIS Dashboard running for you.
	

***
*** Current Release 
***

***
*** Roadmap 
***