"""
The flask application package.
"""

from dashboard import config
from flask import Flask

app = Flask(__name__)
app.config.from_object(config)

from dashboard.views import *
from dashboard.processors import *
from dashboard.filters import *