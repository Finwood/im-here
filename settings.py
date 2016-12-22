# coding: utf-8
"""Eve settings file"""

import os
import re
import yaml

ENDPOINTS_CONFIG_FILE = 'endpoints.yaml'


# Heroku support
MONGODB_URI = os.environ.get('MONGODB_URI')
if MONGODB_URI:
    match = re.match(r'^mongodb://(?P<username>.+):(?P<password>.+)' \
                     r'@(?P<host>.+):(?P<port>\d+)/(?P<dbname>.+)$',
                     MONGODB_URI)
    MONGO_HOST = match.group('host')
    MONGO_PORT = match.group('port')
    MONGO_USERNAME = match.group('username')
    MONGO_PASSWORD = match.group('password')
    MONGO_DBNAME = match.group('dbname')
else:
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_USERNAME = 'user'
    MONGO_PASSWORD = 'user'
    MONGO_DBNAME = 'apitest'


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET) and deletes (DELETE) of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=60'
CACHE_EXPIRES = 60


# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
with open(ENDPOINTS_CONFIG_FILE) as f:
    DOMAIN = yaml.load(f)
