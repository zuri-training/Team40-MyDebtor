import os
import random
import string
from datetime import datetime

def get_passport_path(request, filename):
    original_filename = filename
    nowTime = datetime.now().strftime('%Y_%m_%d_%H:%M:%S_')
    filename = "%s%s%s" % ('IMG_', nowTime, original_filename)

    return os.path.join('passport/', filename)

def get_complaint_path(request, filename):
    original_filename = filename
    nowTime = datetime.now().strftime('%Y_%m_%d_%H:%M:%S_')
    filename = "%s%s%s" % ('IMG_', nowTime, original_filename)

    return os.path.join('complaint/', filename)

def get_credentials_path(request, filename):
    original_filename = filename
    nowTime = datetime.now().strftime('%Y_%m_%d_%H:%M:%S_')
    filename = "%s%s%s" % ('IMG_', nowTime, original_filename)

    return os.path.join('credentials/', filename)


def get_school_logo_path(request, filename):
    original_filename = filename
    nowTime = datetime.now().strftime('%Y_%m_%d_%H:%M:%S_')
    filename = "%s%s%s" % ('IMG_', nowTime, original_filename)

    return os.path.join('school_logo/', filename)


def reg_number_generator (length = 10, chars = string.digits):
    return ''.join(random.choice(chars) for _ in range(length))