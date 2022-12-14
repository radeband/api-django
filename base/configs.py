from decouple import config, Csv


class GeneralConfig:
    DEBUG = True
    TZ = config('TZ')
    # ALLOWED_HOSTS = config('ALLOWED_HOSTS')
    ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
    CSRF_TRUSTED_ORIGINS = ['http://api.radeband.ir', 'https://api.radeband.ir']

# database configs
class DatabaseConfig:
    DB_NAME = config('DB_NAME')
    DB_USER = config('DB_USER')
    DB_PASS = config('DB_PASS')
    DB_HOST = config('DB_HOST')
    DB_PORT = config('DB_PORT')


class GoogleOAuthConfig:
    GOOGLE_OAUTH_CLIENT_ID = config('GOOGLE_OAUTH_CLIENT_ID')
    GOOGLE_OAUTH_SECRET = config('GOOGLE_OAUTH_SECRET')
    GOOGLE_OAUTH_KEY = config('GOOGLE_OAUTH_KEY')