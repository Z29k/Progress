DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "progress_dev",
        "USER": "localdev",
        "PASSWORD": "testing",
    }
}

ALLOWED_HOSTS = ('127.0.0.1',)