from flask import Flask, request
from flask_restful import Api, Resource
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

id_list = ["qlalf9824@naver.com", "gayoung5401@gmail.com", "asdfeg@viewmagine.com"]
id = "qlalf9824@viewmagine.com"
pw = "1q2w3e"

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
    app.run(host="0.0.0.0",port=5000, debug=True)