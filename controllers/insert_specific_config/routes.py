from flask import Blueprint, render_template, abort, abort, jsonify, request, make_response, redirect
from jinja2 import TemplateNotFound
from app import db, session, Node_Base, Column, relationship, ansible
from datetime import datetime
import models
import os
from sqlalchemy import and_, or_
from assets import *
from controllers.insert_specific_config.test import ROOT_DIR

from global_assets.common import *

from flask_restplus import Api, Resource

mod = Blueprint('insert_specific_config', __name__,
                template_folder='templates')

mod_v1 = Api(mod, version='1.0', title='Todo API',
             description='A simple TODO API',
             )


@mod_v1.route('/configs/specific_configs', methods=['GET', 'POST', 'PUT'])
class Specific_Configs(Resource):
    def get(self):
        return {"status": "Got new data"}

    def post(self):
        return {"status": "Posted new data"}

    def put(self):
        return {"status": "Posted new data"}


@mod.route('/configs/specific_configs/validate', methods=['POST'])
def validate_specific_config():
    if not request.json:
        abort(400)
    else:
        data = request.json
    return "INCOMMING"


@mod.route('/configs/specific_configs/recommend', methods=['GET'])
def get_recommend_config():
    if not (request.args.get('config_key') and request.args.get('config_value')):
        abort(400)

    return "INCOMMING"


@mod.route('/configs/specific_configs/submit', methods=['POST'])
def submit_configs():
    if not request.json:
        abort(400)
    else:
        data = request.json
    return "INCOMMING"


@mod_v1.route('/configs/specific_configs', methods=['GET', 'POST', 'PUT'])
class Specific_Configs(Resource):
    def get(self):
        return {"status": "Got new data"}

    def post(self):
        return {"status": "Posted new data"}

    def put(self):
        return {"status": "Posted new data"}


@mod.route('/configs', methods=['GET'])
def submit_configsdasdad():
    return render_template('form_bk.html')


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField
from wtforms.validators import DataRequired, Email, Length
import oyaml as yaml
import sys
from flask import Response

import global_assets.const as CONST




