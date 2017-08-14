# Set Flask into Debug mode
DEBUG = False

# Connectiong string to SSISDB database
CONNECTION_STRING = {
                    "main": "DRIVER={SQL Server};SERVER=localhost;DATABASE=SSISDB;UID=;PWD=",
                    }

# How many hours back in time the queries should look for data. Default if 15 days, or 360 hours
HOUR_SPAN = 360

# Automatically refresh the page every specified seconds (-1 to disable autorefresh)
AUTOREFRESH = 30

# Google analytics code to keep track of site usage. Eg: 'UA-12345678-1'
GOOGLE_ANALYTICS = None