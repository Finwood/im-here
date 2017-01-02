#!/usr/bin/env python3
# coding: utf-8
"""Small and simple CLI for Demola-HERE.

Usage:
    client.py (submit | clear)
    client.py --help

Arguments:
    submit  Post sample data to API.
    clear   Clear entire dataset.

"""

from docopt import docopt
import requests
import yaml

ENDPOINT = 'http://demola-here.herokuapp.com/api/feedback/'


def submit_sample():
    ipinfo = requests.get('http://ipinfo.io')
    ipinfo.raise_for_status()
    ip = ipinfo.json().get('ip', '0.0.0.0')
    lat, lon = map(float, ipinfo.json().get('loc', '0.0,0.0').split(','))

    data = {'user': ip,
            'lat': lat,
            'lon': lon}

    res = requests.post(ENDPOINT, data=data)
    # res.raise_for_status()
    print(yaml.dump(res.json()))

def clear_remote():
    res = requests.delete(ENDPOINT)
    print(res.text)

if __name__ == '__main__':
    args = docopt(__doc__)
    if args['clear']:
        clear_remote()
    if args['submit']:
        submit_sample()