ALLOWED_EXTENSIONS = set(['yml', 'yaml'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


import os
from flask import send_file

from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename


@mod_v1.route('/tools/list_ansible_group_vars', methods=['GET', 'POST'])
class Ansible_Group_Vars(Resource):
    def get(self):
        # print(request.args.get('lamtv19'))
        if request.args.get('download') == 'yes' and request.args.get('group') and request.args.get('filename'):
            file_path = CONST.ansible_group_vars_dir + '/' + request.args.get('group') + '/' + request.args.get(
                'filename')
            if os.path.isfile(file_path):
                return send_file(file_path, as_attachment=True, cache_timeout=0)
            else:
                abort(404, 'No such file ' + file_path)
        with open('static/role_service.json') as role_data_file:
            role_data = json.load(role_data_file)
        result = OrderedDict()

        list_roles = role_data.keys()
        list_roles.sort()
        for role in list_roles:
            result[role] = []
            list_node_role = session.query(models.Node_role).filter_by(role_name=role).all()
            for node_role in list_node_role:
                node = session.query(models.Node).filter_by(node_id=node_role.node_id).first()
                result[role].append({"node_id": node.node_id, "node_display_name": node.node_display_name,
                                     "management_ip": node.management_ip})

        session.commit()

        # print(role_data.keys())

        res = OrderedDict()

        res["data"] = result

        group_var_dir = CONST.ansible_group_vars_dir
        list_group = [o for o in os.listdir(group_var_dir) if os.path.isdir(os.path.join(group_var_dir, o))]

        list_role_configs = []
        for role in list_group:
            role_configs = OrderedDict()
            role_configs['name'] = role
            role_configs['configs'] = []

            list_file = [o for o in os.listdir(group_var_dir + '/' + role) if
                         os.path.isfile(os.path.join(group_var_dir + '/' + role, o))]
            for filename in list_file:
                role_configs['configs'].append({
                    'filename': filename,
                    'file_path': group_var_dir + '/' + role + '/' + filename,
                    'link_to_edit': '/tools/edit_ansible_group_vars' + '?group=' + role + '&filename=' + filename})
            list_role_configs.append(role_configs)
        res["list_roles_and_configs"] = list_role_configs

        return Response(
            render_template('list_ansible_group_vars.html', data=res["data"], list_group=res["list_roles_and_configs"]), 200, mimetype='text/html')

    def post(self):
        if not request.json:
            abort(400)
        reset_ansible_group_vars = request.json.get('reset_ansible_group_vars')
        if not reset_ansible_group_vars:
            abort(400, 'reset_ansible_group_vars must be True')
        template_dir = CONST.ansible_group_vars_template_dir
        sf_dir = CONST.ansible_group_vars_sf_dir
        group_var_dir = CONST.ansible_group_vars_dir
        reset_all = request.json.get('reset_all')
        if reset_all is True:
            os.system(' \cp -r  ' + template_dir + '/*' + ' ' + group_var_dir)
            os.system(' \cp -r  ' + template_dir + '/*' + ' ' + sf_dir)
            list_group = [o for o in os.listdir(group_var_dir) if os.path.isdir(os.path.join(group_var_dir, o))]
            for group in list_group:
                list_file = [o for o in os.listdir(group_var_dir + '/' + group) if
                             os.path.isfile(os.path.join(group_var_dir + '/' + group, o))]
                for filename in list_file:
                    origin_data = load_yml_file(group_var_dir+ '/' + group + '/'+filename)
                    convert_original_to_input_sf(origin_data, sf_dir+ '/' + group + '/'+filename)

            return {"response": 'Reset All Group_vars sucessfully. Check Result in /tools/edit_ansible_group_vars'}, 200

        role_name = request.json.get('role_name')
        filename = request.json.get('filename')

        template_file = template_dir + '/' + role_name + '/' + filename
        if not os.path.isfile(template_file):
            return abort(404, 'No such File ' + template_file)

        group_var_file = group_var_dir + '/' + role_name + '/' + filename
        os.system('mkdir -p ' + group_var_dir + '/' + role_name)
        os.system('mkdir -p ' + sf_dir + '/' + role_name)

        os.system(' \cp -r  ' + template_file + ' ' + group_var_file)
        origin_data = load_yml_file(group_var_file)
        convert_original_to_input_sf(origin_data, sf_dir  + '/' + role_name + '/' + filename)
        return {
                   "response": 'Reset Group_vars ' + group_var_file + ' sucessfully. Check Result in /tools/edit_ansible_group_vars'}, 200


@mod_v1.route('/tools/edit_ansible_group_vars', methods=['GET', 'POST'])
class FORM_INSERT(Resource):
    def get(self):
        if not request.args.get('group') or not request.args.get('filename'):
            return abort(400, 'Need Group and FileName')

        sf_dir = CONST.ansible_group_vars_sf_dir
        group_var_dir = CONST.ansible_group_vars_dir

        args = request.args
        file_path = group_var_dir + '/' + request.args.get('group') + '/' + request.args.get('filename')
        if not os.path.isfile(file_path):
            return abort(404, 'No such file ' + file_path)
        else:

            origin_data = load_yml_file(file_path)
            os.system('mkdir -p ' + sf_dir + '/' + request.args.get('group'))
            sf_file_path = sf_dir + '/' + request.args.get('group') + '/' + request.args.get('filename')
            if not os.path.isfile(sf_file_path):
                os.system('rm -rf ' + sf_file_path)
                convert_original_to_input_sf(origin_data, sf_file_path)
            sf_data = load_yml_file(sf_file_path)
            return Response(
                render_template('form_edit_ansible_group_vars.html', my_data=sf_data, group=request.args.get('group'),
                                filename=request.args.get('filename')), 200, mimetype='text/html')

    def post(self):
        res = request.form.to_dict()
        # print(res.keys())
        list_keys = res.keys()
        list_keys.remove('submit')
        group_var_dir = CONST.ansible_group_vars_dir
        sf_dir = CONST.ansible_group_vars_sf_dir

        file_path = group_var_dir + '/' + request.args.get('group') + '/' + request.args.get('filename')
        sf_file_path = sf_dir + '/' + request.args.get('group') + '/' + request.args.get('filename')
        data = load_yml_file(sf_file_path)
        for gr_data in data:
            for config in gr_data['configs']:
                if config['input_type'] == 'checkbox':
                    config['ex_value'] = False
        for key in list_keys:
            group_key = key.split("###")[0]
            # print(group_key)
            key_name = key.split("###")[1]
            value = res[key]
            for gr_data in data:
                if gr_data['name'] == group_key:
                    for config in gr_data['configs']:
                        if config['key'] == key_name:
                            if config['input_type'] == 'number':
                                config['ex_value'] = int(value)
                            elif config['input_type'] == 'checkbox':
                                # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx" + str(value))
                                config['ex_value'] = True if value.encode('utf-8') == 'on' else False
                            else:
                                config['ex_value'] = value.encode('utf-8')

        stream = file(sf_file_path, 'w')
        yaml.dump(data, stream)
        convert_input_sf_to_origin(data, file_path)

        flash('Edit  Group_vars ' + file_path + ' sucessfully. Check Result in /tools/edit_ansible_group_vars?'+'group='+request.args.get('group')+'&filename='+request.args.get('filename'))
        return redirect('/tools/list_ansible_group_vars')







@mod.route('/tools/', methods=['GET'])
def get_tools():
    list_tools = [
        {'label': 'cnv_group_var_origin_to_sf', 'url': '/tools/cnv_group_var_origin_to_sf'},
        {'label': 'cnv_group_var_sf_to_origin', 'url': '/tools/cnv_group_var_sf_to_origin'},
        {'label': 'convert_ansible_task_yml_to_sf_task_yml', 'url': '/tools/convert_ansible_task_yml_to_sf_task_yml'},
        {'label': 'edit_ansible_group_vars', 'url': '/tools/list_ansible_group_vars'}]
    return render_template('tools.html', list_tools=list_tools)
@mod.route('/api/v1/tools/', methods=['GET'])
def get_tools_v1():

    return redirect('/tools')


@mod_v1.route('/tools/cnv_group_var_origin_to_sf', methods=['GET', 'POST'])
class CNV_Group_Var_1(Resource):
    def get(self):
        tool_name = 'Tool chuyen doi file group_var_origin dung trong Ansible sang file group_var dung trong API SoftwareManagement'
        tool_url = "/tools/cnv_group_var_origin_to_sf"
        return Response(render_template('convert_tool.html', tool_name=tool_name, tool_url=tool_url), 200,
                        mimetype='text/html')

    def post(self):
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            flash('File successfully uploaded' + ' ' + filename)
            file.save(CONST.tools_dir + '/cnv_group_var_origin_to_sf_input.yml')
            data = load_yml_file(CONST.tools_dir + '/cnv_group_var_origin_to_sf_input.yml')
            convert_original_to_input_sf(data,
                                         CONST.tools_dir + '/' + filename + '__cnv_group_var_origin_to_sf_output.yml')

            # print(CONST.tools_dir+'/cnv_group_var_origin_to_sf_input.yml')
            # return redirect('/tools/cnv_group_var_sf_to_origin')
            return send_file(CONST.tools_dir + '/' + filename + '__cnv_group_var_origin_to_sf_output.yml',
                             as_attachment=True, cache_timeout=0)
        else:
            flash('Allowed file types are yml, yaml')
            return redirect(request.url)


@mod_v1.route('/tools/cnv_group_var_sf_to_origin', methods=['GET', 'POST'])
class CNV_Group_Var_2(Resource):
    def get(self):
        tool_name = 'Tool chuyen doi file group_var dung trong API SoftwareManagement sang file group_var origin dung trong Ansible'
        tool_url = "/tools/cnv_group_var_sf_to_origin"
        return Response(render_template('convert_tool.html', tool_name=tool_name, tool_url=tool_url), 200,
                        mimetype='text/html')

    def post(self):
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            flash('File successfully uploaded' + ' ' + filename)
            file.save(CONST.tools_dir + '/cnv_group_var_sf_to_origin_input.yml')
            data = load_yml_file(CONST.tools_dir + '/cnv_group_var_sf_to_origin_input.yml')
            convert_input_sf_to_origin(data,
                                       CONST.tools_dir + '/' + filename + '__cnv_group_var_sf_to_origin_output.yml')

            # print(CONST.tools_dir+'/cnv_group_var_origin_to_sf_input.yml')
            # return redirect('/tools/cnv_group_var_sf_to_origin')
            return send_file(CONST.tools_dir + '/' + filename + '__cnv_group_var_sf_to_origin_output.yml',
                             as_attachment=True, cache_timeout=0)
        else:
            flash('Allowed file types are yml, yaml')
            return redirect(request.url)


@mod_v1.route('/tools/convert_ansible_task_yml_to_sf_task_yml', methods=['GET', 'POST'])
class CNV_Group_Var_3(Resource):
    def get(self):
        tool_name = 'Tool chuyen doi file ansible task main yml dung trong Ansible sang file task main yml dung trong API SoftwareManagement'
        tool_url = "/tools/convert_ansible_task_yml_to_sf_task_yml"
        return Response(render_template('convert_tool.html', tool_name=tool_name, tool_url=tool_url), 200,
                        mimetype='text/html')

    def post(self):
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            flash('File successfully uploaded' + ' ' + filename)
            file.save(CONST.tools_dir + '/convert_ansible_task_yml_to_sf_task_yml_input.yml')
            data = load_yml_file(CONST.tools_dir + '/convert_ansible_task_yml_to_sf_task_yml_input.yml')
            convert_ansible_task_yml_to_sf_task_yml(data,
                                                    CONST.tools_dir + '/' + filename + '__convert_ansible_task_yml_to_sf_task_yml_output.yml')

            # print(CONST.tools_dir+'/cnv_group_var_origin_to_sf_input.yml')
            # return redirect('/tools/cnv_group_var_sf_to_origin')
            return send_file(CONST.tools_dir + '/' + filename + '__convert_ansible_task_yml_to_sf_task_yml_output.yml',
                             as_attachment=True, cache_timeout=0)
        else:
            flash('Allowed file types are yml, yaml')
            return redirect(request.url)
