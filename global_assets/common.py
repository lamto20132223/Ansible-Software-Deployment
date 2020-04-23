from app import  db, session, Node_Base, Column, relationship, ansible
from datetime import  datetime
import  models
import os
import json
import oyaml as yaml
import global_assets.const as CONST

from yaml.resolver import Resolver

def get_service_setups_from_deployment(deployment):
    def sort_function(e):
        return e.setup_index

    service_setups = deployment.service_setups
    service_setups.sort(key=sort_function)
    return service_setups

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

