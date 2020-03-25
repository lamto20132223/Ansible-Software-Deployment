from flask import Blueprint, render_template, abort,  abort, jsonify, request,make_response, redirect
from jinja2 import TemplateNotFound
from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
from sqlalchemy import and_,or_
from assets import *

mod = Blueprint('old_test_assign_role', __name__,
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


# - GET: List_ROle: / api / roles /
@mod.route('/roles', methods=['GET', 'POST'])
def get_roles():
    resutl={}

    for role in list_roles:
        resutl[role]=[]
        list_node_role=session.query(models.Node_role).filter_by(role_name=role).all()
        for node_role in list_node_role:
            node=session.query(models.Node).filter_by(node_id=node_role.node_id).first()
            resutl[role].append(models.to_json(node, 'Node',False))

    return jsonify(resutl), 201


@mod.route('/roles/<string:role_name>', methods=['GET', 'POST'])
def get_role(role_name):

    if role_name not in list_roles:
        return  abort(400)
    resutl=[]
    list_node_role=session.query(models.Node_role).filter_by(role_name=role_name).all()
    for node_role in list_node_role:
        node=session.query(models.Node).filter_by(node_id=node_role.node_id).first()
        resutl.append(models.to_json(node, 'Node',False))

    return jsonify(resutl), 201

@mod.route('/api/assign_role', methods=['POST'])
def post_role():
    if not request.json :

        abort(400)
    node_id=request.json.get('node_id')
    roles=request.json.get('roles')
    node = session.query(models.Node).filter_by(node_id=node_id).first()

    for role in roles:
        node_role=models.Node_role(role_name=role)
        node.node_roles.append(node_role)
    session.add(node)
    session.commit()
    return make_response({"ok":"ok"})



    # if role_name not in list_roles:
    #     return  abort(400)
    # resutl=[]
    # list_node_role=session.query(models.Node_role).filter_by(role_name=role_name).all()
    # for node_role in list_node_role:
    #     node=session.query(models.Node).filter_by(node_id=node_role.node_id).first()
    #     resutl.append(models.to_json(node, 'Node',False))
    #
    # return jsonify(resutl), 201



@mod.route()














# - Get: list_service in role / api / roles?role_id = xxx
#
# - POST: / api / assign_role /
# DICT: {node_id:, role}
# - GET / hosts / host_name / service_setups
# - POST / host / host_name / service_setups / disable
# Json: list_disable_service
#
# - GET / host / host_name / service_setups / < string:service_setup_id > / playbooks
# - GET / host / host_name / service_setups / < string:service_setup_id > / tasks / < task_id >


