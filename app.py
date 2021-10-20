from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

class Login(Resource):
    def get(self):
        params = request.get_json(force=True)
        print(parmas)



api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(debug=True)