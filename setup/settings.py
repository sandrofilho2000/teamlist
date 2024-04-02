# Django settings for setup project.

# Import necessary modules
import os
from pathlib import Path
from .jazzmin_settings import JAZZMIN_SETTINGS
from dj_database_url import parse as db_url
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Get secret key from environment variables
SECRET_KEY = os.environ.get("SECRET_KEY")

# DEBUG mode configuration
DEBUG = os.environ.get("DEBUG")
if DEBUG in ["true", "1", True, "True"]:
    DEBUG = True
else:
    DEBUG = False

# Get allowed hosts from environment variables
allowed_hosts_str = os.environ.get("ALLOWED_HOSTS")
ALLOWED_HOSTS = allowed_hosts_str.split(',')

# Get CSRF trusted origins from environment variables
csrf_trusted_origins_str = os.environ.get("CSRF_TRUSTED_ORIGINS")
CSRF_TRUSTED_ORIGINS = csrf_trusted_origins_str.split(',')

# Define installed apps
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

# Define TAILWIND_APP_NAME
TAILWIND_APP_NAME = 'theme'

# Define middleware
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

# Define root URL configuration
ROOT_URLCONF = "setup.urls"

# Define templates configuration
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

# Define WSGI application
WSGI_APPLICATION = "setup.wsgi.application"

# Load JAZZMIN_SETTINGS
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS

# Database configuration
DATABASE_URL = os.environ.get("DATABASE_URL", default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
DATABASES = {
    "default": db_url(DATABASE_URL)
}

# Define authentication password validators
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

# Internationalization settings
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Define internal IPs
INTERNAL_IPS = ["127.0.0.1"]

# Define NPM_BIN_PATH based on deployment environment
if os.environ.get('DEPLOYMENT_ENV') == 'remote':
    NPM_BIN_PATH = 'npm'  
else:
    NPM_BIN_PATH = 'C:/Program Files/nodejs/npm.cmd'

# AWS S3 settings
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "teamlist-bkt-1"
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_FILE_OVERWRITE = False

# Define storage settings
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
}

# Static and media files settings
STATIC_URL = "/theme/static/"
STATICFILES_DIRS = [BASE_DIR / "/theme/static"]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
