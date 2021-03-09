import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/bloggers'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,

}