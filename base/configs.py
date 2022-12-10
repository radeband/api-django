import environ
env = environ.Env()
environ.Env.read_env()

class GeneralConfig():
    TZ = env('TZ')

# database configs
class DatabaseConfig():
    DB_NAME = env('DB_NAME')
    DB_USER = env('DB_USER')
    DB_PASS = env('DB_PASS')
    DB_HOST = env('DB_HOST')
    DB_PORT = env('DB_PORT')