"""
Django settings for watchmate project.

Generated by 'django-admin startproject' using Django 3.2a1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from pathlib import Path
from environ import Env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$*(4s7evu!!i0=3o#g1gqyf^60vqpveyw)e=+y%k(k51qe*+z('

# SECURITY WARNING: don't run with debug turned on in production!
#Env.read_env()

#environ.Env.read_env()
#env.read_env()
env = Env() 
env.read_env()

DEBUG = env.bool("API_DEBUG", default=True)

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'book_app',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'djmoney',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

#CORS_ALLOWED_ORIGINS = [
#    "http://localhost:4200",
#]

#CORS_ALLOW_METHODS = [
#    'DELETE',
#    'GET',
#    'OPTIONS',
#    'PATCH',
#    'POST',
#    'PUT',
#]

#ALLOWED_HOSTS=['*']
CORS_ORIGIN_ALLOW_ALL = True
SECURE_CROSS_ORIGIN_OPENER_POLICY = None
#CSRF_TRUSTED_ORIGINS=["*"]

ROOT_URLCONF = 'watchmate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'watchmate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        # MySQL engine. Powered by the mysqlclient module.
        'ENGINE': 'mysql.connector.django',
        'NAME': 'books',
        'USER': 'root',
        #'USER': 'admin',
        'PASSWORD': 'Password$12',
        'HOST': 'localhost',
        #'HOST': 'books.c5ktsotgokwo.us-east-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


if DEBUG:
    DEFAULT_RENDERER_CLASSES = (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    )
else:
    DEFAULT_RENDERER_CLASSES = (
        "rest_framework.renderers.JSONRenderer",
    )

REST_FRAMEWORK = {

    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],

    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle'
    # ],

    #'DEFAULT_THROTTLE_RATES': {
    #    'anon': '100/day',
    #    'user': '100/day',
    #    'review-create': '2/day',
    #    'review-list': '100/day',
    #    'review-detail': '100/day',
    #},

    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 5,

    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES,
}

# SIMPLE_JWT = {
#     'ROTATE_REFRESH_TOKENS' : True,
# }
