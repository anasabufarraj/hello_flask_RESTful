#!/usr/bin/env python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------
""" Learning Flask-RESTful extension"""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Student(Resource):
    """Define Student class."""
    @staticmethod
    def get(name):
        """Returns name.

        :param name: string
        :return: a dictionary of student name
        """
        return {'student': name}


api.add_resource(Student, '/student/<string:name>')

if __name__ == '__main__':
    app.run()
