
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


def convert_file(file_path):
    list_input_tasks = load_yml_file(file_path)
    list_output_tasks = []
    for index, input_task in enumerate(list_input_tasks, start=1):
        input_task['register'] = 'infos'
        name_output_task =  OrderedDict()
        name_output_task['name'] = str(index) + "." + input_task['name']
        name_output_task['debug'] = 'msg=\'Starting ' + str(index) + "----------------------------------------------->\'"
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
    with open(file_path+'results.yml', 'w') as yaml_file:

        yaml.dump(list_output_tasks, yaml_file)


if __name__ == "__main__":
    # example_tasks = load_yml_file('./example.yml')[0]
    # print(example_tasks)

    convert_file('nova_compute_task.yml')

"""
\cp init_repo/tasks/main.yml ceph/tasks/main.yml
\cp init_repo/tasks/main.yml chrony/tasks/main.yml
\cp init_repo/tasks/main.yml cinder-api/tasks/main.yml
\cp init_repo/tasks/main.yml cinder-volume/tasks/main.yml
\cp init_repo/tasks/main.yml docker/tasks/main.yml
\cp init_repo/tasks/main.yml elasticsearch/tasks/main.yml
\cp init_repo/tasks/main.yml fluentd/tasks/main.yml
\cp init_repo/tasks/main.yml glance-api/tasks/main.yml
\cp init_repo/tasks/main.yml haproxy/tasks/main.yml
\cp init_repo/tasks/main.yml horizon/tasks/main.yml
\cp init_repo/tasks/main.yml init_repo/tasks/main.yml
\cp init_repo/tasks/main.yml keepalived/tasks/main.yml
\cp init_repo/tasks/main.yml keystone/tasks/main.yml
\cp init_repo/tasks/main.yml kibana/tasks/main.yml
\cp init_repo/tasks/main.yml memcached/tasks/main.yml
\cp init_repo/tasks/main.yml neutron-dhcp_agent/tasks/main.yml
\cp init_repo/tasks/main.yml neutron-metadata_agent/tasks/main.yml
\cp init_repo/tasks/main.yml neutron-openvswitch_agent/tasks/main.yml
\cp init_repo/tasks/main.yml neutron-server/tasks/main.yml
\cp init_repo/tasks/main.yml neutron-sriov_agent/tasks/main.yml
\cp init_repo/tasks/main.yml nova-api/tasks/main.yml
\cp init_repo/tasks/main.yml nova-compute/tasks/main.yml
\cp init_repo/tasks/main.yml openday_light/tasks/main.yml
\cp init_repo/tasks/main.yml openvswitch_dpdk/tasks/main.yml
\cp init_repo/tasks/main.yml percona_xtra_db_cluster/tasks/main.yml
\cp init_repo/tasks/main.yml prometheus/tasks/main.yml
\cp init_repo/tasks/main.yml qemu/tasks/main.yml
\cp init_repo/tasks/main.yml rabbitmq/tasks/main.yml
\cp init_repo/tasks/main.yml swift_proxy/tasks/main.yml
\cp init_repo/tasks/main.yml test_ansible_command/tasks/main.yml

"""