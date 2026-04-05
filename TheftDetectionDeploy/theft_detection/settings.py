# theft_detection/settings.py

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = "django-insecure-7h#@8y$z!v5r2l2d&*+x!k4w9q0s1p3m"
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',  # MUST be here
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # your app
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # must be here
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # must be here
    'django.contrib.messages.middleware.MessageMiddleware',    # must be here
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'theft_detection.urls'

# theft_detection/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # you can leave empty if using app templates
        'APP_DIRS': True,  # must be True to find templates inside apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'theft_detection.wsgi.application'

# DATABASES is NOT included — Django will run without migrations
# DATABASES = {}   # optional, leave out completely

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (for uploading videos)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'