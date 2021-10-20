from flask import Flask, request
from flask_restful import Api, Resource
from flask_restful import reqparse
import re

app = Flask(__name__)
api = Api(app)

id_list = ["qlalf9824@naver.com", "gayoung5401@gmail.com", "asdfeg@viewmagine.com"]
id = "qlalf9824@viewmagine.com"
pw = "1q2w3e"
pattern = "(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

class Login(Resource):
    def get(self):
        
        param_dict = request.args.to_dict()

        id = param_dict['id']

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

        
class LoginTest(Resource):
    def get(self):
        try: 
            params = request.get_json(force=True)
            print(params['id'])
            for id in id_list:
                if params['id'] == id:
                    return {
                        'Response' :  
                            {
                            'Message': '이미 존재하는 아이디입니다.', 
                            'Result' : 'Error',
                            'Details': '이미 존재하는 아이디입니다.'
                            }
                    }
                else:
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

    def post(self):
        params = request.get_json(force=True)
        print(params['id'], params['pw'])
        if not re.match(pattern, params['id']):
            print('wrong email')
            return {
                'Response' :  
                    {
                    'Message': '잘못된 이메일 형식입니다.', 
                    'Result' : 'Error',
                    'Details': '잘못된 이메일 형식입니다.'
                    }
            }
        elif params['id'] != id or params['pw'] != pw:
            print('wrong account')
            return {
                'Response' :  
                    {
                    'Message': '아이디 혹은 비밀번호가 틀렸습니다.', 
                    'Result' : 'Error',
                    'Details': '아이디 혹은 비밀번호가 틀렸습니다.'
                    }
            }
        else:
            print('Login!')
            return {
                'Response' :  
                    {
                    'Message': params['id']+'님 로그인 성공!', 
                    'Result' : 'OK',
                    'Details': '로그인 성공!'
                    }
            }


api.add_resource(Login, '/login')
api.add_resource(LoginTest, '/login_test')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001, debug=True)