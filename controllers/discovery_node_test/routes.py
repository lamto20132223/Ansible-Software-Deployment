from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
from sqlalchemy import and_,or_
from assets import *
from global_assets.custom_response import custom_response
import global_assets.const as CONST

mod = Blueprint('discovery_node', __name__,
                        template_folder='templates')




@mod.route('/hosts/add_host', methods=['POST'])
def add_host():
    if not request.json :
        abort(400)
    else:
        data = request.json
    old_nodes = session.query(models.Node).filter(or_(models.Node.management_ip==data.get('management_ip'), models.Node.node_display_name==data.get('node_display_name').lower())).all()
    if len(old_nodes) != 0:
        return custom_response(request, 226, "Node da ton tai", None,None)

    node = models.Node(created_at=datetime.now(), updated_at=datetime.now(), deleted_at=None, management_ip=data.get('management_ip', ""),ssh_user=data.get('ssh_user',""), ssh_password=data.get('ssh_password',  ""), status="set_ip", node_display_name=data.get('node_display_name', ''))

    session.add(node)
    session.commit()
    new_node = session.query(models.Node).filter_by(node_display_name=str(data.get('node_display_name', ''))).all()
    res = jsonify(models.to_json(new_node, 'Node',True))
    session.close()
    #print(models.to_json(new_node, 'Node',True))
    return custom_response(request, 201, None, None,res)


@mod.route('/hosts/update_host', methods=['POST'])
def update_host_ssh():
    if not request.json :
        abort(400)
    else:
        data = request.json
    node =session.query(models.Node).filter_by(node_id=data.get('node_id')).first()
    if node is None:
        return custom_response(request, 404, "Node chua ton tai", None,None)

    node.updated_at = datetime.now()
    node.management_ip = data.get('management_ip', "")
    node.ssh_user=data.get('ssh_user',"")
    node.ssh_password = data.get('ssh_password', "")
    node.status = "set_ip"
    node.node_display_name = data.get('node_display_name', '')


    session.add(node)
    session.commit()

    res = jsonify(models.to_json(node, 'Node',False))
    session.close()
    #print(models.to_json(new_node, 'Node',True))
    return custom_response(request, 200, None, None,res)


@mod.route('/hosts', methods=['GET'])
def get_hosts():

    ############UNDONE /api/v1/hosts?role=compute

    ############UNDONE /api/v1/hosts?role=controller

    nodes = session.query(models.Node).all()
    res = jsonify(models.to_json(nodes, 'Node', True))
    #print(models.to_json(nodes, 'Node', True))
    return res, 200

@mod.route('/hosts/<string:host_id>', methods=['GET'])
def get_host(host_id):
    if host_id is None:
        return redirect('/api/v1/hosts/all')
    selected_node = session.query(models.Node).filter_by(node_id=str(host_id)).all()
    if len(selected_node) ==0:
        return abort(404)
    else:
        res =  jsonify(models.to_json(selected_node[0], 'Node', False))
        return custom_response(request, 200,None, None,res)


@mod.route('/hosts/discover_hosts_v1', methods=['POST']) #################################### ERROR #######################
def discover_hosts_v1():
    inventory_dir = CONST.inventory_dir+'/new_node'
    facts_dir = CONST.facts_dir
    inventory_data = get_facts(inventory_dir, facts_dir)
    # load_node_info_to_database(facts_dir)
    return custom_response(request, 200,None, None,inventory_data)

@mod.route('/hosts/discover_hosts_v2', methods=['POST']) #################################### ERROR #######################
def discover_hosts_v2():
    inventory_dir = CONST.inventory_dir+'/new_node'
    facts_dir = CONST.facts_dir
    get_facts_local(inventory_dir, facts_dir)
    load_node_info_to_database(facts_dir)
    return redirect('/api/v1/hosts/')


@mod.route('/hosts/discover_hosts', methods=['POST']) #################################### ERROR #######################
def discover_hosts():
    inventory_dir = CONST.inventory_dir+'/new_node'
    facts_dir = CONST.facts_dir
    get_facts(inventory_dir, facts_dir)
    res = load_node_info_to_database(facts_dir)
    return custom_response(request, 200,None, 'Discover host sucessfully. Check Result in /api/v1/hosts',res)

