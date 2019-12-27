"""Base settings to build other settings files upon."""

import environ

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('projectjose')

env = environ.Env()

# Base
DEBUG = env.bool('DJANGO_DEBUG', False)

# Language and timezone
TIME_ZONE = 'America/Mexico_City'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# DATABASES
DATABASES = {
    'default': env.db('DATABASE_URL'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# URLs
ROOT_URLCONF = 'config.urls'

# WSGI
WSGI_APPLICATION = 'config.wsgi.application'

# Apps
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

THIRD_PARTY_APPS = [
    'crispy_forms',

]
LOCAL_APPS = [
    'projectjose.dashboard',
    'projectjose.social',
    'projectjose.services',
    'projectjose.core',
    'projectjose.posts',
    'projectjose.staff',

]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Passwords
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]
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

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Static files
STATIC_ROOT = str(ROOT_DIR('staticfiles'))
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Media
MEDIA_ROOT = str(APPS_DIR('media'))
MEDIA_URL = '/media/'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'projectjose.social.processors.ctx_dict',
            ],
        },
    },
]

LOGIN_REDIRECT_URL = 'dashboard:staff-list'

# Django Crispy Forms ----------------------------------------------------------
CRISPY_ALLOWED_TEMPLATE_PACKS = (
    'uni_form',
    'bootstrap',
    'bootstrap3',
    'bootstrap4',
    #'concept',
)

CRISPY_TEMPLATE_PACK = 'bootstrap4'

VERSATILEIMAGEFIELD_SETTINGS = {
    'cache_length': 2592000,
    'cache_name': 'versatileimagefield_cache',
    'jpeg_resize_quality': 70,
    'sized_directory_name': '__sized__',
    'filtered_directory_name': '__filtered__',
    'placeholder_directory_name': '__placeholder__',
    'create_images_on_demand': True,
    'image_key_post_processor': None,
    'progressive_jpeg': False
}

VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'post': [
        ('gallery', 'thumbnail__540x540'),
        ('gallery_2x', 'thumbnail__1080x1080'),
        ('small', 'thumbnail__60x60'),
        ('small_2x', 'thumbnail__120x120'),
        ('list', 'thumbnail__255x255'),
        ('list_2x', 'thumbnail__510x510'),
        ('tiny', 'thumbnail__10x10'),
        ('tiny_2x', 'thumbnail__20x20'),
    ],
}


# Security
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

from decouple import config

EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'lfsoverop@unac.edu.pe'
EMAIL_HOST_PASSWORD = config('USER_EMAIL_PASSWORD') #ENV
EMAIL_USE_TLS = True

# Email
# EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# Admin
ADMIN_URL = 'admin/'
# ADMINS = [
#     ("""Pablo Trinidad""", 'pablotrinidad@ciencias.unam.mx'),
# ]
# MANAGERS = ADMINS




# Celery
INSTALLED_APPS += ['projectjose.taskapp.celery.CeleryAppConfig']
if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = env('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYD_TASK_TIME_LIMIT = 5 * 60
CELERYD_TASK_SOFT_TIME_LIMIT = 60
