import os
from .common import * 

ALLOWED_HOSTS = ['studebt4-prod.herokuapp.com']

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

