from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
from sqlalchemy import and_,or_
from assets import *




from flask_restplus import Api, Resource

mod = Blueprint('insert_specific_config', __name__,
                        template_folder='templates')

mod_v1 =Api(mod, version='1.0', title='Todo API',
    description='A simple TODO API',
)



@mod_v1.route('/configs/specific_configs', methods=['GET', 'POST' , 'PUT'])
class Specific_Configs(Resource):
    def get(self):
        return { "status": "Got new data" }
    def post(self):
        return { "status": "Posted new data" }
    def put(self):
        return { "status": "Posted new data" }


@mod.route('/configs/specific_configs/validate', methods=['POST'])
def validate_specific_config():
    if not request.json :
        abort(400)
    else:
        data = request.json
    return "INCOMMING"


@mod.route('/configs/specific_configs/recommend', methods=['GET'])
def get_recommend_config():
    if not (request.args.get('config_key') and request.args.get('config_value')):
        abort(400)

    return "INCOMMING"


@mod.route('/configs/specific_configs/submit', methods=['POST'])
def submit_configs():
    if not request.json:
        abort(400)
    else:
        data = request.json
    return "INCOMMING"


