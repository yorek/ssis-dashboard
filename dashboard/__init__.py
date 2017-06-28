"""
The flask application package.
"""

from dashboard import config
from flask import Flask

app = Flask(__name__)
app.config.from_object(config)
app.config.from_envvar('DASHBOARD_CONFIG')

from dashboard.views import *
from dashboard.processors import *
from dashboard.filters import *