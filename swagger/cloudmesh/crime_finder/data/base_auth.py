#!/usr/bin/env python3

import flask
import yaml

credentials="config/credentials.yml"

try:
    from decorator import decorator
except ImportError:
    import sys
    import logging
    logging.error('Missing dependency. Please run `pip install decorator`')
    sys.exit(1)
    
try:
    config = yaml.load(open(credentials))   
except FileNotFoundError:
    import sys
    import logging
    logging.error('Please create credentials.yml with username and password')
    sys.exit(1)    
    

# validate the credentials with credentials.yaml
def check_auth(username: str, password: str):
    return username == config['applicationAdmin']['username'] and password == config['applicationAdmin']['password']
       

def failed():
    return flask.Response('Login credentials are wrong', 401,
                          {'WWW-Authenticate': 'Basic realm="Login Required"'})


@decorator
def requires_auth(f: callable, *args, **kwargs):
    auth = flask.request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return failed()
    return f(*args, **kwargs)
