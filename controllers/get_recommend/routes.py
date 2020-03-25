from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
from sqlalchemy import and_,or_
from assets import *

mod = Blueprint('get_recommend', __name__,
                        template_folder='templates')



@mod.route('/recommendations/assign_role', methods=['POST'])
def get_recommend_assign_role():
    return "INCOMMING"



@mod.route('/recommendations/select_service ', methods=['POST'])
def get_recommend_select_service():
    return "INCOMMING"


@mod.route('/recommendations/gen_password', methods=['POST'])
def get_recommend_password():
    if not request.json :
        abort(400)
    else:
        data = request.json

    return "INCOMMING"


@mod.route('/recommendations/select_IP', methods=['POST'])
def get_recommend_select_ip():
    return "INCOMMING"

@mod.route('/recommendations/select_folders', methods=['POST'])
def get_recommend_select_folder():
    return "INCOMMING"

@mod.route('/recommendations/configs', methods=['POST'])
def get_recommend_configs():

    return "Get recommend config "

