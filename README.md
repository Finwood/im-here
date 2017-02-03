I'm HERE
========

Web backend for the [DEMOLA Tampere](http://tampere.demola.net)
[I'm HERE](http://demola-here.hirundoweb.com) project.

REST API
--------
One part of this repository consists of a REST API to store the provided
location data, which is (currently) hosted
[on Heroku](https://demola-here.herokuapp.com/api/).
The implementation relies on a running MongoDB instance and expects the
environment variable `MONGO_URI` to be set.

The API provides a single endpoint, `/feedback/`, which expects objects
consisting of a `user` description string, a `lat` and a `lon` float, e.g.
```
{
    "user": "Matti Heikkinen",
    "lat": 61.4474,
    "lon": 23.8625
}
```

The API is implemented using _Python Eve_, see
[the documentation](http://python-eve.org) for detailled information regarding
interaction with the API.

The script `client.py` provides a sample client implementation, capable of
inserting new data and flushing the database.

Web Interface
-------------
For convenience, the HTML web monitoring app has been integrated in this
repository. Hence, it is also available
[on Heroku](https://demola-here.herokuapp.com/static/).
