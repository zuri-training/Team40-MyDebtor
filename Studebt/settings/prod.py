import os
import dj_database_url
from .common import * 

ALLOWED_HOSTS = ['studebt4-prod.herokuapp.com']

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    
    'default': dj_database_url.config()
}