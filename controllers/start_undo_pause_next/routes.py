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
from libs.ansible.runner import Runner
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




@mod.route('/roles/test_run_first_ansble_playbook', methods=['POST', 'GET'])
def test_code_create_ansible_playbook_p3():


    node = session.query(models.Node).first()
    service_setups= get_service_setups_from_deployment(node.deployment)

    service = service_setups[0]

    runner = Runner(playbook='playbook_setup_' + service.service_name + '_for_' + node.node_display_name + '.yml',
                    inventory='new_node', run_data={'extra_vars': {'target': 'target'}, 'tags': []},
                    start_at_task=None, step=False, private_key_file=None, become_pass=None, verbosity=None)


    # ansible-playbook ansible_compute.yml --extra-vars "target=target other_variable=foo" --tags "install, uninstall" --start-at-task=task.task_display_name --step

    print(runner.variable_manager)

    log_run = runner.run()
    print(log_run)
    return str(log_run)



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



@mod.route('/installation/runtask', methods=['POST'])
def run_specific_task():
    if not request.json:
        abort(400)
    else:
        task_id = request.json.get('task_id')
        method = request.json.get('method')

    task = session.query(models.Task).filter_by(task_id=task_id).first()

    if task is None :
        return abort(400)
    service = task.service_setup
    node = service.deployment.node

    if method == "Install":


        runner = Runner(playbook='playbook_setup_'+ service.service_name + '_for_'+node.node_display_name + '.yml', inventory='new_node', run_data={'extra_vars': {'target': 'No'}, 'tags': [str(task.task_index)]}, start_at_task=None, step=False, private_key_file=None, become_pass=None, verbosity=None)

        # ansible-playbook ansible_compute.yml --extra-vars "target=target other_variable=foo" --tags "install, uninstall" --start-at-task=task.task_display_name --step

        print(runner.variable_manager)

        log_run = runner.run()
        print(log_run)
        return str(log_run)
    else :
        return {"res":"INCOMMING"}


@mod.route('/api/v1/installation/skip', methods=['GET'])
def skip_current_installation():
    current_task = session.query(models.Task).filter_by(status='INPROCESSING').first()
    session.commit()
    if current_task is None:
        current_task = session.query(models.Task).filter_by(status='FAILED').first()
        session.commit()
    if current_task is None:
        current_task = session.query(models.Task).filter_by(status='DONE').order_by(models.Task.finished_at.desc())
        current_task = current_task[0] if current_task is not None else None
        session.commit()
    ### MAYBE ERROR IF NO TASK IS DONE

    current_task.status=current_task.status + "_" +  "SKIPPED"
    next_task = session.query(models.Task).filter_by(service_setup_id=current_task.service_setup_id,task_index= current_task.task_index+1).first()
    if next_task is None:
        current_service_setup = current_task.service_setup
        current_service_setup.status=current_service_setup.status + "_"+"SKIPPED"
        next_service_setup = session.query(models.Service_setup).filter_by(deployment_id=current_service_setup.deployment_id,setup_index= current_service_setup.setup_index+1).first()
        if next_service_setup is None:
            current_service_setup.deployment.status=current_service_setup.deployment.status+"_"+"SKIPPED"
        else:
            ###ERROR
            next_task=[t for t in next_service_setup.tasks if t.task_index == 1][0]

    return {" current_task": models.to_json(current_task,'Task',False)  ,
            " next_task": models.to_json(next_task, 'Task', False)}



@mod.route('/api/v1/installation/current', methods=['GET'])
def get_current_installation_status():
    current_task = session.query(models.Task).filter_by(status='INPROCESSING').first()
    session.commit()
    if current_task is None:
        current_task = session.query(models.Task).filter_by(status='FAILED').first()
        session.commit()
    if current_task is None:
        current_task = session.query(models.Task).filter_by(status='DONE').order_by(models.Task.finished_at.desc())
        current_task = current_task[0] if current_task is not None else None
        session.commit()

    current_service = current_task.service_setup
    current_node = current_service.deployment.node

    return {" current_task": models.to_json(current_task,'Task',False)  ,
             "current_service":models.to_json(current_service,'Service_setup',False),
             "current_node": models.to_json(current_node, 'Node', False),
             } , 200




