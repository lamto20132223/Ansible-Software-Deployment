from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
from sqlalchemy import and_,or_
from assets import *

mod = Blueprint('gen_template', __name__,
                        template_folder='templates')



@mod.route('/templates', methods=['GET'])
def get_all_templates():
    return "Liet ke danh sach tat ca templates"



@mod.route('/templates/filter', methods=['GET'])
def search_template():
    if not (request.args.get('properties.name') and request.args.get('properties.type')):
        abort(400)

    return "TIm kiem template theo name. type"

