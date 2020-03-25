from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
from sqlalchemy import and_,or_
from assets import *


from flask_restplus import Api, Resource

mod = Blueprint('change_password', __name__,
                        template_folder='templates')

mod_v1 =Api(mod, version='1.0', title='Todo API',
    description='A simple TODO API',
)



@mod.route('/passwords', methods=['GET'])
def get_all_passwords():
    return {"status":"Liet ke danh sach User, Password"}


@mod_v1.route('/passwords/<string:password_id>', methods=['GET' , 'PUT'])
class Specific_Configs(Resource):
    def get(self,password_id):
        return { "status": "Lay cac thong tin lien quan den password nay nhu file_config su dung, service su dung" }

    def put(self):
        return { "status": "Cap nhat password moi" }
