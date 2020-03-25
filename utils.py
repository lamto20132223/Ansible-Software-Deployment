import uuid
import json
from uuid import uuid4
# from sqlalchemy.ext.declarative import declarative_base
# Node_Base = declarative_base()

# class BinaryUUID(TypeDecorator):
#     impl = BINARY(16)
    
#     def process_bind_param(self, value, dialect):
#         try:
#             return value.bytes
#         except AttributeError:
#             try:
#                 return uuid.UUID(value).bytes
#             except TypeError:
#                 return value
                
#     def process_result_value(self, value, dialect):
#         return uuid.UUID(bytes=value)

def generate_uuid():
    return str(uuid.uuid4())


#### 
with open('configs/conf.json') as json_file:
    global_conf = json.load(json_file)

from libs import ansible