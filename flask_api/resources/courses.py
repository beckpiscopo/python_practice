from flask import jsonify, Blueprint, abort
from flask_restful import (Resource, Api, reqparse,
                           inputs, fields, marshal,
                           marshal_with, url_for)

from auth import auth
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

    @marshal_with(course_fields)
    def post(self):
        args = self.reqparse.parse_args()
        course = models.Course.create(**args)
        return (add_reviews(course), 201, {
                'Location': url_for('resources.courses.course', id=course.id)}
                )


class Course(Resource):
    """ 
    Import marshal_with (decorator)
    marshal_with is useful when only returning a single item
    """

    def __init__(self):
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

    @marshal_with(course_fields)
    def get(self, id):
        return add_reviews(course_or_404(id))

    @marshal_with(course_fields)
    def put(self, id):
        args = self.reqparse.parse_args()
        query = models.Course.update(**args).where(models.Course.id == id)
        query.execute()
        return (add_reviews(models.Course.get(models.Course.id == id)), 200,
                {
                    # Location header to indicate where the record is
                    'Location': url_for('resources.courses.course', id=id)
        })

    @marshal_with(course_fields)
    def delete(self, id):
        query = models.Course.delete().where(models.Course.id == id)
        query.execute()
        # return an empty body and 204 message
        return ('', 204, {'Location': url_for('resources.courses.courses')})


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
