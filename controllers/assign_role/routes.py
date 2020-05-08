from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
from sqlalchemy import and_,or_
from assets import *
from global_assets.common import *
import sys
import oyaml as yaml
from sqlalchemy.exc import IntegrityError
from libs.ansible.runner import Runner
from flask_restplus import Api, Resource
import json
import ast
from collections import OrderedDict
import logging


from global_assets.custom_response import custom_response

LOGGER = logging.getLogger(__name__)


# def close_session(func):
#
#     def inner(*args, **kwargs):
#         print("I can decorate any function")
#         output=  func(*args, **kwargs)
#
#         print("I still can decorate any function")
#         #session.close()
#         return output
#     return inner
#



mod = Blueprint('assign_role', __name__,
                        template_folder='templates')
mod_v1 =Api(mod, version='1.0', title='Todo API',
    description='A simple TODO API',
)




@mod.route('/roles', methods=['GET','POST'])
def get_all_roles():
    with open('static/role_service.json') as role_data_file:
        role_data = json.load(role_data_file)
    result=OrderedDict()
    list_roles = role_data.keys()
    list_roles.sort()
    for role in list_roles:
        result[role]=[]
        list_node_role = session.query(models.Node_role).filter_by(role_name=role).all()
        for node_role in list_node_role:
            node = session.query(models.Node).filter_by(node_id=node_role.node_id).first()
            result[role].append(models.to_json(node, 'Node', False))

    session.commit()

    #print(role_data.keys())


    res_data = result
    res_data["list_roles_and_configs"] = list_roles

    return custom_response(request,200,None,None,res_data)

@mod.route('/roles/<int:role_id>/', methods=['GET'])
def get_role_info_by_id(role_id):
    return redirect('/api/v1/roles/'+str(role_id)+'/role_info')


@mod.route('/roles/<int:role_id>/role_info', methods=['GET'])
def get_role_info(role_id):

    with open('static/role_service.json') as role_data_file:
        role_data = json.load(role_data_file)

    print(role_data.keys())

    role_info = [{ "role_name":role_name , "role_inf" : role_data[role_name]} for role_name in role_data.keys() if role_data[role_name]['id']==role_id]
    if len(role_info)==0 :
        return custom_response(request,404,"role_id Not Found!",None,{})

    role_node = []

    list_node_role = session.query(models.Node_role).filter_by(role_name=role_info[0]["role_name"]).all()
    for node_role in list_node_role:
        node = session.query(models.Node).filter_by(node_id=node_role.node_id).first()
        role_node.append(models.to_json(node, 'Node', False))

    session.close()

    res_data ={
        "role_info": role_info[0],
        "role_node" : role_node
    }


    return  custom_response(request,200,None,"Succeed Get Role Info", res_data)



@mod.route('/roles/add_host_to_role', methods=['POST'])
def add_host_to_role():
    if not request.json :
        abort(400)
    else:
        node_id = request.json.get('node_id')
        roles = request.json.get('roles')

    node = session.query(models.Node).filter_by(node_id=node_id).first()
    if node is None:
        return custom_response(request,404,"Node is not exist!",None,None)

    if node.node_info is None:
        return custom_response(request,404,"Node is not discover yet!",None,None)


    if roles is None:
        return custom_response(request,226,"Roles Data Not Valid",None,None)

    with open('static/role_service.json') as role_data_file:
        role_data = json.load(role_data_file)

        list_roles = role_data.keys()
        for role in roles:
            if role not in list_roles:

                return custom_response(request,226, "Information Role with name" + role + " is not invalid",None,None)


    for role in roles:
        node_role = models.Node_role(role_name=role)
        node.node_roles.append(node_role)
    session.add(node)
    data = {"node_info":models.to_json(node, 'Node', False)}
    session.commit()
    session.close()

    return custom_response(request,202,None,None,data)




    # return res,202


@mod.route('/roles/test_create_deployment', methods=['POST', 'GET'])
def add_all_deployment():
    nodes = session.query(models.Node).all()
    for node in nodes:
        if node.deployment is None and     node.node_roles > 0:
            deployment = models.Deployment(created_at=datetime.now(), updated_at=datetime.now(), finished_at=None,status="IN QUEUE", name = "deployement " + str(node.management_ip) )
            node.deployment = deployment
        session.add(node)
    session.commit()
    session.close()
    return custom_response(request,202, None,"Done Add Deployment to Database",None)

