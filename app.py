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
        try:
            param_dict = request.args.to_dict()

            reid = param_dict['id']

            if(reid in id_list):
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
        except Exception as e:
            return {
                'Response' : {
                    'Message' : 'Error in Processing',
                    'Result': 'Error',
                    'Details': str(e)
                }
            }

    def post(self):
        try:
            params = request.get_json(force=True)

            reid = params['id']
            repw = params['pw']
            
            pattern = "^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

            if re.match(pattern, reid)== None:
                return {
                    'Response' : {
                        'message' : 'Wrong email'
                    }
                }
            elif(reid == id and repw == pw):
                return {
                    'Response' : {
                        'message' : 'Login!'
                    }
                }
            else:
                return {
                    'Response' : {
                        'message' : 'Wrong ID or Password'
                    }
                }
        except Exception as e:
            return {
                'Response' : {
                    'Message' : 'Error in Processing',
                    'Result': 'Error',
                    'Details': str(e)
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
                            'Message': '?????? ???????????? ??????????????????.', 
                            'Result' : 'Error',
                            'Details': '?????? ???????????? ??????????????????.'
                            }
                    }
                else:
                    return {
                        'Response' :  
                            {
                            'Message': '????????? ??? ?????? ??????????????????.', 
                            'Result' : 'OK',
                            'Details': '????????? ??? ?????? ??????????????????.'
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
                    'Message': '????????? ????????? ???????????????.', 
                    'Result' : 'Error',
                    'Details': '????????? ????????? ???????????????.'
                    }
            }
        elif params['id'] != id or params['pw'] != pw:
            print('wrong account')
            return {
                'Response' :  
                    {
                    'Message': '????????? ?????? ??????????????? ???????????????.', 
                    'Result' : 'Error',
                    'Details': '????????? ?????? ??????????????? ???????????????.'
                    }
            }
        else:
            print('Login!')
            return {
                'Response' :  
                    {
                    'Message': params['id']+'??? ????????? ??????!', 
                    'Result' : 'OK',
                    'Details': '????????? ??????!'
                    }
            }


api.add_resource(Login, '/login')
api.add_resource(LoginTest, '/login_test')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001, debug=True)