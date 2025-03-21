import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-y0&g8dvlox@d92kfqfl+y%ad2ct)go+*+$)a7h7c+gsqpq@^bf"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = 'phi-production.up.railway.app',



# Application definition
INSTALLED_APPS = [
    'channels',
    'rest_framework',
    'embed_video',
    "query_search",
    "messaging",
    "ml",
    "social_app",
    "xvoice",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myvoice.urls"


# ✅ Correct: TEMPLATES is a list of dicts
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Templates outside apps
        'APP_DIRS': True,  # Allow Django to search app-specific templates
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

            ],
        },
    },
]


WSGI_APPLICATION = "myvoice.wsgi.application"
path = '/home/videofeed/myvoice/myvoice/'
os.environ['DJANGO_SETTINGS_MODULE'] = 'myvoice.settings'

# Databasehttps://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'railway'),
        'USER': os.environ.get('DATABASE_USER', 'postgres'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'spuiRAjWJIIABraVywDjSixizLTeStVf'),
        'HOST': os.environ.get('DATABASE_HOST', 'postgres.railway.internal'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# AUTH_USER_MODEL = 'social_app.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# settings.py

# URL prefix for serving static files


# Directory where collectstatic will gather all static files for production

STATIC_URL = '/static/'


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Where collectstatic copies files

# Additional directories to search for static files during development

LOGIN_URL = '/accounts/login/'
# settings.py
LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'
#
# myproject/settings.py
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_ACCESS_KEY_ID = 'your-access-key'
# AWS_SECRET_ACCESS_KEY = 'your-secret-key'
# AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'

ASGI_APPLICATION = 'myvoice.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# settings.py
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
SESSION_COOKIE_NAME = "sessionid"
SESSION_COOKIE_DOMAIN = ".pythonanywhere.com/user/videofeed/myvoice/"  # Corrected domain
SESSION_COOKIE_SECURE = True # Only send the cookie over HTTPS

# Django CORS settings
CORS_ORIGIN_WHITELIST = ['https://node-app.www.pythonanywhere.com/user/videofeed/myvoice/'],
CORS_ALLOW_CREDENTIALS = True

# Advanced Redis configuration
SESSION_REDIS = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 1,
    'password':'VtYU3CdPHD80MuyK1SQYGbXMCXD1Uh3R' ,  # Set password to None if no password is used
    'prefix': 'session',
    'socket_timeout': 1,
    'retry_on_timeout': False

}# Security settings
SECURE_BROWSER_XSS_FILTER = True  # Enable browser XSS filtering
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent content type sniffing
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'  # Referrer policy for security

# For reverse proxies (if applicable)
USE_X_FORWARDED_HOST = True  # Trust proxy headers for request host
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # Indicate SSL via proxy headers

