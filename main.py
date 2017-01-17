#!/usr/bin/env python3.5
# coding: utf-8

import os

from eve import Eve
from flask import send_from_directory

SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'settings.py')
app = Eve(__name__, settings=SETTINGS_PATH, static_url_path='')

app.debug = 'DEBUG' in os.environ


# the API is registered under the the URL prefix `/api`
# let's use Eve as normal Flask application for serving statics
@app.route('/static/', methods=['GET'], defaults={'path': 'index.html'})
@app.route('/static/<path:path>', methods=['GET'])
def send_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
