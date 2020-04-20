from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import oyaml as yaml
import sys, os
from collections import OrderedDict
from global_assets.common import *
import json



def convert_original_to_input_sf(data, output_file):


    # data = {"ok":"ok"}
    print(data.keys())

    output = []
    default_group = OrderedDict()
    default_group['name'] = 'DEFAULT'
    default_group['configs'] = []
    output.append(default_group)
    for key in data.keys():
        if type(data[key]) is OrderedDict:
            new_group = OrderedDict()
            new_group['name'] = key
            new_group['configs'] = []
            for config in data[key].keys():
                config_data = OrderedDict()
                config_data['key'] = config
                config_data['ex_value'] = data[key][config]
                config_data['required'] = False
                config_data['editable'] = True
                config_data['need_edit'] = False
                config_data['input_type'] = 'text'
                if type(config_data['ex_value']) is int:
                    config_data['input_type'] = 'number'
                if type(config_data['ex_value']) is bool:
                    config_data['input_type'] = 'checkbox'
                new_group['configs'].append(config_data)
            output.append(new_group)
        else:
            config_data=OrderedDict()
            config_data['key'] = key
            config_data['ex_value'] = data[key]
            config_data['required'] = False
            config_data['editable'] = True
            config_data['need_edit'] = False
            config_data['input_type'] = 'text'
            if type(config_data['ex_value']) is int:
                config_data['input_type'] = 'number'
            if type(config_data['ex_value']) is bool:
                config_data['input_type'] = 'checkbox'
            default_group['configs'].append(config_data)


    stream = file(output_file, 'w')
    print(data)
    yaml.dump(output, stream)
def convert_input_sf_to_origin(data, output_file):
    output = OrderedDict()
    for group_data in data:
        if group_data['name']=='DEFAULT':
            for config in group_data['configs']:
                key = config['key']
                value = config['ex_value']
                output[key] =value
        else :
            output[group_data['name']] = OrderedDict()
            for config in group_data['configs']:
                key = config['key']
                value = config['ex_value']
                output[group_data['name']][key] = value
    stream = file(output_file, 'w')
    # print(data)
    yaml.dump(output, stream)



def convert_ansible_task_yml_to_sf_task_yml(data, output_file):
    list_input_tasks = data
    list_output_tasks = []
    for index, input_task in enumerate(list_input_tasks, start=1):
        input_task['register'] = 'infos'
        name_output_task =  OrderedDict()
        name_output_task['name'] = str(index) + "." + input_task['name']
        name_output_task['debug'] = 'msg=\'Starting ' + str(index) + "-------------------------------------------->\'"
        input_task.pop('name')

        output_task = OrderedDict()
        output_task['block'] = []
        output_task['block'].append(name_output_task)
        output_task['block'].append(OrderedDict([('include', 'extends/before.yml task_index='+str(index))]))
        output_task['block'].append(input_task)
        output_task['block'].append(OrderedDict([('include', 'extends/after_ok.yml task_index='+str(index)+' info={{ infos  }}')]))
        output_task['rescue'] =[]
        output_task['rescue'].append(OrderedDict([('include', 'extends/after_failse.yml task_index='+str(index)+' info={{ infos  }}')]))
        output_task['rescue'].append(OrderedDict([('fail', 'msg={{ infos  }}')]))
        output_task['tags']=['install',str(index)]
        list_output_tasks.append(output_task)



    print("lamtv10")
    with open(output_file, 'w') as yaml_file:

        yaml.dump(list_output_tasks, yaml_file)