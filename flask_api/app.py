
from flask import Flask
from flask_restful import Resource, Api

import models
from resources.courses import courses_api
from resources.reviews import reviews_api

PORT = 8080
app = Flask(__name__)
api = Api(app)
app.register_blueprint(courses_api)
app.register_blueprint(reviews_api, url_prefix='/api/v1')


if __name__ == '__main__':
    models.initialize()
    app.run(debug=True, port=PORT)
