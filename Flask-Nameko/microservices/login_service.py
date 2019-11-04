from nameko.rpc import rpc
import pymongo,json
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.microservice_db
user_service = db.user_service

class LoginService:

    name='loginService'

    @rpc
    def login_service(self,request_data):

        response={
            "success":False,
            "message":"something went wrong",
            "data":[]
        }

        # username=request_data['username']
        password=request_data['password']
        email_id=request_data['email_id']

        print(email_id,password,'------->login_service')

        user_obj=user_service.find_one({
            "email_id":email_id
        })

        print(user_obj,"user_obj")
        if user_obj is not None:
            response['success'] = True
            response['message'] = '{} successfully logged in'.format(user_obj['username'])

        return response
