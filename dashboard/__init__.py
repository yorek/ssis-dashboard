"""
The flask application package.
"""

from dashboard import config
from flask import Flask
import os

app = Flask(__name__)

app.config.from_object(config)

envConfig = 'DASHBOARD_CONFIG'
fileConfig = 'config.cfg'

envConfigExists = os.getenv(envConfig) != None
fileConfigExists = os.path.isfile('config.cfg')

if envConfigExists == False and fileConfigExists == True:
    os.environ[envConfig] = '..\\' + fileConfig

app.config.from_envvar(envConfig)

from dashboard.views import *
from dashboard.processors import *
from dashboard.filters import *