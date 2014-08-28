"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

# Configure App
import config
app.config.from_object(config)

# Import Modules
from routes import *
from processors import *
from filters import *

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    if not app.debug:
        import logging
        from logging.handlers import RotatingFileHandler
        from logging import Formatter
        file_handler = RotatingFileHandler('app.log', maxBytes = 10240, backupCount = 3, encoding = 'utf-8')
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s ''[in %(pathname)s:%(lineno)d]'))
        app.logger.addHandler(file_handler)
    
    app.run(HOST, PORT, threaded=True)
    
