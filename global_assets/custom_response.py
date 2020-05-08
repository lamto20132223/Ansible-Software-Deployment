from datetime import datetime
from flask import jsonify
import json

from collections import OrderedDict

def custom_response(request=None, status_code=None,error_message=None, info_message=None,res_data=None):
    res =  OrderedDict()
    res["timestamp"] = str( datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    res["request"] =  { "request":request.method + " " + request.base_url, "req_data": json.loads(request.data) if request.data is not "" else None}
    res["status_code"] = status_code
    res["error"] = error_message
    res["message"] = info_message
    res["data"] = res_data

    print(jsonify(res))
    return jsonify(res),status_code

def custom_response_flask_restful(request=None, status_code=None,error_message=None, info_message=None,res_data=None):
    res =  OrderedDict()
    res["timestamp"] =str( datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    res["request"] =  { "request":request.method + " " + request.base_url, "req_data": json.loads(request.data) if request.data is not "" else None}
    res["status_code"] = status_code
    res["error"] = error_message
    res["message"] = info_message
    res["data"] = res_data

    return res,status_code

# print(jsonify(custom_response(status_code=200)))