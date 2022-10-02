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


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '617e747e2afc2c'
EMAIL_HOST_PASSWORD = 'e99890b04db43b'
EMAIL_PORT = '2525'