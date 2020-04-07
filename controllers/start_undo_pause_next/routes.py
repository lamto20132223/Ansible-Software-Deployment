from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
import sys
import oyaml as yaml
from sqlalchemy import and_,or_
from assets import *
import logging
import libs.ansible.runner as runner
from flask_restplus import Api, Resource
import json
import ast
LOGGER = logging.getLogger(__name__)

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




@mod.route('/tasks/update_task', methods=['POST'])
def update_task_info():
    if not request.json:
        abort(400)
    node_ip = request.json.get('node_ip')
    task_index = request.json.get('task_index')

    logging.debug("TYPE INDEX: " + str(type(task_index)))

    task = session.query(models.Task).filter(and_(str(models.Task.task_index) == str(task_index),
                                                  models.Task.service_setup.has(models.Service_setup.deployment.has(
                                                      models.Deployment.node.has(
                                                          models.Node.management_ip == str(node_ip)))))).first()

    if task is None:
        session.commit()
        return {"res": "Error Task Not Found" + 'node_ip: ' + str(
            node_ip) + ' task_index: ' + task_index }, 200



    info = request.json.get('info')
    if info is None:
        task.status = 'INPROCESSING'
        task.result = 'UNDONE'
        task.service_setup.status="INPROCESSING"
        task.service_setup.deployment.status="INPROCESSING"
        session.add(task)
        session.commit()
        return jsonify(models.to_json(task, 'Task', False)) , 200


    logging.debug("TYPE INFO: " + str(type(info)))
    if type(info) is unicode:
        info = info.encode('utf-8')
    if type(info) is not  dict:
        info = ast.literal_eval(info)



    logging.debug("INFO.failed: " + str(info.get('failed')))
    logging.debug("INFO.results: " + str(info.get('results')))
    logging.debug("INFO.stderr: " + str(info.get('stderr')))
    logging.debug("INFO.stdout: " + str(info.get('stdout')))



    if info.get('failed') is True:
        task.status = "FAILED"
    else:
        task.status = "DONE"
        task.finished_at = datetime.now()
    task.log =json.dumps(info.get('results'))
    if info.get('results') is not None:
        task_result = "SUCCEED "
        for index, change_info in enumerate(info.get('results'), start=1):
            change_status = "OK" if change_info.get('failed') is False else "FAILED"
            change_log = " stdout = " +  change_info.get("stdout") +"|| stderr = " + change_info.get("stderr")
            task_result = "ERROR " + change_info.get("stderr") if change_info.get("stderr") != "" else task_result + change_info.get("stdout")
            finished_at = datetime.now() if change_info.get('failed') is False else None
            change_type = json.dumps(change_info)
            change_type = change_type[:250] + (change_type[250:] and '..')
            file_config_id = -1
            change = models.Change(created_at=datetime.now(), change_type=change_type, status=change_status , change_log=change_log, finished_at=finished_at, file_config_id = file_config_id)
            task.changes.append(change)

        task.result = task_result
        if "ERROR" in task_result:
            task.service_setup.status = "FAILED"
            task.service_setup.deployment.status = "FAILED"
        else:
            task.service_setup.status = "DONE" if  task.task_index == len(task.service_setup.tasks) else "INPROCESSING"
            task.service_setup.deployment.status = "INPROCESSING"


    session.add(task)
    session.commit()
    return jsonify(models.to_json(task, 'Task', False)) , 200




