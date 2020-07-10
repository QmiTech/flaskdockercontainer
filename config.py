import os

class Config:
    SECRET_KEY = 'qmi'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

class ProdConfig (Config):
    pass

class DevConfig (Config):

    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig
}