@mod.route('/tasks/update_task', methods=['POST'])
def update_task_info():
    if not request.json:
        abort(400)
    state= request.json.get('state')
    node_ip = request.json.get('node_ip')
    task_index = int(request.json.get('task_index').encode('utf-8'))
    service_name = request.json.get('service_name').encode('utf-8')
    logging.debug("TYPE INDEX: " + str(type(task_index)))

    task = session.query(models.Task).filter(and_(models.Task.task_index == task_index, models.Task.service_setup.has(models.Service_setup.service_name == str(service_name)),
                                                  models.Task.service_setup.has(models.Service_setup.deployment.has(
                                                      models.Deployment.node.has(
                                                          models.Node.management_ip == str(node_ip))))) ).first()

    if task is None:
        session.commit()
        return {"res": "Error Task Not Found" + 'node_ip: ' + str(
            node_ip) + ' service_name: ' + str(service_name)+ ' task_index: ' + str(task_index) }, 200



    info = request.json.get('info')
    if state == "before_task" :
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


    logging.debug("INFO: " + json.dumps(info))
    logging.debug("INFO.failed: " + str(info.get('failed')))
    logging.debug("INFO.results: " + str(info.get('results')))
    logging.debug("INFO.stderr: " + str(info.get('stderr')))
    logging.debug("INFO.stdout: " + str(info.get('stdout')))

    if state == "after_task_failse":
        task.status = "FAILED"
        task.service_setup.status = "FAILED"
        task.service_setup.deployment.status = "FAILED"

    if state == "after_task_ok":
        if info.get('failed') is True:
            task.status = "FAILED_IGNORE"
        else:
            task.status = "DONE"

        task.service_setup.status = "DONE" if task.task_index == len(task.service_setup.tasks) else "INPROCESSING"
        task.service_setup.deployment.status = "INPROCESSING"
        task.finished_at = datetime.now()

    if 'command' in task.task_type:
        task.log =json.dumps(info.get('results'))
        if info.get('results') is not None:
            task_result = "SUCCEED "
            task.changes[:] = []
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


    if 'template' in task.task_type:
        if info.get('changed') == True:
            task.result = "SUCCEED CHANGE FILE: "+info.get('dest')
            task.log = "dest: "+  info.get('dest') + '|| backup: ' + info.get('backup_file')
            task.changes[:] = []
            file_config_id = -1
            change = models.Change(created_at=datetime.now(), change_type='template', status='OK',
                                   change_log=task.log, finished_at=datetime.now(), file_config_id=file_config_id)
            task.changes.append(change)
        else :
            if info.get('failed') == False:
                task.result = "DONE NOTHING CHANGED: " + info.get('dest')
            else :
                task.result = "FAILED TO CHANGE FILE " + str(info.get('msg'))
                task.log = json.dumps(info)
    if 'systemd' in task.task_type:
        if info.get('changed') == True:
            task.result = "SUCCEED SYSTEMD SERVICE: " + info.get('name')
            task.log = "service: " + info.get('name') + '|| state: ' + info.get('state') + '|| enable: ' + info.get('enable')
            task.changes[:] = []
            file_config_id = -1
            change = models.Change(created_at=datetime.now(), change_type='service', status='OK',
                                   change_log=task.log, finished_at=datetime.now(), file_config_id=file_config_id)
            task.changes.append(change)
        else :
            if info.get('failed') == False:
                task.result = "DONE NOTHING CHANGED: " + info.get('name')
            else :
                task.result = "FAILED TO CHANGE SERVICE " + str(info.get('msg'))
                task.log = json.dumps(info)
    session.add(task)
    session.commit()
    return jsonify(models.to_json(task, 'Task', False)) , 200