"""
Django settings for gigzera project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8veuiojh=5^rhyx&2%d+3=mu(9+bskvpdiupx#c+h6f)7w#82%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','localhost', '13.235.71.115', '13.127.0.178']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'non_register',
    'freelancer',
    'client',
    'db_schemas',
    'myadmin',

    # custom
    'storages',
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

ROOT_URLCONF = 'gigzera.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'myadmin.context_processors.user_role_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'gigzera.wsgi.application'
CSRF_COOKIE_HTTPONLY = False


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

# Add the path to your static directory
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Directory to collect static files during deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



import boto3

def get_ssm_parameter(param_name, default=None):
    try:
        ssm = boto3.client('ssm', region_name="ap-south-1")
        response = ssm.get_parameter(Name=f"/myapp/{param_name}", WithDecryption=True)
        return response['Parameter']['Value']
    except Exception as e:
        print(f"Warning: {e}")
        return default


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sampleDB',
        'USER': 'postgres',
        'PASSWORD': 'mysuperpass',
        'HOST': 'demo-postgre.ctigc0i0wbqn.ap-south-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'gigzera',
#         'USER': 'gigzera',
#         'PASSWORD': 'GigzeraPass',
#         'HOST': 'gigzera-rds.cbouq000srap.ap-south-1.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }




# Load environment variables from .env
load_dotenv()

# Use AWS S3 in production, local storage in development
# USE_S3 = os.getenv("USE_S3", "False") == "True"
USE_S3 = True

if USE_S3:
    print("Using AWS S3 storage-->")
    AWS_DEFAULT_ACL = "public-read"
    
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID") or get_ssm_parameter("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY") or get_ssm_parameter("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME") or get_ssm_parameter("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = "ap-south-1"

    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None
    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=86400",
    }

    AWS_LOCATION = "media"  # Remove "media" if it’s causing duplication in the path
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    # AWS_LOCATION = "media"
    # MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"
else:
    print("Using local storage")
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# AWS completed
# AWS_LOCATION = ""

