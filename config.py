import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    QUOTE_API_BASE ='http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/bloggers'

config_options = {
'development':DevConfig,
'production':ProdConfig,
}