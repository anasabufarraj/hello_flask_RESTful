#!./venv/bin/python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj
# ------------------------------------------------------------------------------
""" Learning Flask-RESTful extension."""

from flask import Flask, request
from flask_restful import Resource, Api

APP = Flask(__name__)
APP.secret_key = 'secret_password'
API = Api(APP)

ITEMS = [{'name': 'book', 'price': 17.99}]


class ItemList(Resource):
    @staticmethod
    def get():
        """Returns a JSON of all items with 200 (OK) response."""
        return {'items': ITEMS}, 200


class Item(Resource):
    @staticmethod
    def get(name):
        """Returns item by name if found.
        Iterate in lazy way over a filter object with next, return an item if found,
        or return None by default.
        :param name: string
        :returns: {"item": <name>} or {"item": null}, 200 if True, otherwise 404.
        """
        item = next(filter(lambda x: x['name'] == name, ITEMS), None)
        return {'item': item}, 200 if item else 404

    @staticmethod
    def post(name):
        """Create and append new item, returns a message if exist and 400 (BAD REQUEST).
        :param name: strong
        :returns: item and 201 (CREATED)
        """
        item = next(filter(lambda x: x['name'] == name, ITEMS), None)
        if item:
            return {'message': f'item with name {name} already exists!'}, 400

        request_data = request.get_json()  # Data posts in the request bod
        item = {'name': name, 'price': request_data['price']}
        ITEMS.append(item)

        return item, 201


API.add_resource(ItemList, '/item')
API.add_resource(Item, '/item/<string:name>')