@mod.route('/roles/test_create_service_setup', methods=['POST', 'GET'])
def test_code_create_service_setup():
    with open('static/role_service.json') as role_data_file:
        role_data = json.load(role_data_file)
    nodes = session.query(models.Node).all()
    for node in nodes:
        deployment = node.deployment
        if deployment is not None:
            roles =[role.role_name for role in node.node_roles]

            for role in roles:
                list_services = role_data[role]['list_service']
                for service in list_services:
                    service_setup = models.Service_setup(service_type=role, service_name = service['service_name'],enable="ENABLE",  service_lib=None, service_config_folder = None, setup_index = service['index'], is_validated_success=None, validated_status = None)
                    deployment.service_setups.append(service_setup)



        session.add(node)
    session.commit()
    session.close()
    return  custom_response(request,202, None,"Done Add Service Setup to Database",None)






@mod.route('/roles/test_create_ansible_inventory_with_role', methods=['POST', 'GET'])
def test_code_create_ansible_playbook_p1():
    with open('static/role_service.json') as role_data_file:
        role_data = json.load(role_data_file)

    list_roles = role_data.keys()
    list_roles.sort()
    file_new_node = open(CONST.inventory_dir+'/new_node', "a")
    for role in list_roles:
        file_new_node.write('[' + str(role) + ':children' + ']')
        file_new_node.write("\n")
        list_node_role = session.query(models.Node_role).filter_by(role_name=role).all()
        for node_role in list_node_role:
            node = session.query(models.Node).filter_by(node_id=node_role.node_id).first()
            file_new_node.write(str(node.node_display_name))
            file_new_node.write("\n")
    file_new_node.close()

    f = open(CONST.inventory_dir+'/new_node', "r")
    return custom_response(request, 202, None, "Done Create Ansible Inventory",  {"inventory": str(f.read())})



@mod.route('/roles/test_create_ansible_playbook', methods=['POST', 'GET'])
def test_code_create_ansible_playbook_p2():

    # host_name='host_name'
    # service_name='service_name'
    # role_name = 'role_name'
#######################
############# NEN PHAN BIET SERVICE_NAME VA ROLE_NAME
#######################
    list_nodes = session.query(models.Node).all()
    list_playbooks = []
    for node in list_nodes:
        if node.deployment is not None:
            host_name = node.node_display_name
            deployment = node.deployment
            list_services = deployment.service_setups
            for service in list_services:
                service_name = service.service_name
                role_name = service.service_name
                ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
                playbook_temp = os.path.join(ROOT_DIR, 'global_assets/playbook_temp.yml')
                new_playbook = CONST.playbook_dir+'/'+'playbook_setup_'+ service_name + '_for_'+host_name + '.yml'
                os.system('\cp '+ str(playbook_temp) + ' '+new_playbook )
                os.system('sed -i "s|SERVICE_NAME|'+service_name+'|g" '+ str(new_playbook))
                os.system('sed -i "s|HOST_NAME|'+host_name+'|g" '+ str(new_playbook))
                os.system('sed -i "s|ROLE_NAME|'+role_name+'|g" '+ str(new_playbook))
                list_playbooks.append('playbook_setup_'+ service_name + '_for_'+host_name + '.yml')

    #host=





    # with open('static/role_service.json') as role_data_file:
    #     role_data = json.load(role_data_file)
    # nodes = session.query(models.Node).all()
    # for node in nodes:
    #     deployment = node.deployment
    #     roles =[role.role_name for role in node.node_roles]
    #
    #     for role in roles:
    #         list_services = role_data[role]['list_service']
    #         for service in list_services:
    #             service_setup = models.Service_setup(service_type=role, service_name = service['service_name'],service_info="ENABLE",  service_lib=None, service_config_folder = None, setup_index = service['index'], is_validated_success=None, validated_status = None)
    #             deployment.service_setups.append(service_setup)
    #
    #     session.add(node)
    # session.commit()

    return custom_response(request, 202, None, "Done Create Ansible Playbooks",  {"List Playbooks":list_playbooks})




#
@mod.route('/roles/test_create_task', methods=['POST', 'GET'])
def test_code_create_task_for_service():

    list_nodes = session.query(models.Node).all()
    for node in list_nodes:
        print(node.node_display_name)
        service_setups= get_service_setups_from_deployment(node.deployment)

        #service = service_setups[0]
        for service in service_setups:

            list_tasks = load_yml_file(CONST.role_dir+'/' + service.service_name+'/tasks/main.yml')

            list_task_info =[]
            for index,task in enumerate(list_tasks, start=0):

                task_info = {}


                for command in task.get('block'):
                    if command.get('name') is not None:
                        task_info['name'] = command.get('name')
                    elif command.get('include') is None:
                        setup_data= str(json.dumps(command))
                        task_info['setup_data'] = setup_data[:250] + (setup_data[250:] and '..')
                        task_info['task_type'] = command.keys()
                        if 'register' in task_info['task_type']: task_info['task_type'].remove('register')
                list_task_info.append(task_info)


            for index,task  in enumerate(list_task_info,start=1):

                task_data = models.Task(created_at=datetime.now(), task_display_name= task.get('name'), setup_data=task.get('setup_data'),task_type=str(task.get('task_type')), task_index= index)
                service.tasks.append(task_data)

        session.add(node)
    session.commit()
    session.close()
    return custom_response(request, 202, None, "Done Create Tasks in Database. Check in /api/v1/tasks",  None)

