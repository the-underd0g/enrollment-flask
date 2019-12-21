import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x87\xa1\x1a\x8e\xb5\x8b\xd0\xf8 \xf3Rr\x08U\xfe\xcf'
    MONGODB_SETTINGS = {
        'db' : 'UTA_Enrollment'
    }