@mod.route('/hosts/host_info', methods=['GET']) ############################### UNDONE ##################
def get_host_info():
    if request.args.get('host_id') is None:
        return abort(400)
    host_id = request.args.get('host_id')
    nodes = session.query(models.Node).filter_by(node_id=str(host_id)).first()

    if nodes is None:
        return abort(400)
    #print(nodes.node_info)
    if request.args.get("fields") is None:
        return custom_response(request, 200, None, None, jsonify(models.to_json(nodes.node_info, 'Node_info',False)))
    else:
        return custom_response(request, 200, None, None,models.to_json(nodes.node_info, 'Node_info',False))


@mod.route('/hosts/interface_resources', methods=['GET'])
def get_interface_resources():
    interface_id = request.args.get('interface_id')
    device_name = request.args.get('device_name')
    host_id = request.args.get('host_id')

    if interface_id is not None:
        interface_resource = session.query(models.Interface_resource).filter_by(interface_id=str(interface_id)).first()
        return custom_response(request, 200, None, None,jsonify(models.to_json(interface_resource, 'Interface_resource', False)))

    if host_id is not None:
        if device_name is not None:
            list_interface_resources=session.query(models.Interface_resource).filter(and_(models.Interface_resource.device_name==str(device_name) , models.Interface_resource.node_info.has(models.Node_info.node.has(models.Node.node_id==host_id)))).all()
            return custom_response(request, 200, None, None,jsonify(models.to_json(list_interface_resources, 'Interface_resource', True)))
        else:
            list_interface_resources = session.query(models.Interface_resource).filter( models.Interface_resource.node_info.has(models.Node_info.node.has(models.Node.node_id==host_id))).all()
            return custom_response(request, 200, None, None,jsonify(models.to_json(list_interface_resources, 'Interface_resource', True)))
    if device_name is not None:
        list_interface_resources = session.query(models.Interface_resource).filter_by(device_name=str(device_name)).all()
        return custom_response(request, 200, None, None,jsonify(models.to_json(list_interface_resources, 'Interface_resource', True)))

    return abort(400)


@mod.route('/hosts/disk_resources', methods=['GET'])
def get_disk_resources():
    disk_id = request.args.get('disk_id')
    device_name = request.args.get('device_name')
    host_id = request.args.get('host_id')

    if disk_id is not None:
        disk_resource = session.query(models.Disk_resource).filter_by(disk_id=str(disk_id)).first()
        return custom_response(request, 200, None, None,jsonify(models.to_json(disk_resource, 'Disk_resource', False)))

    if host_id is not None:
        if device_name is not None:
            list_disk_resources=session.query(models.Disk_resource).filter(and_(models.Disk_resource.device_name==str(device_name) , models.Disk_resource.node_info.has(models.Node_info.node.has(models.Node.node_id==host_id)))).all()
            return custom_response(request, 200, None, None,
                                   jsonify(models.to_json(list_disk_resources, 'Disk_resource', True)))
        else:
            list_disk_resources = session.query(models.Disk_resource).filter( models.Disk_resource.node_info.has(models.Node_info.node.has(models.Node.node_id==host_id))).all()
            return custom_response(request, 200, None, None,
                                   jsonify(models.to_json(list_disk_resources, 'Disk_resource', True)))

    if device_name is not None:
        list_disk_resources = session.query(models.Disk_resource).filter_by(device_name=str(device_name)).all()
        return custom_response(request, 200, None, None,
                               jsonify(models.to_json(list_disk_resources, 'Disk_resource', True)))

    return abort(400)

@mod.route('/hosts/<string:host_id>/historys', methods=['GET', 'POST'])
def get_set_host_historys(host_id):
    return "INCOMMING"

@mod.route('/hosts/<string:host_id>/refresh', methods=['GET'])
def refresh_host_info(host_id):
    return "INCOMMING"




