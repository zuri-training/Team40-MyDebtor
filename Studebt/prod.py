import os

import dj_database_url

from .settings import *

ALLOWED_HOSTS = ['studebt4-prod.herokuapp.com']

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {

    'default': dj_database_url.config()
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ['CLOUD_NAME'],
    'API_KEY': os.environ['CLOUD_API_KEY'],
    'API_SECRET': os.environ['CLOUD_API_SECRET'],
}
