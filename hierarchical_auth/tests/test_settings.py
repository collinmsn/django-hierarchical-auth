import os

BASE_DIR = os.path.dirname(__file__)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'mptt',
    'hierarchical_auth',
    'hierarchical_auth.tests',
)

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'mydatabase',
    }
}

SECRET = 'secret'
SECRET_KEY = 'secret'

AUTHENTICATION_BACKENDS = (
    'hierarchical_auth.backends.HierarchicalModelBackend',
)
