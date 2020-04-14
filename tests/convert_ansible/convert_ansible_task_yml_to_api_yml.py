
import time
import requests

import os
import json
import oyaml as yaml
from yaml.resolver import Resolver
import re



yaml.preserve_quotes = True  # not necessary for your current input
from collections import OrderedDict

def load_yml_file(file_path):
    # remove resolver entries for On/Off/Yes/No
    for ch in "OoYyNn":
        if Resolver.yaml_implicit_resolvers.get(ch):
            if len(Resolver.yaml_implicit_resolvers[ch]) == 1:
                del Resolver.yaml_implicit_resolvers[ch]
            else:
                Resolver.yaml_implicit_resolvers[ch] = [x for x in
                                                        Resolver.yaml_implicit_resolvers[ch] if
                                                        x[0] != 'tag:yaml.org,2002:bool']
    with open(file_path) as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        result = yaml.load(file, Loader=yaml.FullLoader)

        #print(type(list_task))
    return result


if __name__ == "__main__":
    example_tasks = load_yml_file('./example.yml')[0]
    print(example_tasks)

    list_input_tasks = load_yml_file('./init_repo.yml')
    list_output_tasks = []
    for index, input_task in enumerate(list_input_tasks, start=1):
        input_task['register'] = 'infos'

        output_task = OrderedDict()
        output_task['name']= str(index)+"."+input_task['name']
        output_task['block'] = []
        output_task['block'].append(OrderedDict([('include', 'extends/before.yml task_index='+str(index))]))
        input_task.pop('name')
        output_task['block'].append(input_task)
        output_task['block'].append(OrderedDict([('include', 'extends/after_ok.yml task_index='+str(index)+' info={{ infos  }}')]))
        output_task['rescue'] = [OrderedDict([('include', 'extends/after_failse.yml task_index='+str(index)+' info={{ infos  }}')])]
        output_task['tags']=['install',str(index)]
        list_output_tasks.append(output_task)


    print("lamtv10")
    with open('results.yml', 'w') as yaml_file:

        yaml.dump(list_output_tasks, yaml_file)
