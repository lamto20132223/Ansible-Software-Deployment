#https://docs.sqlalchemy.org/en/13/core/type_basics.html
from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime

import sqlalchemy as db 
import json

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Node(Base):
    __tablename__ = 'nodes'
    node_id = Column(Integer,primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    management_id = Column(String(45))
    ssh_user = Column(String(45))
    ssh_password = Column(String(45))
    status = Column(Text)
    node_display_name = Column(String(45))
    node_info_id = Column(String(45))
    deployment_id = Column(Integer)
    role_type = Column(String(45))
    def __repr__(self):
    	return "<Node(created_at='%s',updated_at='%s',deleted_at='%s',management_id='%s',ssh_user='%s',ssh_password='%s',status='%s',node_display_name='%s',node_info_id='%s',deployment_id='%s',created_at='%s')>" %(self.created_at,self.updated_at,self.deleted_at,self.management_id,self.ssh_user,self.ssh_password,self.status,self.node_display_name,self.node_info_id,self.deployment_id,self.role_type) 





CONF = {"database":{"connection":"mysql+pymysql://lamtv10:lamtv10@172.16.29.198/lamtv10"}}
db_engine = db.create_engine(CONF["database"]["connection"])
db_connection = db_engine.connect()
db_metadata = db.MetaData()
db_nodes = db.Table('nodes', db_metadata, autoload=True, autoload_with=db_engine)

result = db_connection.execute("select * from nodes")
print(result)

#db_connection.execute(db_nodes.insert(), {"id: "})

Session = sessionmaker()
Session.configure(bind=db_engine) 
session = Session()

node1 = Node(node_id=111,created_at=datetime(2015, 6, 5, 8, 10, 10, 10),updated_at=datetime(2015, 6, 5, 8, 10, 10, 10),deleted_at=datetime(2015, 6, 5, 8, 10, 10, 10),management_id="172.16.29.194", ssh_user="root", ssh_password="123456aA@", status="INIT", node_display_name="test1")

session.add(node1)
session.commit()
our_node = session.query(Node).filter_by(node_display_name='test1').first() 
print(our_node)


