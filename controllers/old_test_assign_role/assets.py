from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
import json

list_roles=['CONTROLLER', 'COMPUTE', 'CEPTH','SWIFT']

print(os.path.exists('static/role_service.json'))

with open('./static/role_service.json') as role_service_file:
    data = json.load(role_service_file)
    print(data)