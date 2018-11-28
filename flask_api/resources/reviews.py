import json
from flask import jsonify, Blueprint, abort, g, make_response
from flask_restful import (Resource, Api, reqparse, inputs, fields,
                           marshal, marshal_with)

from auth import auth
import models

review_fields = {
    'id': fields.Integer,
    'for_course': fields.String,
    'rating': fields.Integer,
    'comment': fields.String(default=''),
    'created_at': fields.DateTime
}


def review_or_404(review_id):
    try:
        review = models.Review.get(models.Review.id == review_id)
    except models.Review.DoesNotExist:
        abort(404)
    else:
        return review


def add_course(review):
    review.for_course = [url_for('resources.courses.course', id=review.course.id)
                         for review in course.review_set]
    return review


class ReviewList(Resource):
    def __init__(self):
        """
        Input validation using reqparse
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'course',
            type=inputs.positive,
            required=True,
            help='No course provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'rating',
            type=inputs.int_range(1, 5),
            required=True,
            help='No rating provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'comment',
            required=False,
            location=['form', 'json'],
            default=''
        )
        super().__init__()

    def get(self):
        """
        Get all the reviews
        - Import marshal and marshal_with (a decorator)
        - When using marshal, you provide the records and fields that you defined
        - for the resource. 
        """
        return {'reviews': [marshal(add_course(review), review_fields)
                            for review in models.Review.select()
                            ]}

    @marshal_with(review_fields)
    def post(self):
        args = self.reqparse.parse_args()
        # create() sends back the record that was created
        review = models.Review.create(**args)
        return add_course(review)


class Review(Resource):
    @marshal_with(review_fields)
    def get(self, id):
        return add_course(review_or_404(id))

    def put(self, id):
        return jsonify({'course': 1, 'rating': 5})

    def delete(self, id):
        return jsonify({'course': 1, 'rating': 5})


reviews_api = Blueprint('resources.reviews', __name__)
api = Api(reviews_api)
api.add_resource(
    ReviewList,
    '/reviews',
    endpoint='reviews'
)

api.add_resource(
    Review,
    '/reviews/<int:id>',
    endpoint='review'
)
