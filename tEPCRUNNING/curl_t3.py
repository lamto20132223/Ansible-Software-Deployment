import os
#
#
#

import time
import requests

##task = [task for task in tasks if task['id'] == task_id]


#### **************************  example *********************************************
#curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks
# #curl -X POST "http://172.16.29.194:9876/language" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"file\": \"docker.io/istio/sidecar_injector:1.4.4\"}"

##***************** add_host ************************

def send_task_info():
    os.system(
        'curl -X POST "http://172.16.29.194:4321/api/v1/tasks/update_task" -H  "accept: application/json" -H  "Content-Type: application/json" --data   @task_info.json ')

def update_host():
    os.system(
        'curl -X POST "http://172.16.29.194:4321/api/v1/hosts/update_host" -H  "accept: application/json" -H  "Content-Type: application/json" --data @nodes.json')

def add_host():
    for i in range(18)[1:]:
        os.system(
            'curl -X POST "http://172.16.29.194:4321/api/v1/hosts/add_host" -H  "accept: application/json" -H  "Content-Type: application/json" --data @nodes'+str(i)+'.json')
        time.sleep(1)


##***************************** discover_hosts *********************************************
def discover_hosts():
    # os.system('curl -X POST "http://172.16.29.194:4321/api/v1/hosts/discover_hosts_v1" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
    # time.sleep(5)

    os.system('curl -X POST "http://172.16.29.194:4321/api/v1/hosts/discover_hosts" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
    time.sleep(5)


###*******************************add_host_to_role *******************************************************
def add_host_to_role():
    for i in range(18)[1:]:
        os.system('curl -X POST "http://172.16.29.194:4321/api/v1/roles/add_host_to_role" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role'+str(i)+'.json')
        time.sleep(5)

def insert_test_data():
    os.system('curl -X POST "http://172.16.29.194:4321/api/v1/roles/test_create_deployment" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
    time.sleep(5)

    os.system('curl -X POST "http://172.16.29.194:4321/api/v1/roles/test_create_service_setup" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
    time.sleep(5)
    os.system('curl -X POST "http://172.16.29.194:4321/api/v1/roles/test_create_ansible_inventory_with_role" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
    time.sleep(5)

    os.system('curl -X POST "http://172.16.29.194:4321/api/v1/roles/test_create_ansible_playbook" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
    time.sleep(5)



    os.system('curl -X POST "http://172.16.29.194:4321/api/v1/roles/test_create_task" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
    time.sleep(5)


# http://0.0.0.0:4321/api/v1/roles/test_code
# http://0.0.0.0:4321/api/v1/roles/test_code2
# http://0.0.0.0:4321/api/v1/roles/test_code3


#os.system('curl -X GET "http://127.0.0.1:4321/api/v1/hosts/host_info?host_id=154"')

# // {"node_id":"175", "roles": ["CONTROLLER"]}
# //{"node_id":"177", "roles": ["COMPUTE"]}
# //{"node_id":"179", "roles": ["COMPUTE"]}
# //{"node_id":"181", "roles": ["CEPH"]}



#{"management_ip":"172.16.29.23", "ssh_user":"root", "ssh_password":"Vttek@123", "node_display_name":"controller"}
#{"management_ip":"172.16.29.27", "ssh_user":"root", "ssh_password":"Vttek@123", "node_display_name":"compute01"}
#{"management_ip":"172.16.29.41", "ssh_user":"root", "ssh_password":"Vttek@123", "node_display_name":"compute02"}
#{"management_ip":"172.16.29.43", "ssh_user":"root", "ssh_password":"Vttek@123", "node_display_name":"ceph"}

def delete_data():
    os.system(
        'curl -X POST "http://172.16.29.194:4321/api/v1/clean_data" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')


def run_one_task():
    os.system('curl -X POST "http://172.16.29.194:4321/api/v1/roles/test_run_first_ansble_playbook" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
    time.sleep(5)

def run_task_id(task_id):

    url = 'http://172.16.29.194:4321/api/v1/installation/runtask'
    payload = {'task_id':task_id,'method':'Install'}
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, json=payload, headers=headers)
    print(r.text)
    # os.system('curl -X POST "http://172.16.29.194:4321/api/v1/installation/runtask" -H  "accept: application/json" -H  "Content-Type: application/json"  --data "{\'task_id\':\'1\',\'method\':\'Install\' }"')
    time.sleep(5)

def run_service_setup(deployment_id, setup_index):

    url = 'http://172.16.29.194:4321/api/v1/installation/run_service_setup'
    payload = {'deployment_id':deployment_id,'setup_index':setup_index,  'method':'Install'}
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, json=payload, headers=headers)
    print(r.text)
    # os.system('curl -X POST "http://172.16.29.194:4321/api/v1/installation/runtask" -H  "accept: application/json" -H  "Content-Type: application/json"  --data "{\'task_id\':\'1\',\'method\':\'Install\' }"')
    time.sleep(5)


def run_service_set_up_start_at_task(deployment_id, setup_index, start_at_task_id):

    url = 'http://172.16.29.194:4321/api/v1/installation/run_service_setup'
    payload = {'deployment_id':deployment_id,'setup_index':setup_index,  'method':'Install','start_at_task_id':start_at_task_id}
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, json=payload, headers=headers)
    print(r.text)
    # os.system('curl -X POST "http://172.16.29.194:4321/api/v1/installation/runtask" -H  "accept: application/json" -H  "Content-Type: application/json"  --data "{\'task_id\':\'1\',\'method\':\'Install\' }"')
    time.sleep(5)

def run_deployment(deployment_id, service_setup_id):
    url = 'http://172.16.29.194:4321/api/v1/installation/run_deployment'
    payload = {'deployment_id':deployment_id,'service_setup_id':service_setup_id,  'method':'Install'}
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, json=payload, headers=headers)
    print(r.text)
    # os.system('curl -X POST "http://172.16.29.194:4321/api/v1/installation/runtask" -H  "accept: application/json" -H  "Content-Type: application/json"  --data "{\'task_id\':\'1\',\'method\':\'Install\' }"')
    time.sleep(5)
def create_ansible_group_var():

    url = 'http://172.16.29.194:4321/tools/list_ansible_group_vars'
    payload = {'reset_ansible_group_vars': True, 'reset_all': True}
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, json=payload, headers=headers)
    print(r.text)

    time.sleep(5)


def add_service_setup_to_node( node_id,  service_setup_name):
    url = 'http://172.16.29.194:4321/api/v1/service_setups/add_service_setup_to_node'


    payload = {'node_id': node_id, 'service_setup_name': service_setup_name}
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, json=payload, headers=headers)
    print(r.text)

    time.sleep(5)



if __name__ == "__main__":
    # delete_data()
    add_host()
    #update_host()
    discover_hosts()
    add_host_to_role()
    insert_test_data()
    create_ansible_group_var()

#    add_service_setup_to_node(2, "openvswitch_dpdk")

    #send_task_info()
    #run_one_task(
    # )
    # run_task_id(1)
    # run_task_id(2)
    # run_task_id(3)
    # run_task_id(4)
    # run_task_id(5)
    # run_task_id(6)
    # run_task_id(7)
    #
    #run_service_set_up_start_at_task(1,1,8)
    # run_service_setup(1, 3)
    #run_task_id(8)
    # run_deployment(1,1)