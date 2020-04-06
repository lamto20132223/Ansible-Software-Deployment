from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
from sqlalchemy import and_,or_
from assets import *


from flask_restplus import Api, Resource

mod = Blueprint('start_undo_pause_next', __name__,
                        template_folder='templates')

mod_v1 =Api(mod, version='1.0', title='Todo API',
    description='A simple TODO API',
)


@mod_v1.route('/installation', methods=['GET','POST'])
class Installation(Resource):

    def get(self):
        return "Danh sach node + status cai tren tung node"

    def post(self):
        action = request.args.get('action')
        if not (request.args.get('action') ):
            abort(400)

        if action == "START":
            return "START INSTALL"
        if action == "UNDO":
            return "BACK TO THE HOLE"
        if action == "PAUSE":
            return "WAITE FOR IT"
        if action == "NEXT":
            return "SKIP TO NEXT "

        return "WRONG ACTION"


@mod.route('/installation/node_info', methods=['GET'])
def get_all_node_info():
    return "List ke trang thai cua installation tren Node: Danh sach cac Service_setup + status cai tren tung Service_setup"


@mod.route('/installation/service_info', methods=['GET'])
def get_service_info():
    if not (request.args.get('node_id')):
        abort(400)

    return "INCOMMING"



@mod.route('/installation/task_info', methods=['GET'])
def get_task_info():
    if not (request.args.get('service_id')):
        abort(400)

    return "INCOMMING"


@mod.route('/installation/change_info', methods=['GET'])
def get_change_info():
    if not (request.args.get('task_id')):
        abort(400)

    return "INCOMMING"



# - GET / api / v1 / installation / node_info
#
#
# - GET / api / v1 / installation / service_info?node_id =
#
#
# - GET / api / v1 / installation / task_info?service_id =
#
#
# - GET / api / v1 / installation / change_info?task_id =
# /api/v1/installation/current ==> node service task
#
# /api/v1/installation/start
#
# /api/v1/installation/runtask
#
# /api/v1/installation/undo
# /api/v1/installation/pause
# /api/v1/installation/skip
#
