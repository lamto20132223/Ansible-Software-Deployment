import os,sys

from flask import Flask
from configs.conf_dev import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import json

import importlib
from flask_restplus import Api, Resource, fields
import logging
import logging.config
ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
log_config_dir = os.path.join(ROOT_DIR, 'configs/logging.conf')
logging.config.fileConfig(log_config_dir, disable_existing_loggers=False)


app = Flask(__name__)
api=Api(app)


# FOR DEV TEST ONLY
app.config.from_object(Config)

lamtv10="tovanlam"



# def connect_database():
db = SQLAlchemy(app)
ma = Marshmallow(app)
session = db.session
Node_Base = db.Model
# Node_Base.metadata.create_all(db)
Column = db.Column
relationship = db.relationship


# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     session.remove()


#
#
# migrate = Migrate(app, db)
#
import models
from utils import ansible



#
#
#
#
def _test_add_nodes_b1():
    print("sdfsdfs")

    # node1 = Node(created_at=datetime.now(), updated_at=datetime.now(), deleted_at=None, management_ip="172.16.29.193", ssh_user="root", ssh_password="123456@Epc", status="set_ip", node_display_name="controller_01")
    node2 = models.Node(created_at=datetime.now(), updated_at=datetime.now(), deleted_at=None,
                        management_ip="172.16.29.194", ssh_user="root", ssh_password="123456@Epc", status="set_ip",
                        node_display_name="controller_02")
    node3 = models.Node(created_at=datetime.now(), updated_at=datetime.now(), deleted_at=None,
                        management_ip="172.16.29.195", ssh_user="root", ssh_password="123456@Epc", status="set_ip",
                        node_display_name="controller_03")

    # node_info  = Node_info(node_name="tovanlam1", memory_mb=123)
    # session.add(node1)
    session.add(node2)
    session.add(node3)

    session.commit()
    print("OK")
def add_deployment_to_node():
    nodes = session.query(models.Node).all()
    print("lamtv10")
    print(len(nodes))
    for node in  nodes:
        print(node)
        deployment=models.Deployment(created_at=datetime.now(),updated_at=datetime.now(), finished_at=None, status='Init', name='deployment_'+ str(node.node_display_name) , progress='Init')
        node.deployment=deployment
        session.add(node)
        session.commit()





def register_all_module_controller():
    d ='./controllers'

    list_dir = [o for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]
    print(list_dir)
    for module in list_dir:
        module_page = importlib.import_module('controllers.'+str(module))
        app.register_blueprint(module_page.mod)

def register_module(module_name, url_prefix=None):
    module_page = importlib.import_module('controllers.' + str(module_name))

    if url_prefix is None:
        app.register_blueprint(module_page.mod)
    else:
        app.register_blueprint(module_page.mod, url_prefix=url_prefix)


if __name__ == "__main__":
    # runner = ansible.Runner('ansible_compute.yml', 'multnode',
    #                         {'extra_vars': {'target': "ta1"}, 'tags': ['install', 'uninstall']}, None, False, None,
    #                         None, None)
    # stats = runner.run()
    # ansible.print_stats(stats)
    #
    # runner2 = ansible.Runner('ansible_compute.yml', 'multnode',
    #                          {'extra_vars': {'target': "ta2"}, 'tags': ['install', 'uninstall']}, None, False, None,
    #                          None, None)
    # stats2 = runner2.run()
    # ansible.print_stats(stats2)

    register_module("demo")
    register_module("test_thread")
    register_module("discovery_node_test",'/api/v1')
    register_module("test_api")
    register_module("assign_role",'/api/v1')
    register_module("insert_specific_config", "/api/v1")
    register_module("start_undo_pause_next", "/api/v1")
    register_module("scallingup_scallingdown","/api/v1")
    register_module("replace_controller", "/api/v1")
    register_module("gen_template", "/api/v1")
    register_module("get_recommend", "/api/v1")
    register_module("management_file_config", "/api/v1")
    register_module("change_password","/api/v1" )


    print("FFFFF")
    #test_add_nodes_b1()
    #add_deployment_to_node()

    print("lamtv10")


    @app.route("/hello")
    def home():
        return "Hello World!"


    @app.route('/index')
    def index():
        return "Hello, World!"


    @app.route('/nodes')
    def get():
        nodes = session.query(models.Node).all()
        print(nodes[0].__dict__)

        return {'result' : str(nodes)}, 201
    app.logger.addHandler(logging.handlers)
    app.run(debug=True,host="0.0.0.0", port=4321)


