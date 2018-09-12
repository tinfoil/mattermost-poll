"""This file contains all user settings of the application"""

import os

# Path to the database file.
DATABASE = 'polls.db'

# Address to listen on
WEBSERVER_ADDRESS = '0.0.0.0'

# Port of the webserver
WEBSERVER_PORT = 5000

# Optional list of Mattermost tokens (list of strings e.g. ['abc123', 'xyz321'])
MATTERMOST_TOKENS = filter(lambda x: x, os.environ.get('MATTERMOST_TOKENS', '').split(','))

# URL of the Mattermost server
MATTERMOST_URL = os.environ.get('MATTERMOST_URL', 'http://localhost')

# Private access token of some user.
# Required to resolve username in 'public' polls.
# https://docs.mattermost.com/developer/personal-access-tokens.html
MATTERMOST_PA_TOKEN = os.environ.get('MATTERMOST_PA_TOKEN')

# Uncomment the following lines to enable file logging:
#import logging
#logging.basicConfig(filename='poll.log', level=logging.DEBUG)
