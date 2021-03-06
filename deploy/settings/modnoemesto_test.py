# -*- coding: utf-8 -*-

DEBUG = TEMPLATE_DEBUG = 1

ADMINS = (
    ('tech', 'tech@web-mark.ru'),
    ('dgk', 'dgk@web-mark.ru'),
    ('elias', 'elias@web-mark.ru'),
    ('eugene', 'eugene@web-mark.ru'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:', #rel('local.db'),
    },

    'billing': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'billing_test',
        'USER': 'billing_test',
        'PASSWORD': 'akonEsdfsdfd2',
        'HOST': '10.10.10.7',
    },
}


#CELERY_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'apps.async_email.backends.CeleryEmailBackend'

VIDEO_PROXY_SERVER_URL = 'rtmp://109.234.158.4/cam3'

TASKS_ENABLED = dict(
        AVATAR_RESIZE=1,
        LIBRARY_VIDEO_RESIZE=1,
)

