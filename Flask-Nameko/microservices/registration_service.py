from nameko.rpc import rpc
import pymongo,json
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.microservice_db
user_service = db.user_service


class RegistrationService:

    name = 'registrationService'

    @rpc
    def registration_service(self, request_data):


        response = {
            "success": False,
            "message": "something went wrong",
            "data": []
        }

        username = request_data['username']
        password = request_data['password']
        email_id = request_data['email_id']

        print(username, password, '------->registration_service')

        inserted_id = user_service.insert({
            "username": username,
            "password": password,
            "email_id": email_id
        })

        user_obj = user_service.find_one({
            "email_id": email_id
        })
        print(inserted_id, "inserted_id")

        response['success'] = True
        response['message'] = '{} are successfully Registered'.format(user_obj['username'])

        return response
