# Installation Procedure

## Readme First! 
If you're not confident with Python, or don't what to install it on your machine, or you just prefer a ready-to-go solution, you can use the docker image as described [here](docker-support.md).

## Install Python 
Download Python 3.6 and install using default options from https://www.python.org/ website.
At the end of the installation process you'll have a `C:\Python36` folder.
If you prefer to use the  Anaconda distribution, that is supported too.

## Get SSIS Dashboard Files
Get the SSIS Dashboard source files from GitHub

https://github.com/yorek/ssis-dashboard 

For example store them into 
```
c:\ssis-dashboard
```
folder.

## Configure SSIS Dashboard
All you have to do put the correct connection string and values in the 
```
config.cfg
```
file. The file needs to be created the very first time. To do that just create an empty text file in root folder and
then copy the content from ```dashboard/config.py``` and put the configuration values correct for you. Chances are that you only need to set the correct connecting string: all the other values may be left as you find them.
If you are using Google Analytics and want to track how the dashboard is used, you can put the Google Analytics code in the related configuration option, for example:

```
GOOGLE_ANALYTICS = 'UA-01234567-1'
```

## Install Requirements
In order for SSIS Dashboard to run, the micro-framework Flask and PyODBC have to be installed. It's easy as doing this
```
cd c:\ssis-dashboard
c:\<python-install-folder>\Scripts\pip.exe install -r requirements.txt
```
provided that you downloaded the SSIS Dashboard source files into a directory named `ssis-dashboard` in the `C:` drive.

Please note that the above installation steps install the packages in the global catalog. If you are already using Python it's better to create a virtual environment and have the package installed there (instruction for Windows using the standard Python 3 distribution):

```
cd c:\ssis-dashboard
python -m venv env
env\Script\activate
```

and then proceeed to install package using the usual pip command:

```
c:\<python-install-folder>\Scripts\pip.exe install -r requirements.txt
```

# Run SSIS Dashboard
Since Flask 0.12 the preferred method to run Flask application is to use ```flask``` command:

```
set FLASK_APP=dashboard/__init__.py
flask run --host=0.0.0.0
```

in this case the server will listen on port 5000 by default:
```
http://localhost:5000/
```

for more information, like 
- enabling Debug mode
- changing default tcp port
- allowing the app to serve different hostname than "localhost"

please read the [Flask Quickstart](http://flask.pocoo.org/docs/0.12/quickstart/)
	
# Run SSIS Dashboard (deprecated)
This section remain just beacuse it describes how you can run your application just like Visual Studio will do when you debug it, just in case you need to reproduce the same behaviour.

After pip has finished its work, it's time to run the web app.  Again it's as easy as doing this:
```
cd c:\ssis-dashboard
c:\<python-install-folder>\python.exe runserver.py
```
now you can open your preferred browser and point to 
```
http://localhost:5555/
```
and voilà, SSIS Dashboard running for you.

If you want to be able to access the dashboard also from a different address than "localhost", you just have to set the `SERVER_HOST` environment variable, before running the app:

```
set SERVER_HOST=myserver.domain.name
cd c:\ssis-dashboard
c:\<python-install-folder>\python.exe runserver.py
```
