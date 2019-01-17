#!/usr/bin/env python3

### IMPORTS ###
import os
import pytest

import redis

import app

### GLOBALS ###
REDIS_SERVER_HOSTNAME = os.getenv('REDIS_SERVER_HOSTNAME', 'localhost')
REDIS_SERVER_PORT = os.getenv('REDIS_SERVER_PORT', '6379')
REDIS_SERVER_DB = os.getenv('REDIS_SERVER_DB', '0')

app.redis_client = redis.StrictRedis(host=REDIS_SERVER_HOSTNAME, port=REDIS_SERVER_PORT, db=REDIS_SERVER_DB)

### FUNCTIONS ###
@pytest.fixture
def api():
    return app.api

def test_get(api):
    r = api.requests.get("/")
    assert r.status_code == 200

### CLASSES ###