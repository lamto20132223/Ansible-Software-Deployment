from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
from sqlalchemy import and_,or_
from assets import *

mod = Blueprint('scalling_up_scalling_down', __name__,
                        template_folder='templates')






@mod.route('/hosts/scalling_up_host', methods=['POST'])
def scalling_up_host():
    return "INCOMMING Thuc hien thao tac scalling_up, body data la thong tin host compute moi"


@mod.route('/hosts/scalling_down_host', methods=['DELETE'])
def scalling_down_host():
    return "Thuc hien thao tac scalling down, body data la id host compute se bi go bo khoi he thong"


