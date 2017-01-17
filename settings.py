# coding: utf-8
"""Eve settings file"""

import os
import re
import yaml

ENDPOINTS_CONFIG_FILE = 'endpoints.yaml'


# make API available at `/api/`
URL_PREFIX = 'api'

DEBUG = os.environ.get('DEBUG', False)

# Heroku support
if 'MONGODB_URI' in os.environ:
    MONGO_URI = os.environ['MONGODB_URI']
else:
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_USERNAME = ''
    MONGO_PASSWORD = ''
    MONGO_DBNAME = 'eve'


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET) and deletes (DELETE) of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'DELETE']

CACHE_CONTROL = 'no-cache'

HATEOAS = False
PAGINATION_DEFAULT = 10

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


# enable Operation Log for debuging purposes
OPLOG = True
OPLOG_AUDIT = True
OPLOG_ENDPOINT = 'oplog'

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
with open(ENDPOINTS_CONFIG_FILE) as f:
    DOMAIN = yaml.load(f)
