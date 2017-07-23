"""
The flask application package.
"""

from dashboard import config
from flask import Flask
import os

# global variables setup
global configurationNeeded, fileConfig

# default values setup
configurationNeeded = False
fileConfig = 'config.cfg'
envConfig = 'DASHBOARD_CONFIG'

# create Flask app by followin the best pratices
# http://flask.pocoo.org/docs/0.10/api/#application-object
app = Flask(__name__.split('.')[0])

# configure app using default configuration values
app.config.from_object(config)

# check if .cfg file and environment configuration variable exists
envConfigExists = os.getenv(envConfig) != None
fileConfigExists = os.path.isfile(fileConfig)

# if no .cfg file is found then requestes 
# will be redirected to /configure endpoint
if fileConfigExists == False:
    configurationNeeded = True

# if not environment configuration variable is specified
# then point to the local .cfg file
if envConfigExists == False and fileConfigExists == True:
    os.environ[envConfig] = '..\\' + fileConfig
    envConfigExists = True

# configure from environment variable
if envConfigExists == True:
    app.config.from_envvar(envConfig)

# now include dashboard modules
from dashboard.views import *
from dashboard.processors import *
from dashboard.filters import *