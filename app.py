from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

id_list = ['test@test.com', 'dltndud100@gmail.com', 'sooyoung.lee@gmail.com']
password = "12345"

class Login(Resource):
    def get(self):
        params = request.get_json(force=True)
        print(params)

class LoginTest(Resource):
    def get(self):
        try: 
            params = request.get_json(force=True)
            print(params['id'])
            for id in id_list:
                if params['id'] == id:
                    print('fail')
                    return {
                        'Response' :  
                            {
                            'Message': '이미 존재하는 아이디입니다.', 
                            'Result' : 'Error',
                            'Details': '이미 존재하는 아이디입니다.'
                            }
                    }
                else:
                    print('success')
                    return {
                        'Response' :  
                            {
                            'Message': '사용할 수 있는 아이디입니다.', 
                            'Result' : 'OK',
                            'Details': '사용할 수 있는 아이디입니다.'
                            }
                    }

        except Exception as e:
            return{
                'Response' :
                    {
                        'Message' : 'Error in Processing',
                        'Result': 'Error',
                        'Details': str(e)
                    }
            }


api.add_resource(Login, '/login')
api.add_resource(LoginTest, '/login_test')

if __name__ == '__main__':
    app.run(debug=True)