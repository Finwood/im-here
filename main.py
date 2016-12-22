#!/usr/bin/env python3.5
# coding: utf-8

import os.path
from eve import Eve

SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'settings.py')
app = Eve(__name__, settings=SETTINGS_PATH)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
