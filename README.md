# Watching Storage System

This is a project that will help you keep track of clients who have active cards, keep track of who is in the vault at
the moment and how long he has been there, show the history of visits to the vault for each client, which will make it
possible to understand who has been suspiciously long in the vault and at what time.

## Environment

### Requirements

Python3 should be already installed. Then use pip3 to install dependencies:

```bash
pip3 install -r requirements.txt
```

## Run

Launch on Mac/Linux(Python 3) or Windows:

```bash

$ python3 manage.py runserver 0.0.0.0:8000

```

You will see:

```
System check identified no issues (0 silenced).
November 22, 2022 - 23:33:56
Django version 3.2.16, using settings 'project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

Follow the development server link

### Environment variables

- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS (A list of strings representing the host/domain names that this Django site can serve. This is a security
  measure to prevent HTTP Host header attacks, which are possible even under many seemingly-safe web server
  configurations.)

#### Database settings: 

For more information
see [databases settings](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-DATABASES) :

For eg we use here postgresql database connection

- HOST
- PORT
- NAME
- USER
- PASSWORD

If you want to use your own environment variables, database settings - you should:

1. Put `.env` file near `settings.py`.
2. `.env` contains text data without quotes.

For example, if you print `.env` content, you will see:

```bash
$ cat .env
SECRET_KEY=2zjlxr=c667v6r-jzg2&ie=8vtt3l354*)4+7*kgazei=6*x&$
DEBUG=True
HOST=checkpoint.devman.org
PORT=port
NAME=name
USER=user
PASSWORD=password
ALLOWED_HOSTS=.localhost, .herokuapp.com
```

#### How to get

* We can generate a SECRET_KEY using the terminal by running the following command:

```bash
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