@mod.route('/roles/test_code7', methods=['POST', 'GET'])
def test_code_create_task_for_service7():
    ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
    return {"response: ": ROOT_DIR+CONST.inventory_dir},200






@mod.route('/hosts/deployments', methods=['GET'])
def get_all_deployments():
    deployments = session.query(models.Deployment).all()
    session.commit()
    return custom_response(request, 200, None, None,  models.to_json(deployments, 'Deployment', True))


@mod.route('/hosts/<string:host_id>/deployments', methods=['GET'])
def get_deployment(host_id):
    node = session.query(models.Node).filter_by(node_id=host_id).first()
    session.commit()


    return custom_response(request, 200, None, None,  models.to_json(node.deployment, 'Deployment', False))
@mod.route('/deployments', methods=['GET'])
def get_all_deployments_v2():
    return redirect('/api/v1/hosts/deployments')


@mod.route('/hosts/deployments/<string:deployment_id>', methods=['GET'])
def get_deployment_by_id_v0(deployment_id):
    deployment = session.query(models.Deployment).filter_by(deployment_id=deployment_id).first()
    session.commit()
    if deployment is None:
        abort(400)

    return custom_response(request, 200, None, None, models.to_json(deployment, 'Deployment', False))

@mod.route('/deployments/<string:deployment_id>', methods=['GET'])
def get_deployment_by_id(deployment_id):
    deployment = session.query(models.Deployment).filter_by(deployment_id=deployment_id).first()
    session.commit()
    if deployment is None:
        abort(400)

    return custom_response(request, 200, None, None, models.to_json(deployment, 'Deployment', False))
@mod.route('/deployments/<string:deployment_id>/service_setups', methods=['GET'])
def get_all_service_setups_v0(deployment_id):
    deployment = session.query(models.Deployment).filter_by(deployment_id=deployment_id).first()
    if deployment is None:
        abort(400)
    service_setups=get_service_setups_from_deployment(deployment)
    session.commit()

    return custom_response(request, 200, None, None, models.to_json(service_setups, 'Service_setup', True))
@mod.route('/deployments/<string:deployment_id>/<string:service_setup_id>', methods=['GET'])
def get_one_service_setup(deployment_id,service_setup_id):
    service_setup = session.query(models.Service_setup).filter_by(service_setup_id=service_setup_id, deployment_id=deployment_id).first()
    if service_setup is None:
        abort(400)
    session.commit()
    return custom_response(request, 201, None, None, models.to_json(service_setup,'Service_setup',False))


@mod.route('/service_setups/', methods=['GET'])
def get_service_setup():


    if not (request.args.get('deployment_id') or request.args.get('service_name')):
        service_setup = session.query(models.Service_setup).all()
        return custom_response(request, 200, None, None, models.to_json(service_setup, 'Service_setup', True))

    service_setup = session.query(models.Service_setup).filter_by(deployment_id=request.args.get('deployment_id'),service_name =  request.args.get('service_name')).first()
    if service_setup is None:
        abort(400)
    return custom_response(request, 200, None, None, models.to_json(service_setup, 'Service_setup', False))




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
    if not (request.args.get('service_setup_id')):

        deployment = session.query(models.Deployment).filter_by(deployment_id=deployment_id).first()
        if deployment is None:
            abort(400)
        node =deployment.node
        service_setups = get_service_setups_from_deployment(deployment)
        list_playbook = []
        for service in service_setups:
            list_playbook.append('playbook_setup_'+ service.service_name + '_for_'+node.node_display_name + '.yml')
        session.commit()
        return   custom_response(request, 200, None, None, list_playbook)



    else :
        return "INCOMMING " + str(request.args.get('service_setup_id'))

# @mod.route('/deployments/<string:deployment_id>/playbooks', methods=['GET'])
# def get_playbook_with_service_setup_id(deployment_id):
#     if not (request.args.get('service_setup_id')):
#
#
#     return "Thong tin chi tiet cua mot service setup "

@mod.route('/service_setups/<string:service_setup_id>', methods=['GET'])
def get_service(service_setup_id):
    service_setup = session.query(models.Service_setup).filter_by(service_setup_id=service_setup_id).first()
    if service_setup is None:
        abort(400)
    session.commit()
    return custom_response(request, 200, None, None, models.to_json(service_setup,'Service_setup',False))
