from create_app import app
from flask_mongoengine import MongoEngine

app.config['MONGODB_SETTINGS'] = {
    'db': 'productDB',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)
