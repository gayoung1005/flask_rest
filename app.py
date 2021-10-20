from flask import Flask, request
from flask_restful import Api, Resource
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)


class Login(Resource):
    def get(self):
        
        param_dict = request.args.to_dict()

        id = param_dict['id']
        
        id_list = ["qlalf9824@naver.com", "gayoung5401@gmail.com", "asdfeg@viewmagine.com"]

        if(id in id_list):
            return {
                'Response' : {
                    'message' : 'This is a duplicate ID.'
                }
            }
        else:
            return {
                'Response' : {
                    'message' : 'This is the ID that you can use.'
                }
            }

        



api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)