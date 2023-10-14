from decouple import config

# DEBUG = False
ALLOWED_HOSTS = ['*']

SECRET_KEY = 'bws0+*2eh!0#b&4#mx+l!1)#!-p3-x&^vv$m2xj7-0v$bi3+qn'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('NAME'),
        'HOST': config('HOST'),
        'PORT': config('PORT'),
        'USER': config('DB_USER'),
        'PASSWORD': config('PASSWORD')
    }
}
