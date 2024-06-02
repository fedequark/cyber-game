import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    USE_DATABASE = os.environ.get('USE_DATABASE', 'false').lower() in ['true', '1', 't']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///development.db'
    USE_DATABASE = False  # Cambiar a True para usar el workflow basado en la base de datos

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///production.db'
    USE_DATABASE = False  # Cambiar a True para usar el workflow basado en la base de datos

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
