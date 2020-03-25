from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
from sqlalchemy import and_,or_
from assets import *

mod = Blueprint('replace_controller', __name__,
                        template_folder='templates')



@mod.route('/hosts/replace_controller', methods=['POST'])
def replace_controller():
    return "Thuc hien thao tac replace_controller, body data la thong tin host controller moi va host controller se bi go bo khoi he thong"



