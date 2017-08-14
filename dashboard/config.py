# Show "Fork Me on GitHub" Banner?
GITHUB_LINK = False

# Set Flask into Debug mode
DEBUG = True

# TCP Port when running localhost
PORT = 5555

# Leave it to 'NOW' to see current data, otherwise set it to a specific 
# date to freeze queries to that point in time
AS_OF_DATE = 'NOW'

# Connectiong string to SSISDB database
CONNECTION_STRING = {
                    "main": "DRIVER={SQL Server};SERVER=localhost;DATABASE=SSISDB;UID=;PWD=",
                    }

# How many hours back in time the queries should look for data. Default if 15 days, or 360 hours
HOUR_SPAN = 360

# Google analytics code to keep track of site usage. Eg: 'UA-12345678-1'
GOOGLE_ANALYTICS = None

# Automatically refresh the page (-1 to disable autorefresh)
AUTOREFRESH = 30
