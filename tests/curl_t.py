import os
#
#
#


##task = [task for task in tasks if task['id'] == task_id]


#### **************************  example *********************************************
#curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks
# #curl -X POST "http://172.16.29.193:9876/language" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"file\": \"docker.io/istio/sidecar_injector:1.4.4\"}"

##***************** add_host ************************
# os.system('curl -X POST "http://127.0.0.1:4321/api/v1/hosts/add_host" -H  "accept: application/json" -H  "Content-Type: application/json" --data @nodes.json')


##***************************** discover_hosts *********************************************
#os.system('curl -X POST "http://127.0.0.1:4321/api/v1/hosts/discover_hosts_v1" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')

# os.system('curl -X POST "http://127.0.0.1:4321/api/v1/hosts/discover_hosts" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')


###*******************************add_host_to_role *******************************************************
#os.system('curl -X POST "http://127.0.0.1:4321/api/v1/roles/add_host_to_role" -H  "accept: application/json" -H  "Content-Type: application/json" --data @node_role.json')


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