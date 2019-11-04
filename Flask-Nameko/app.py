

from flask import Flask,request,jsonify

app = Flask(__name__)
# from __init__ import app, rpc
from nameko.standalone.rpc import ClusterRpcProxy
config = {
    "AMQP_URI":"pyamqp://guest:guest@localhost"
}

# @app.route('/',methods=['GET','POST'])
# def index():
#     result = rpc.service.do_something('test')
#     return result



@app.route('/login',methods=['GET','POST'])
def login():

    response = {
        "success": False,
        "message": "something went wrong",
        "data": []
    }
    request_data=request.get_json()
    print(request_data)

    with ClusterRpcProxy(config) as cluster_rpc:

        result=cluster_rpc.loginService.login_service(request_data)
        print(result,'--------result')

        if result:
            response=jsonify(result)
            response.status_code=200


    return response

@app.route('/register',methods=['POST'])
def registration():

    response = {
        "success": False,
        "message": "something went wrong",
        "data": []
    }

    request_data = request.get_json()
    print(request_data)

    with ClusterRpcProxy(config) as cluster_rpc:
        result = cluster_rpc.registrationService.registration_service(request_data)
        print(result, '--------result')

        if result:
            response = jsonify(result)
            response.status_code = 201

    return response

if __name__ == '__main__':

    app.run(debug=True)