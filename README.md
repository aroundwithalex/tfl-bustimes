# Bustimes

Bustimes is a Python library that retrives information from the [TFL Bus Arrivals API](https://api.tfl.gov.uk/StopPoint/490009333W/arrivals) and displays it within a Flask application.  The Flask application itself is hosted on Heroku, at this [address](https://tfl-bustimes.herokuapp.com)

## Installation

The best way to install the project is to clone the source code using Git. This can either be done using the GitHub interface, or by calling:

```git
git clone https://github.com/aroundwithalex/tfl-bustimes.git
```

Alternatively, you can interact with the application without cloning the source code.  The [TFL Bustimes app](https://tfl-bustimes.herokuapp.com) will provide a fully functional interface: the same as you would get if you ran it locally on your machine.

## Usage

If you elect to download the source code, you first need to ensure that Flask and other dependencies have been installed in your virtual environment (see below for details about how to do this).  After activating the virtual environment, you should then be able to run the following command:

```python

flask run

```
This should open the Flask server, and from there you should be able to directly interact with the application.

The backend Postgres database, which stores all calls to the TFL API, has been exposed as an API in its own right.  It is available to query via a GET request, and you should be able to retrieve the data via:

```python

import requests

r = requests.get('https://tfl-bustimes.herokuapp.com/api/history')
r.json()

```

The data should be returned as a list of dictionaries, and you should be able to iterate through this to see each individual record within the database.


## Development Setup

First, ensure that you create a Python virtual environment in the top level directory.  Navigate to the top level directory and run the following command:

```bash

python -m venv env
source env/bin/activate
```

The virtual environment should now be set up.  Next, install the modules included in requirements.txt using the following command: 

```
python -m pip install -r requirements.txt

```

After the requirements have been installed, you should be able to run the Flask server.  In order to run the Flask server, run the following command on the top level directory:

```python

flask run

```

To run the unittests, run the following command against the top level directory:

```python

python -m unittest discover

```

The unittest test runner should automatically find the unit tests and run them.  Any issues can be reported using the Issue feature on GitHub.

## License

[MIT](https://choosealicense.com/licenses/mit)

## Future Tasks

There are several ways to extend this project.  We could refactor the Flask app, to take advantage of application factory methods and blueprints. Also, we could publish a subset of the features shown here to PyPI, namely methods to query the two APIs. The frontend heavily utilises Bootstrap, and we could replace this with a JavaScript frontend such as Angular or React.
