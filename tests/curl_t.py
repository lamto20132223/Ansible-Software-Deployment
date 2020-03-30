import os
#
#
#

import time

##task = [task for task in tasks if task['id'] == task_id]


#### **************************  example *********************************************
#curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks
# #curl -X POST "http://172.16.29.193:9876/language" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"file\": \"docker.io/istio/sidecar_injector:1.4.4\"}"

##***************** add_host ************************



def add_host():
    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/hosts/add_host" -H  "accept: application/json" -H  "Content-Type: application/json" --data @nodes1.json')
    time.sleep(1)
    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/hosts/add_host" -H  "accept: application/json" -H  "Content-Type: application/json" --data @nodes2.json')
    time.sleep(1)
    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/hosts/add_host" -H  "accept: application/json" -H  "Content-Type: application/json" --data @nodes3.json')
    time.sleep(1)
    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/hosts/add_host" -H  "accept: application/json" -H  "Content-Type: application/json" --data @nodes4.json')
    time.sleep(1)

##***************************** discover_hosts *********************************************
def discover_hosts():
    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/hosts/discover_hosts_v1" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
    time.sleep(5)

    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/hosts/discover_hosts_v2" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
    time.sleep(5)


###*******************************add_host_to_role *******************************************************
def add_host_to_role():
    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/roles/add_host_to_role" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role1.json')
    time.sleep(5)
    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/roles/add_host_to_role" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role2.json')
    time.sleep(5)
    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/roles/add_host_to_role" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role3.json')
    time.sleep(5)
    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/roles/add_host_to_role" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role4.json')
    time.sleep(5)


def insert_test_data():
    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/roles/test_create_deployment" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
    time.sleep(5)

    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/roles/test_create_service_setup" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
    time.sleep(5)
    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/roles/test_create_ansible_inventory_with_role" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
    time.sleep(5)

    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/roles/test_create_ansible_playbook" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
    time.sleep(5)
    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/roles/test_run_first_ansble_playbook" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
    time.sleep(5)



    os.system('curl -X POST "http://127.0.0.1:4321/api/v1/roles/test_create_task" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')
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
        'curl -X POST "http://127.0.0.1:4321/api/v1/clean_data" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')

if __name__ == "__main__":
    #delete_data()
    #add_host()
    #discover_hosts()
    #add_host_to_role()
    insert_test_data()
