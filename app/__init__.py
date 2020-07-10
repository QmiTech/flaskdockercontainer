from flask import Flask
from config import config_options
from flask_uploads import UploadSet, configure_uploads, IMAGES
import boto3
import os

ACCESS_ID = ''
SECRET_K = ''

photos = UploadSet('photos',IMAGES)
session = boto3.session.Session()

#configuring a client
client = session.client('s3',
                        region_name='nyc3',
                        endpoint_url='https://nyc3.digitaloceanspaces.com',
                        aws_access_key_id=os.getenv('ACCESS_ID'),
                        aws_secret_access_key=os.getenv('SECRET_K'))

def create_app(config_name):
    app = Flask(__name__)

    #creating the app configuration
    app.config.from_object(config_options[config_name])

    #configure uploadset
    configure_uploads(app,photos)

    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config

    return app