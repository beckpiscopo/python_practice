from flask import jsonify, Blueprint, abort
from flask_restful import (Resource, Api, reqparse,
                           inputs, fields, marshal,
                           marshal_with)

import models

# This dictionary discribes the fields included when this API gives a resource.
# Import fields from flask_restful
course_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'url': fields.String,
    'reviews': fields.List(fields.String)
}


def add_reviews(course):
    course.reviews = [url_for('resources.reviews.review', id=review.id)
                      for review in course.review_set]
    return course


def course_or_404(course_id):
    # get a single course or throws 404 error
    try:
        course = models.Course.get(models.Course.id == course_id)
    except models.Course.DoesNotExist:
        abort(404, message="Course {} does not exist".format(course_id))
    else:
        return course


class CourseList(Resource):
    def __init__(self):
        """
        Input validation using reqparse
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title',
            required=True,
            help='No course title provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'url',
            required=True,
            help='No course url provided',
            location=['form', 'json'],
            type=inputs.url
        )
        super().__init__()

    def get(self):
        """
        Get all the courses
        - Import marshal and marshal_with (a decorator)
        - When using marshal, you provide the records and fields that you defined
        - for the resource. 
        """
        courses = [marshal(course, course_fields)
                   for course in models.Course.select()]
        return {'courses': courses}

    def post(self):
        args = self.reqparse.parse_args()
        models.Course.create(**args)
        return jsonify({'courses': [{'title': 'Python Basics'}]})


class Course(Resource):
    """ 
    Import marshal_with (decorator)
    marshal_with is useful when only returning a single item
    """
    @marshal_with(course_fields)
    def get(self, id):
        return add_reviews(course_or_404(id))

    def put(self, id):
        return jsonify({'title': 'Python Basics'})

    def delete(self, id):
        return jsonify({'title': 'Python Basics'})


courses_api = Blueprint('resources.courses', __name__)
api = Api(courses_api)
api.add_resource(
    CourseList,
    '/api/v1/courses',
    endpoint='courses'
)
api.add_resource(
    Course,
    '/api/v1/courses/<int:id>',
    endpoint='course'
)
