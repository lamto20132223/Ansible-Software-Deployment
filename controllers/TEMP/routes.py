from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
from sqlalchemy import and_,or_
from assets import *

mod = Blueprint('assign_role', __name__,
                        template_folder='templates')



@mod.route('/roles', methods=['GET','POST'])
def get_all_roles():
    return "INCOMMING"



@mod.route('/roles/<string:role_id>/role_info', methods=['GET'])
def get_role_info(role_id):
    return "INCOMMING" + str(role_id)


@mod.route('/roles/add_host_to_role', methods=['POST'])
def add_host_to_role():
    if not request.json :
        abort(400)
    else:
        data = request.json

    return "INCOMMING"


@mod.route('/hosts/<string:host_id>/deployments', methods=['GET'])
def get_all_deployments(host_id):
    return "INCOMMING" + str(host_id)

@mod.route('/deployments/<string:deployment_id>/service_setups', methods=['GET'])
def get_all_service_setups(deployment_id):
    return "INCOMMING" + str(deployment_id)

@mod.route('/service_setups/', methods=['GET'])
def get_service_setup():
    if not (request.args.get('deployment_id') and request.args.get('service_name')):
        abort(400)

    return "Thông tin chi tiết của một service_setup "



@mod.route('/service_setups/disable_setup/', methods=['POST'])
def edit_disable_service():
    if not request.json :
        abort(400)
    else:
        data = request.json


    return "INCOMMING"

@mod.route('/service_setups/enable_setup/', methods=[ 'POST'])
def edit_enable_service():
    if not request.json :
        abort(400)
    else:
        data = request.json

    return "INCOMMING"

@mod.route('/deployments/<string:deployment_id>/playbooks', methods=['GET'])
def get_all_playbooks(deployment_id):
    return "INCOMMING"

@mod.route('/deployments/<string:deployment_id>/playbooks', methods=['GET'])
def get_playbook_with_service_setup_id(deployment_id):
    if not (request.args.get('deployment_id') and request.args.get('service_name')):
        abort(400)

    return "Thông tin chi tiết của một service_setup "
    return "INCOMMING"

@mod.route('/service_setups/<string:service_setup_id>/tasks', methods=['GET'])
def get_all_tasks(service_setup_id):
    return "INCOMMING"

@mod.route('/service_setups/<string:service_setup_id>/tasks_____task_id', methods=['GET', 'POST'])
def get_task(service_setup_id):
    return "INCOMMING"

@mod.route('tasks/<string:task_id>', methods=['GET'])
def get_set_host_historys(task_id):
    return "INCOMMING"
