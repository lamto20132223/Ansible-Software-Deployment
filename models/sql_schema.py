from models import  *

class ChangeSchema(ma.ModelSchema):
    class Meta:
        model=Change

class DeploymentSchema(ma.ModelSchema):
    class Meta:
        model=Deployment

class Disk_resourceSchema(ma.ModelSchema):
    class Meta:
        model=Disk_resource

class File_configSchema(ma.ModelSchema):
    class Meta:
        model=File_config

class Interface_resourceSchema(ma.ModelSchema):
    class Meta:
        model=Interface_resource

class NodeSchema(ma.ModelSchema):
    class Meta:
        model=Node

class Node_infoSchema(ma.ModelSchema):
    class Meta:
        model=Node_info

class Node_roleSchema(ma.ModelSchema):
    class Meta:
        model=Node_role

class Openstack_configSchema(ma.ModelSchema):
    class Meta:
        model=Openstack_config

class PasswordSchema(ma.ModelSchema):
    class Meta:
        model=Password

class Service_infoSchema(ma.ModelSchema):
    class Meta:
        model=Service_info

class Service_info_File_configSchema(ma.ModelSchema):
    class Meta:
        model=Service_info_File_config

class Service_setupSchema(ma.ModelSchema):
    class Meta:
        model=Service_setup

class TaskSchema(ma.ModelSchema):
    class Meta:
        model=Task

class UpdateSchema(ma.ModelSchema):
    class Meta:
        model=Update

class Update_changeSchema(ma.ModelSchema):
    class Meta:
        model=Update_change



def to_json(querey_data, type_data, many):
    if type_data=='Change':
        return ChangeSchema(many=many).dump(querey_data).data
    elif  type_data=='Deployment':
        return DeploymentSchema(many=many).dump(querey_data).data
    elif  type_data=='Disk_resource':
        return Disk_resourceSchema(many=many).dump(querey_data).data
    elif  type_data=='File_config':
        return File_configSchema(many=many).dump(querey_data).data
    elif  type_data=='Interface_resource':
        return Interface_resourceSchema(many=many).dump(querey_data).data
    elif  type_data=='Node':
        return NodeSchema(many=many).dump(querey_data).data
    elif  type_data=='Node_info':
        return Node_infoSchema(many=many).dump(querey_data).data
    elif  type_data=='Node_role':
        return Node_roleSchema(many=many).dump(querey_data).data
    elif  type_data=='Openstack_config':
        return Openstack_configSchema(many=many).dump(querey_data).data
    elif  type_data=='Password':
        return PasswordSchema(many=many).dump(querey_data).data
    elif  type_data=='Service_info':
        return Service_infoSchema(many=many).dump(querey_data).data
    elif  type_data=='Service_info_File_config':
        return Service_info_File_configSchema(many=many).dump(querey_data).data
    elif  type_data=='Service_setup':
        return Service_setupSchema(many=many).dump(querey_data).data
    elif  type_data=='Task':
        return TaskSchema(many=many).dump(querey_data).data
    elif  type_data=='Update':
        return UpdateSchema(many=many).dump(querey_data).data
    elif  type_data=='Update_change':
        return Update_changeSchema(many=many).dump(querey_data).data
    else:
        return {'ok': 'ok'}