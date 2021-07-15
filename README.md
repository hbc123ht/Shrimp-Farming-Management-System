# Shrimp-Farming-Management-System
A modern system to assist shrimp farmers in controlling and improving the quality of water utilizing IBM cloud.

## Installation

### Set up virtual environment and install dependencies

```console
$ python3 -m venv venv
$ . venv/bin/activate
$ pip3 install -r requirements.txt
```

### Create and apply migrations

```console
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

### Run server on localhost

```console
$ python3 manage.py runserver
```

