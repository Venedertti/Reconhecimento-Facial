from flask import Flask
from flask_restx import Api, Resource
import json

from src.server.instance import server
import src.server.db as db

app, api = server.app, server.api

@api.route('/report')
class Report(Resource):
    def get(self, ):
        return "teste"

    def post(self, id):
        response = api.payload 
        return response, 200
