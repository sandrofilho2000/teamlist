"""
Django settings for setup project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from .jazzmin_settings import JAZZMIN_SETTINGS

from dj_database_url import parse as db_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

from dotenv import load_dotenv
import os

load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG")
if DEBUG in ["true", "1", True, "True"]:
    DEBUG = True
else:
    DEBUG = False
    
    
allowed_hosts_str = os.environ.get("ALLOWED_HOSTS")

# Split the string into a list using comma as delimiter
ALLOWED_HOSTS = allowed_hosts_str.split(',')

MY_APPS = [
    "teams.apps.TeamsConfig",
    "leagues.apps.LeaguesConfig",
    "league_team.apps.LeagueTeamConfig",
    "countries.apps.CountriesConfig",
    "search_items.apps.SearchItemsConfig",
    "players.apps.PlayersConfig",
    "stadiums.apps.StadiumsConfig",
    "trophies.apps.TrophiesConfig",
    "team_trophy.apps.TeamTrophyConfig"
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "jazzmin",
    "tailwind",
    "django_browser_reload",
    "theme", 
    "colorfield",
    "storages",
    "fontawesomefree"
]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

INSTALLED_APPS = MY_APPS + THIRD_PARTY_APPS + DJANGO_APPS

TAILWIND_APP_NAME = 'theme'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "setup.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),  # Add this line
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "teams.context_processors.team_list_processor",
            ],
        },
    },
]

WSGI_APPLICATION = "setup.wsgi.application"

JAZZMIN_SETTINGS = JAZZMIN_SETTINGS

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# Using os.environ.get for DATABASES variable
DATABASE_URL = os.environ.get("DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}")

# Assuming db_url is a custom function to parse database URLs
DATABASES = {
    "default": db_url(DATABASE_URL)
}

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

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


INTERNAL_IPS = [
    "127.0.0.1"
]

if os.environ.get('DEPLOYMENT_ENV') == 'remote':
    NPM_BIN_PATH = 'npm'  

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME = "teamlist-bkt-1"
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_FILE_OVERWRITE = False

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
}


STATIC_URL = "/theme/static/"
STATICFILES_DIRS = [BASE_DIR / "/theme/static"]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    