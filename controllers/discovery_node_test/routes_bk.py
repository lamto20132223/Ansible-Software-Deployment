from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
from sqlalchemy import and_,or_
from assets import *

mod = Blueprint('discovery_node', __name__,
                        template_folder='templates')
# admin_bp = Blueprint('admin_bp', __name__,
#                      template_folder='templates',
#                      static_folder='static')


# @mod.route('/lamtv10')
# def lamtv10():
#     return 'lamtv10'
#
# @mod.route('/<page>')
# def show(page):
#     try:
#         return render_template('pages/%s.html' % page)
#     except TemplateNotFound:
#         abort(404)







@mod.route('/api/addnodes', methods=['POST'])
def add_node():
    if not request.json :

        abort(400)
    old_nodes = session.query(models.Node).filter_by(management_ip=request.json.get('management_ip')).all()
    if len(old_nodes) != 0:
        return {"status":"Node da ton tai"}


    node = models.Node(created_at=datetime.now(), updated_at=datetime.now(), deleted_at=None, management_ip=request.json.get('management_ip', ""),
                 ssh_user=request.json.get('ssh_user',""), ssh_password=request.json.get('ssh_password',  ""), status="set_ip", node_display_name=request.json.get('node_display_name', ''))

    session.add(node)
    session.commit()
    new_node = session.query(models.Node).filter_by(node_display_name=str(request.json.get('node_display_name', ''))).all()

    print(models.to_json(new_node, 'Node',True))

    return jsonify(models.to_json(new_node, 'Node',True)), 201


@mod.route('/hosts/all')
def getnodes():
    nodes = session.query(models.Node).all()

    print(models.to_json(nodes, 'Node',True))

    return jsonify(models.to_json(nodes, 'Node', True)), 201

@mod.route('/hosts')
def getnode():

    node_id = request.args.get('node_id')
    if node_id is None:
        return  redirect('/api/v1/hosts/all')
    selected_node =session.query(models.Node).filter_by(node_id=str(node_id)).first()
    return jsonify(models.to_json(selected_node, 'Node', False)), 201



@mod.route('/api/load_all_node_db', methods=['GET','POST'])
def load_all_node():


    inventory_dir = '/home/vttek/lamtv10/etc/ansible/inventory/new_node'
    facts_dir = '/home/vttek/lamtv10/etc/ansible/facts/'
    get_facts(inventory_dir, facts_dir)
    load_node_info_to_database(facts_dir)
    return redirect('/api/v1/hosts/all')



# @mod.route('/api/test/ansible1')
# def ansible1():
#     #test_add_nodes()
#     print("lamtv10")
#     runner = ansible.Checker('ansible_compute.yml','multnode',{'extra_vars':{'target':"ta1",''} ,'tags':['install','uninstall']},None, False,  None,None,None)
#     stats = runner.run()
#     return jsonify(ansible.get_stats(stats))






@mod.route('/hosts/<host_name>', methods=['GET'])
def gethost(host_name):
    print('alo alo')
    nodes = session.query(models.Node).filter_by(node_display_name=str(host_name)).first()


    print(models.to_json(nodes, 'Node',False))

    return jsonify(models.to_json(nodes, 'Node', False)), 201

@mod.route('/hosts/<string:host_name>/node_info')
def getnodeinfo(host_name):
    nodes = session.query(models.Node).filter_by(node_display_name=str(host_name)).first()

    print(nodes.node_info)
    return jsonify(models.to_json(nodes.node_info, 'Node_info',False)), 201

@mod.route('/hosts/<string:host_name>/node_info/interface_resources', methods=['GET'])
#http://127.0.0.1:4321/hosts/controller_03/node_info/interface_resources?device_name=enx1&interface_id=2
def get_interface_resource(host_name):
    interface_id = request.args.get('interface_id')
    device_name= request.args.get('device_name')
    if  interface_id is None and device_name is None:
        list_interface_resources= session.query(models.Interface_resource).filter(models.Interface_resource.node_info.has(models.Node_info.node.has(models.Node.node_display_name==host_name))).all()
        return jsonify(models.to_json(list_interface_resources,'Interface_resource', True)), 201

    if interface_id is not None and device_name is not None:
        return "Select 1", 400
    if interface_id is not None:
        interface_resource =session.query(models.Interface_resource).filter(and_(models.Interface_resource.interface_id==str(interface_id) , models.Interface_resource.node_info.has(models.Node_info.node.has(models.Node.node_display_name==host_name)))).first()
        return jsonify(models.to_json(interface_resource, 'Interface_resource', False)), 201
    if device_name is not None:
        interface_resource =session.query(models.Interface_resource).filter_by(and_(models.Interface_resource.device_name==str(device_name) , models.Interface_resource.node_info.has(models.Node_info.node.has(models.Node.node_display_name==host_name)))).first()
        return jsonify(models.to_json(interface_resource, 'Interface_resource', False)), 201



@mod.route('/hosts/<string:host_name>/node_info/disk_resources', methods=['GET'])
#http://127.0.0.1:4321/hosts/controller_03/node_info/interface_resources?device_name=enx1&interface_id=2
def get_disk_resource(host_name):
    disk_id = request.args.get('disk_id')
    device_name= request.args.get('device_name')
    if  disk_id is None and device_name is None:
        list_disk_resources= session.query(models.Disk_resource).filter(models.Disk_resource.node_info.has(models.Node_info.node.has(models.Node.node_display_name==host_name))).all()
        return jsonify(models.to_json(list_disk_resources,'Disk_resource', True)), 201

    if disk_id is not None and device_name is not None:
        return "Select 1", 400
    if disk_id is not None:
        disk_resource = session.query(models.Disk_resource).filter(
            and_(models.Disk_resource.disk_id == str(disk_id), models.Disk_resource.node_info.has(
                models.Node_info.node.has(models.Node.node_display_name == host_name)))).first()
        return jsonify(models.to_json(disk_resource, 'Disk_resource', False)), 201
    if device_name is not None:
        disk_resource = session.query(models.Disk_resource).filter(
            and_(models.Disk_resource.device_name == str(device_name), models.Disk_resource.node_info.has(
                models.Node_info.node.has(models.Node.node_display_name == host_name)))).first()
        return jsonify(models.to_json(disk_resource, 'Disk_resource', False)), 201



#
# @mod.route('/hosts/<string:host_name>/node_roles')
# @mod.route('/hosts/<string:host_name>/service_infos')
# @mod.route('/hosts/<string:host_name>/node_info/interface_resources')
# @mod.route('/hosts/<string:host_name>/node_info/disk_resources')
# @mod.route('/hosts/<string:host_name>/node_info')
# @mod.route('/hosts/<string:host_name>/node_info')
# @mod.route('/hosts/<string:host_name>/node_info')
# @mod.route('/hosts/<string:host_name>/node_info')



#
# @mod.route('/hosts/')









