from flask import Flask

# If you get an error on the next line on Python 3.4.0, change to: Flask('app')
# where app matches the name of this file without the .py extension.
app = Flask(__name__)

from routes import *
from processors import *
from filters import *

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app

if __name__ == '__main__':
    import os
    host = os.environ.get('SERVER_HOST', 'localhost')
    try:
        port = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        port = 5555
   
    app.config.from_object('config')
             
    if not app.debug:
        import logging
        from logging.handlers import RotatingFileHandler
        from logging import Formatter
        file_handler = RotatingFileHandler('app.log', maxBytes = 10240, backupCount = 3, encoding = 'utf-8')
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s ''[in %(pathname)s:%(lineno)d]'))
        app.logger.addHandler(file_handler)
    
    app.run(host, port, threaded=True)
    
