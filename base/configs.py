import environ
env = environ.Env()
environ.Env.read_env()


class GeneralConfig:
    TZ = env('TZ')
    ALLOWED_HOSTS = env('ALLOWED_HOSTS')


# database configs
class DatabaseConfig:
    DB_NAME = env('DB_NAME')
    DB_USER = env('DB_USER')
    DB_PASS = env('DB_PASS')
    DB_HOST = env('DB_HOST')
    DB_PORT = env('DB_PORT')


class GoogleOAuthConfig:
    GOOGLE_OAUTH_CLIENT_ID = env('GOOGLE_OAUTH_CLIENT_ID')
    GOOGLE_OAUTH_SECRET = env('GOOGLE_OAUTH_SECRET')
    GOOGLE_OAUTH_KEY = env('GOOGLE_OAUTH_KEY')