from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
from sqlalchemy import and_,or_
from assets import *

mod = Blueprint('management_file_config', __name__,
                        template_folder='templates')



@mod.route('/configs/<string:host_id>', methods=['GET'])
def get_all_config_in_host(host_id):
    return "INCOMMING"

@mod.route('/configs/filter', methods=['GET'])
def search_file_config():
    if not (request.args.get('name') and request.args.get('path') and request.args.get('node') and request.args.get('service')):
        abort(400)
    return "INCOMMING"


@mod.route('/configs/download_configs', methods=['POST'])
def download_file_config():
    if not request.json :
        abort(400)
    else:
        data = request.json

    return "INCOMMING"

@mod.route('/configs/compare_config_db_vs_host', methods=['GET'])
def compare_config_db_vs_host():
    if not (request.args.get('host_id')) or not (request.args.get('file_config_id')):
        abort(400)
    return "INCOMMING"

@mod.route('/configs/compare_config_db_vs_db', methods=['GET'])
def compare_config_db_vs_db():
    if not (request.args.get('file_config_1_id') and request.args.get('file_config_1_id')):
        abort(400)
    return "INCOMMING"

@mod.route('/configs/compare_config_host_vs_host', methods=['GET'])
def compare_config_host_vs_host():
    if not (request.args.get('file_config_1_id') and request.args.get('file_config_2_id') ):
        abort(400)
    return "INCOMMING"


@mod.route('/configs/<string:file_config_id>', methods=['GET'])
def get_file_config_content():
    return "Lay ra noi dung cua File_config ID"

@mod.route('/configs/<string:file_config_id>/services', methods=['GET'])
def get_list_services_related_to_file_config():
    return "Lay danh sach service dang su dung file_config"

@mod.route('/configs/<string:file_config_id>/content', methods=['GET'])
def get_file_config_content_with_type():
    if not (request.args.get('type')):
        abort(400)
    return " Lay ra noi dung file_config theo type de so sanh voi nhau + database: dang o trong database + server: Noi dung thuc te tren server + lastupdate: Noi dung truoc khi commit, update"






@mod.route('/configs/update', methods=['POST'])
def update_file_config_from_db_server():
    if not (request.args.get('file_config_id')):
        abort(400)
    return "Update File Config From DB to Server"



@mod.route('/configs/commit', methods=['POST'])
def update_file_config_from_server_to_server():
    if not (request.args.get('file_config_id')):
        abort(400)
    return "Update File Config From DB to Server"

@mod.route('/configs/rollback', methods=['POST'])
def rollback_file_config():
    if not (request.args.get('file_config_id')):
        abort(400)
    return "Update File Config From DB to Server"