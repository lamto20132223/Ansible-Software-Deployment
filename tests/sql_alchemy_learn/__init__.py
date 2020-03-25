from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import json
from flask_restplus import Api, Resource, fields
app = Flask(__name__)
api=Api(app)

app.config.from_object(Config)
db = SQLAlchemy(app)
session = db.session
Node_Base = db.Model
Column = db.Column
relationship = db.relationship
import uuid


def generate_uuid():
    return str(uuid.uuid4())


migrate = Migrate(app, db)

from sql_alchemy_learn import models




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






if __name__ == "__main__":

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
    app.run(debug=True,host="0.0.0.0", port=4321)



