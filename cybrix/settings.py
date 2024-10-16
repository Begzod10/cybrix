"""
Django settings for cybrix project.

Generated by 'django-admin startproject' using Django 4.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1t37!sv2$5c(vhn0mrkl&as4^*jg_#mt%9e#(mv6ubapmi&qq='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'client_requests'
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

ROOT_URLCONF = 'cybrix.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'cybrix.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
SWAGGER_SETTINGS = {"SECURITY_DEFINITIONS": {"Bearer": {"type": "apiKey", "name": "Authorization", "in": "header", }},
                    "USE_SESSION_AUTH": True}
DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql', 'NAME': 'cybrix', 'USER': 'postgres',
                         'PASSWORD': '123', 'HOST': 'localhost', 'PORT': '5432'}}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
JAZZMIN_SETTINGS = {
    "site_title": "Gennis Admin Site",
    "site_header": "Admin Panel",
    "site_brand": "Admin Panel",
    "welcome_sign": "Welcome to Your Admin Panel",
    "user_avatar": None,

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
        {"app": "system"},
    ],

    "usermenu_links": [
        {"model": "auth.user"}
    ],

    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": [
        "auth", "books", "students", "teachers", "payments", "flows",
        "tasks", "attendances", "time_table", "lesson_plan"
    ],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "books.Book": "fas fa-book",
        "students.Student": "fas fa-user-graduate",
        "teachers.Teacher": "fas fa-chalkboard-teacher",
        "payments.PaymentTypes": "fas fa-money-check-alt",
        "flows.Flow": "fas fa-stream",
        "tasks.Task": "fas fa-tasks",
        "attendances.AttendancePerMonth": "fas fa-calendar-check",
        "time_table.GroupTimeTable": "fas fa-calendar-alt",
        "lesson_plan.LessonPlan": "fas fa-book-open",
        "branch.Branch": "fas fa-building",
        "overhead.Overhead": "fas fa-file-invoice-dollar",
    },

    "default_icon_children": "fas fa-circle",

    "related_modal_active": True,  # Enable modals for related fields
    "custom_css": "css/custom_admin.css",
    "custom_js": "js/custom_admin.js",  # Include your custom JS here
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "books.book": "vertical_tabs",
    },

    "theme": "cerulean",
    "dark_mode_theme": None,

    "logging": {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "WARNING",
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": True,
            },
        },
    },

    # "custom_links": {
    #     "auth": [{
    #         "name": "Make Messages",
    #         "url": "make_messages",
    #         "icon": "fas fa-comments",
    #         "permissions": ["auth.view_user"]
    #     }]
    # },

    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "navbar_fixed": True,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "layout_boxed": False,
    "sidebar_collapsed": False,
    "sidebar_dark": True,

    "language_chooser": False,
}
