import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = ')+gku+t961s1*))2*1s1kpq1^xj#=f$642c+tnle(!)7r8=__c'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'backend']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Intro.apps.IntroConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'labs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'labs.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CSRF_TRUSTED_ORIGINS = [
    '127.0.0.1'
]


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# $$$
import sys
import logging
from django.core.management.color import color_style


class DjangoColorsFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super(DjangoColorsFormatter, self).__init__(*args, **kwargs)
        self.style = self.configure_style(color_style())

    def configure_style(self, style):
        style.DEBUG = style.HTTP_NOT_MODIFIED
        style.INFO = style.HTTP_INFO
        style.WARNING = style.HTTP_NOT_FOUND
        style.ERROR = style.ERROR
        style.CRITICAL = style.HTTP_SERVER_ERROR
        return style

    def format(self, record):
        message = logging.Formatter.format(self, record)
        if sys.version_info[0] < 3:
            if isinstance(message, str):
                message = message.encode('utf-8')
        colorizer = getattr(self.style, record.levelname, self.style.HTTP_SUCCESS)
        return colorizer(message)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'longout': {
            'format': '[%(asctime)s][%(levelname)s:%(name)s:%(lineno)d] %(message)s '
                      '\n_________________________________________________________\n'
        },
        'simple': {
            'format': '[%(asctime)s][%(levelname)s:%(name)s:%(lineno)d] %(message)s '
        },
        'colored': {
            '()': DjangoColorsFormatter,
            'format': '[%(asctime)s] - %(levelname)s - %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        }
    },
    'handlers': {
        'file_db': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug-db.log',
            'formatter': 'longout',
        },
        'file_requests': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug-requests.log',
            'formatter': 'simple',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'colored',
        },
    },
    'loggers': {
        'django.db': {
            'handlers': ['file_db', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django': {
            'handlers': ['file_requests', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)