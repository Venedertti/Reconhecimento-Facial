from flask import Flask, jsonify
from flask_restx import Api, Resource
from src.Controller.ReportHotController import *

app=Flask(__name__)
api=Api(app)

api.route("/")
class App():
    def get():
        return "Hello Word!"

if __name__ == '__main__':
    app.run(debug=True)