"""
Django settings for dataproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

#for celery use
from __future__ import absolute_import
from datetime import timedelta

#celery settings

CELERY_TASK_RESULT_EXPIRES=3600,
CELERYBEAT_SCHEDULE = {
    'get_travel_time-every-30-seconds': {
        'task': 'traffic.tasks.get_travel_time_tmc',
        'schedule': timedelta(seconds=30),
    },
}

#broker url for celery use
BROKER_URL = 'django://'

#periodical schedules


#Django settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#import kombu
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# for nginx to server static files
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# Tell the server where to find geos library
# GEOS_LIBRARY_PATH = '/usr/local/lib/libgeos_c.so'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*d7jnjdq6ng4w_u0$ilw5lyd-s&b9y@kb%!cg=jbx1f7hw^r3q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['mac.heinz.cmu.edu']

ADMINS = (('hzn', 'benhzn07@gmail.com'))

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'traffic',
    'django_extensions',
    # 'kombu.transport.django',
    # 'djcelery',
    'django.contrib.gis',
    # 'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'project_middleware.authen_middleware.LoginRequiredMiddleware',
)

ROOT_URLCONF = 'dataproject.urls'

WSGI_APPLICATION = 'dataproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {


    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dataproject',
	    'USER': 'root',
	    'PASSWORD': 'dataproject',
        # 'HOST': '52.1.172.127',
        # 'HOST': 'LOCALHOST',
        'HOST': '128.2.84.231',
        'PORT': '3306',

    },
   'psql': {
       'ENGINE': 'django.contrib.gis.db.backends.postgis',
       'NAME': 'dataprojectpsql',
       'USER': 'postgres',
       'PASSWORD': 'dataproject',
       # 'HOST': '128.2.81.222',
       'HOST': 'LOCALHOST',
       'PORT': '5432',
   },
}

# Router is used to specify which database a model belongs to
DATABASE_ROUTERS = ['dataproject.router.Router']

# New in Django 1.8
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(__file__),'traffic.views'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'America/New_York'
#
# USE_I18N = True
#
# USE_L10N = True

# No need to use timzone; always use local
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# for login use
LOGIN_URL = '/traffic/login/'

LOGIN_EXEMPT_URLS = (
    'traffic/register/',
    'admin/'
)

# set sessions to expire when user close the browser, this is a global way
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Email setting, use our gmail to send emails
EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'mdap2205@gmail.com'

EMAIL_HOST_PASSWORD = 'dataproject'

EMAIL_PORT = 587

LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'handlers': {
        'console': {
            # logging handler that outputs log messages to terminal
            'class': 'logging.StreamHandler',
            'level': 'DEBUG', # message level to be written to console
        },
    },
    'loggers': {
        '': {
            # this sets root level logger to log debug and higher level
            # logs to console. All other loggers inherit settings from
            # root level logger.
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False, # this tells logger to send logging message
                                # to its parent (will send if set to True)
        },
        'django.db': {
            'level': 'WARNING'
            # django also has database level logging
        },
    },
}

INTERNAL_IPS = [
        '127.0.0.1',
        ]