@mod.route('/service_setups/<string:service_setup_id>/tasks', methods=['GET'])
def get_all_tasks_with_service_setups(service_setup_id):
    service_setup = session.query(models.Service_setup).filter_by(service_setup_id=service_setup_id).first()
    tasks = service_setup.tasks
    session.commit()
    return custom_response(request, 200, None, None, models.to_json(tasks,'Task',True))


@mod.route('/service_setups/<string:service_setup_id>/<string:task_id>', methods=['GET'])
def get_task(service_setup_id,task_id):
    task = session.query(models.Task).filter_by(task_id=task_id, service_setup_id=service_setup_id).first()

    if task is None:
        return abort(400)

    session.commit()
    return custom_response(request, 200, None, None,models.to_json(task, 'Task', False))

@mod.route('/tasks', methods=['GET'])
def get_all_tasks():
    result = []
    list_nodes = session.query(models.Node).all()
    for node in list_nodes:

        node_name = node.node_display_name
        node_ip = node.management_ip
        node_data = {"node_name": node_name, "node_ip": node_ip, "list_services":[]}
        list_services = get_service_setups_from_deployment(node.deployment)
        for service in list_services:

            service_name = service.service_name

            list_tasks = models.to_json(service.tasks,'Task',True)
            node_data["list_services"].append({'service_name':service_name, 'list_tasks': list_tasks})

        result.append(node_data)
    session.commit()
    return custom_response(request, 200, None, None, result)

# from random import random
@mod.route('/tasks/<string:task_id>', methods=['GET','POST'])
def get_task_by_id(task_id):
    task = session.query(models.Task).filter_by(task_id=task_id).first()

    if task is None:
        return abort(400)

    session.commit()
    return custom_response(request, 200, None, None, models.to_json(task, 'Task', False))
# class ClassTask(Resource):
#     def get(self, task_id):
#         task = session.query(models.Task).filter_by(task_id=task_id).first()
#
#         if task is None:
#             return abort(400)
#
#         session.commit()
#
#         return {'res':jsonify(models.to_json(task, 'Task', False))}, 200
#     def post(self, task_id):
#         return {
#             "status": "INCOMMMING"
#         }

@mod.route('/changes/<string:change_id>', methods=['GET'])
def get_change(change_id):
    change = session.query(models.Change).filter_by(change_id=change_id).first()
    if change is None:
        return abort(400)
    return custom_response(request, 200, None, None,models.to_json(change, 'Change', False))


@mod.route('/tasks/<string:task_id>/changes', methods=['GET'])
def get_all_changes(task_id):
    task = session.query(models.Task).filter_by(task_id=task_id).first()

    if task is None:
        return abort(400)
    changes = task.changes
    session.commit()
    return custom_response(request, 200, None, None,models.to_json(changes, 'Change', True))








@mod.route('/clean_data', methods=['GET', 'POST'])
def clean_all_data():
    if request.args.get('table') is not None:
        table = request.args.get('table')
        if table =='nodes':
            db.session.query(models.Node).delete()
        elif table =='deployments':
            db.session.query(models.Deployment).delete()
        elif table =='node_infos':
            db.session.query(models.Node_info).delete()
        elif table =='node_roles':
            db.session.query(models.Node_role).delete()
        elif table =='service_setups':
            db.session.query(models.Service_setup).delete()
        elif table =='tasks':
            db.session.query(models.Task).delete()
        elif table =='changes':
            db.session.query(models.Change).delete()
        elif table =='disk_resources':
            db.session.query(models.Disk_resource).delete()
        elif table =='interface_resources':
            db.session.query(models.Interface_resource).delete()
        db.session.commit()
        db.session.close()
        return {"response":"YOU DELETE " + table}
    else:
        try:
            db.session.commit()
            db.session.query(models.Task).delete()
            db.session.commit()
            db.session.query(models.Service_setup).delete()
            db.session.commit()
            db.session.query(models.Deployment).delete()
            db.session.commit()
            db.session.query(models.Disk_resource).delete()
            db.session.commit()
            db.session.query(models.Interface_resource).delete()
            db.session.commit()
            db.session.query(models.Node_info).delete()
            db.session.commit()
            db.session.query(models.Node_role).delete()
            db.session.commit()
            db.session.query(models.Node).delete()
            db.session.commit()
            db.session.close()
        except IntegrityError:
            # db.session.rollback()
            print("Unexpected error:", sys.exc_info()[0])

        return {"response: " : "LOOK GOOD YOU'VE DELETED ALL"}