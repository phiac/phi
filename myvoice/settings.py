import os
from pathlib import Path
from decouple import config
import dj_database_url

from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-y0&g8dvlox@d92kfqfl+y%ad2ct)go+*+$)a7h7c+gsqpq@^bf')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool, default=True)

ALLOWED_HOSTS = ['*']
if not DEBUG:
    ALLOWED_HOSTS = [config('ALLOWED_HOST', default='your_production_hostname.com')]  # Replace with your actual hostname

# Application definition
INSTALLED_APPS = [
    'channels',
    'rest_framework',
    'embed_video',
    "query_search",
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
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Add WhiteNoise 
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myvoice.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
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

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', 'railway'),
        'USER': os.environ.get('DATABASE_USER', 'postgres'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'WaWJKWDltkMPftyvbYEfzchrRuUPGoJj'),
        'HOST': os.environ.get('DATABASE_HOST', 'postgres.railway.internal'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

ASGI_APPLICATION = 'myvoice.asgi.application'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config('https://cloud.redis.io/#/databases', default='redis://127.0.0.1:6379/1'),
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
SESSION_COOKIE_NAME = "sessionid"
SESSION_COOKIE_DOMAIN = 'postgres-production-a225.up.railway.app'

#  Set this in production if needed.
SESSION_COOKIE_SECURE = not DEBUG  # only in production, session_cookie_secure should be True

# Django CORS settings.  These should be environment variables in production.
CORS_ORIGIN_WHITELIST = [config('CORS_ORIGIN', default='http://localhost:3000')]  # and/or whatever your development port is.
CORS_ALLOW_CREDENTIALS = True

SESSION_REDIS = {
    'host': config('REDIS_HOST', default='127.0.0.1'),  # Use decouple for Redis settings
    'port': config('REDIS_PORT', cast=int, default=6379),  # Use decouple
    'db': config('REDIS_DB', cast=int, default=1),  # Use decouple
    'password': config('VtYU3CdPHD80MuyK1SQYGbXMCXD1Uh3R', default=''),  # Set password to None if no password is used
    'prefix': 'session',
    'socket_timeout': 1,
    'retry_on_timeout': False
}

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CSRF_TRUSTED_ORIGINS = [config('CSRF_ORIGIN', default='http://localhost:8000')]

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
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
