Mai's comment:
1. flask là gì
2. các gói repository offline có mục đích gì, giải thích rõ hơn
3. Docker Iage là gì, có mục đích gì
4. Các mục có giải thích phía dưới thì phải có chú thích (ví dụ xem mục 2.1)
5. Đối với mỗi khối
Mô tả chi tiết URL, phương thức, body request mẫu và body response để hình dung
6. Có một luồng mô tả ngắn và tổng quan về luồng xử lý của từng phần Core API (từ khối này xử lý gì --> khối kia xử lý gì, mục đích gì)
trước khi đi vào chi tiết từng khối 
7. Playbook là gì, giải thích ở mục nào 
8. Thêm giao diện luồng để rõ hơn luồng thực hiện

https://medium.com/eway/nguy%C3%AAn-t%E1%BA%AFc-thi%E1%BA%BFt-k%E1%BA%BF-rest-api-23add16968d7
https://techtalk.vn/tat-tan-tat-ve-api.html

URL tạo bài viết: http://my-blog.xyz/posts. Tương ứng với HTTP method là POST
URL đọc bài viết với ID là 123: http://my-blog.xyz/posts/123. Tương ứng với HTTP method là GET
URL cập nhật bài viết với ID là 123: http://my-blog.xyz/posts/123. Tương ứng với HTTP method là PUT
URL xoá bài viết với ID là 123: http://my-blog.xyz/posts/123. Tương ứng với HTTP method là DELETE


STatus code:
200: OK
201: Created
204: No Content 
304: Not Modified 
400: Bad request 
401: Unauthorized 
403: Forbidden 
404: Not Found 
409: Conflict 
500: Internal Server Error



Tài liệu mô tả URL API:

Bắt đầu mọi service bằng http://0.0.0.0:4321/api/v1/

"Function NAME: "
- get_all__conferences()
- add_conference()
- get_conference()
- edit_conference()

from flask_restplus import Api, Resource
@api.route("/conferences/")
class ConferenceList(Resource):
    def get(self):
        """
        returns a list of conferences
        """
    def post(self):
        """
        Adds a new conference to the list
        """





Tài liệu mô tả thiết kế API và URL
Địa chỉ API: http://172.16.29.193:4321:

1.	TỔNG HỢP LIST METHOD+  URL:
"Discover Node":
POST /hosts/add_host
POST /hosts/update_host
GET  /hosts
POST /hosts/discover_hosts
GET  /hosts/<host_id>
GET  /hosts/host_info?host_id=xxx
GET /hosts/host_info?host_id=xxxx&fields=ram,disk,mem,interface
GET /hosts/interface_resources?interface_id=xx&device_name=xx, host_id=xxx
GET /hosts/disk_resources?disk_id=xx,device_name=xx,host_id=xxx
# GET  /hosts?q=xxx
# GET+POST /hosts/<host_id>/historys
# PUT  /hosts/host_id/refresh


"Assign Role + Service":
GET  /roles
GET  /roles/<role_id>/role_info || /roles/<role_id>
POST /roles/add_host_to_role
POST /roles/test_create_deployment
POST /roles/test_create_service_setup
POST /roles/test_create_ansible_inventory_with_role
POST /roles/test_create_ansible_playbook
POST /roles/test_create_task



GET  /hosts/deployments || /deployments

GET  /hosts/<host_id>/deployments
GET /hosts/deployments/<deployment_id> || /deployments/<deployment_id>
GET  /deployments/<deployment_id>/service_setups
GET  /deployments/<deployment_id>/service_setup_id  || GET  /service_setups/<service_setup_id> || GET  /service_setups?deployment_id=&service_name=&

# POST /service_setups/disable_setup
# POST /service_setups/enable_setup
GET  /deployments/<deployment_id>/playbooks
# GET   /deployments/<deployment_id>/playbooks?service_setup_id=xxxx

GET  /service_setups/<service_setup_id>/tasks

GET  /service_setups/<service_setup_id>/<task_id>  || GET  /tasks/<task_id>

GET /tasks/
GET /tasks/<task_id>/changes
GET /changes/<string:change_id>


"Insert Specific Config":
# GET  /configs/specific_configs/
# POST+PUT /api/configs/specific_configs
# GET  /configs/specific_configs/validate
# GET  /configs/specific_configs/recommend
# POST /configs/specific_configs/submit
GET /tools

"START, UNDO, PAUSE, NEXT"
# POST /installation/
# action:-START-UNDO-PAUSE-NEXT
# GET  /installation
# GET  /installation/node_info
# GET  /installation/service_info?node_id=
# GET  /installation/task_info?service_id=
# GET  /installation/change_info?task_id=

POST /installation/run_service_setup
POST /installation/run_task
POST /installation/skip
GET /installation/current
GET /tasks/update_task




"SCALLING UP, SCALLING DOWN "

GET: /api/v1/hosts?role=compute
POST: /api/v1/hosts/scalling_up_host
DELETE: /api/v1/hosts/scalling_down_host


"REPLACE CONTROLLER"

GET: /api/v1/hosts?role=controller
POST: /api/v1/hosts/replace_controller


"TEMPLATE"
GET: /api/v1/templates
GET: /api/v1/templates/filter?properties.name=&properties.type=


"RECOMMEND"

POST: /api/v1/recommendations/assign_role
POST: /api/v1/recommendations/select_service 
POST: /api/v1/recommendations/gen_password
POST: /api/v1/recommendations/select_IP 
POST: /api/v1/recommendations/select_folders
POST: /api/v1/recommendations/configs


"FILE CONFIFG "

GET: /api/v1/configs/<host_id>
GET: /api/v1/configs/filter?name=&path=&node=&service=
POST: /api/v1/configs/download_configs
GET: /api/v1/configs/compare_config_db_vs_host?host_idt=
GET: /api/v1/configs/compare_config_db_vs_host?file_config_id=
GET: /api/v1/configs/compare_config_db_vs_db?file_config_1_id= & file_config_2_id=
GET: /api/v1/configs/compare_config_host_vs_host?file_config_1_id= & file_config_2_id=


GET: /api/v1/configs/<file_config_id>
GET: /api/v1/configs/<file_config_id>/services 
GET: /api/v1/configs/<file_config_id>/content?type=database|server|last_update
POST: /api/v1/configs/update?file_config_id=file_config_id
POST: /api/v1/configs/commit?file_config_id=file_config_id
POST: /api/v1/configs/rollback?file_config_id


"CHANGE PASSWORD" 
GET: /api/v1/passwords
GET: /api/v1/passwords/<password_id>
PUT: /api/v1/passwords/<passwords_id>


===========================================================================================================
===========================================================================================================
===========================================================================================================
===========================================================================================================
===========================================================================================================


return:
{
    "links":{
        "self": "http://example.com/articles",
        "next": "http://example.com/articles?page[offset]=2",
        "last": "http://example.com/articles?page[offset]=10"
    },
    "data":[{
        "type": "articles",
        "id": "1",
        "attributes": {
          "title": "JSON:API paints my bikeshed!"
    }],

}


===========================================================================================================
===========================================================================================================
===========================================================================================================
===========================================================================================================
===========================================================================================================
===========================================================================================================
===========================================================================================================


"Discover Node":
- POST: /api/v1/hosts/add_host
Bổ xung thêm một Host vào danh sách Hosts sẽ dùng trong OverCloud
body: 
 {
"management_ip":"172.16.29.195", 
"ssh_user":"root",
"ssh_password":"123456@Epc", "host_name":"controller_02"
 }
    response:
     {
        "status":"OK"|"Fail",
        "data":{
            {"host_id": "xxxxx",
             "err_code":""
             "msg":""
            }
        }
     } 

- GET: /api/v1/hosts
    Lấy ra danh sách Hosts đã được thêm vào OverCloud
    response
 {
  .... 
  "data": [<host_id_1>,<host_id_2>,....<host_id_n>]
 }

- POST: /api/v1/hosts/discover_hosts
Gửi yêu cầu get thông tin các Host trong OverCloud về Database. Có thể thao tác discover nhiều host hoặc chỉ một host một lúc.
body: 
 {
"list_host_id":[<host_id_1>,<host_id_2>,..<host_id_n>]
      }
    response: 
 {
        "status":"OK" | "Fail",
        "data": {
            "list_hosts":[
                "<host_id_1>":{ "status":"OK","msg":""}
                "<host_id_2>":{ "status":"Fail", "msg":""}
                .....
            ]
            "ok":4,
            "fail":1
        }
     }

- GET: /api/v1/hosts/<host_id>
Lấy ra thông tin chung chung từng host dựa vào input là host_id
    response:
    {
        "created_at": "",
        "management_ip":"",
        "host_display_name":"",
        "host_roles":[],
        "ssh_user":"",
        "ssh_password":""
        "updated_at":""
        ....
    }


- GET:  /api/v1/hosts/host_info?host_id=xxx
    Lấy ra thông tin chi tiết của từng host dựa vào host_id
    response:
    {
        "default_broadcast":"",
        "default_ipv4":"",
        "disk_resources":[],
        "interface_resources":[],
        "memory_mb":,
        "memory_mb_free":""
        ....
    }


- GET: /api/v1/hosts/host_info?host_id=xxxx&fields=ram,disk,mem,interface
Bổ xung thêm tính năng filter by fields để request chỉ lấy về một loại thông tin cụ thể của host như ram, disk, mem, interface

    response:
    {
        "interface_resources":[]
    }


- GET:  /api/v1/hosts/interface_resources?interface_id=xx & device_name = xx , host_id =xxx
Lấy ra thông tin của interface, dựa vào interface_id, có thể lọc theo device_name, host_id  
response:
    {
        "interface_id":"",
        "active": "True",
        "device_name": "ens0f1",
        "feautures":"",
        "macaddress":"",
        "speed":""
        ....
    }

- GET:  /api/v1/hosts/disk_resources?disk_id = xx, device_name = xx, host_id = xxx 
Lấy ra thông tin của ổ cứng dựa vào disk_id, có thể lọc theo device_name, host_id
    response:
    {
        "disk_id":"",
        "device_name":"sda",
        "model": "LOGICAL_VOLUME",
        "sectors":"",
        "sec2torsize":"",
        "serial":"",
        "vendor":""
        ....
    }

- GET:  /api/v1/hosts?q=xxx
Sử dụng để tìm kiếm host dựa vào các yêu cầu (quer=???) ví dụ ram>20GB, disk>100GB....
    response:
    {
        "count":3,
        "list_host":[<host_id1>,<host_id2>,<host_id3>]
        ....
    }

- GET+POST: /api/v1/hosts/<host_id>/historys?last=xxx
Lấy ra lịch sử các hoạt động gần đây nhất đã thực hiện trên Host dựa vào host_id và last=xxx là số kết quả trả về
    response:
    {
        "date":"",
        "content":"",
        "result":"",
        ....
    }
- PUT: /api/v1/hosts/host_id/refresh
    Gửi yêu cầu cập nhật lại thông tin RAM, DISK, CPU của Host
    body:
    {
        "action":"refresh"
    }

    response:
    {
        "ok":"",
        "msg":""
    }


"Assign Role + Service":

- GET:  /api/v1/roles
Lấy ra thông tin về các ROLE, cùng với đó là danh sách Host đã được assign vào từng Role (ban đầu danh sách này trống)
    response:
    {
        ....
        "list_roles": ["CONTROLLER", "COMPUTE", "CEPH",...]
        "data":{
            "CONTROLLER": [<host_id1>,<host_id2>...],
            "COMPUTE": [<host_id3>,<host_id4>...],
            "CEPH": [<host_id5>]
            ...
        }
    }

- GET: /api/v1/roles/role_info?role_name=CEPH
Lấy ra thông tin chi tiết về từng ROLE, bao gồm các suggestion_services là những service mặc định sẽ cài lên các Host được assign và Role này.
    response:
    {
        ...
        "list_hosts":[<host_id1>,<host_id2>,...],
        "total_cpu":"",
        "total_ram":"",
        "suggestion_services":["nova","cinder","neutron"....]
    }

- POST: /api/v1/roles/add_host_to_role
Gửi yêu cầu thêm một host vào Role với host_id, role_name được validate trước.
    body:
    {
        "host_id":<host_id>,
        "role_name":<role_name>
    }

    response:
    {
        "ok":"",
        "msg":"",
        "redirect":""/api/v1/roles/role_info?role_name=CEPH
    }


- GET: /api/v1/hosts/<host_name>/deployments
Lấy ra danh sách tất cả deployments, mỗi deployments sẽ tưng ứng với một Node
    response:
    {
        "list_deployments":[
            {"index":1, "deployment_id":"", "status":""},
            {"index":2, "deployment_id":"", "status":""},
            {"index":3, "deployment_id":"", "status":""}
        ]
    }

- GET /api/v1/deployments/<deployment_id>/service_setups
Lấy ra thông tin danh sách service_setups của từng deployment
    response:
    {
        "deployment_id":"",
        "list_service_setups":[
            {"index":1, "service_setup_id":"", "status":""},
            {"index":2, "service_setup_id":"", "status":""},
            {"index":3, "service_setup_id":"", "status":""}
        ]

    }


- GET /api/v1/service_setups?deployment_id= & service_name= &
Thông tin chi tiết của một service_setup    

- POST /api/v1/service_setups/disable_setup
Sử dụng để bỏ không cài một hoặc một số service không cần thiết

- POST /api/v1/service_setups/enable_setup
Sử dụng để tái bổ xung một hoặc một số service đã bị disable

- GET /api/v1/deployments/<deployment_id>/playbooks
Lấy danh sách playbook sẽ được chạy trong deployment

- GET /api/v1/deployments/<deployment_id>/playbooks?service_setup_id=xxxx 
Lấy ra danh sash playbook sẽ được cài trong  service_setup_id

- GET /api/v1/service_setups/<service_setup_id>/tasks
Danh sách tasks trong service_setup_id

- GET /api/v1/service_setups/<service_setup_id>/tasks?task_id=xxx 
Trạng thái, kết quả của task với task_id=xxx

- GET /api/v1/tasks/<task_id>
Trạng thái, kết quả của task với task_id=xxx
Danh sách change được thực hiện trong task này


"Insert Specific Config":
- Get: /api/v1/configs/specific_configs
Danh sách các config đặc biệt mà bắt buộc người dùng phải nhập vào bằng tay

- POST + PUT  : /api/configs/specific_configs
    Điền vào giá trị của specific_configs

- POST: /api/v1/configs/specific_configs/validate
    Validate một giá trị 

- GET: /api/v1/configs/specific_configs/recommend
    Xin gợi ý về một giá trị 

- POST: /api/v1/configs/specific_configs/submit
    Submit danh sách specific_configs 


"START, UNDO, PAUSE, NEXT"

- POST /api/v1/installation/
action:-START-UNDO-PAUSE-NEXT
Với mối action đầu vào thực hiện một thao tác trong quá trình cài đặt VIM
  
- GET /api/v1/installation
Liệt kê trạng thái của installation: Danh sách các Node+status cài trên từng Node

- GET /api/v1/installation/node_info
Liệt kê trạng thái của installation trên Node: Danh sách các Service_setup +status cài trên từng Service_setup

- GET /api/v1/installation/service_info?node_id=
Liệt kê trạng thái của installation trên Service_setup: Danh sách các task_setup +status cài trên từng task

    
- GET /api/v1/installation/task_info?service_id= 
    Trạng thái, thông tin của task

- GET /api/v1/installation/change_info?task_id=
    Danh sách change ứng với task_id này


"SCALLING UP, SCALLING DOWN "

- GET: /api/v1/hosts?role=compute
    Liệt kê danh sách các hosts thuộc vào role COMPUTE  

- POST: /api/v1/hosts/scalling_up_host
Thực hiện thao tác scalling_up, body data là thông tin host compute mới
    
- DELETE: /api/v1/hosts/scalling_down_host
Thực hiện thao tác scalling_down, body data là id host compute sẽ bị gỡ khỏi hệ thống

"REPLACE CONTROLLER"

- GET: /api/v1/hosts?role=controller
    Liệt kê danh sách các hosts thuộc vào role CONTROLLER
- POST: /api/v1/hosts/replace_controller
Thực hiện thao tác replace_controller, body data là thông tin host controller mới và host controller sẽ bị gỡ khỏi hệ thống


"TEMPLATE"
- GET: /api/v1/templates
    Liệt kê danh sách tất cả templates  

- GET: /api/v1/templates/filter?properties.name=&properties.type=
    Tìm kiếm template theo name,type


"RECOMMEND"
- POST: /api/v1/recommendations/assign_role
- POST: /api/v1/recommendations/select_service 
- POST: /api/v1/recommendations/gen_password
- POST: /api/v1/recommendations/select_IP 
- POST: /api/v1/recommendations/select_folders
- POST: /api/v1/recommendations/configs


"FILE CONFIFG "
- GET: /api/v1/configs/<host_id>
Liệt kê danh sách file_configs + địa chỉ file_config trên  host có host_id=host_id

- GET: /api/v1/configs/filter?name=&path=&node=&service=
    Tìm kiếm file_config dựa vào tên, path, node,service

- POST: /api/v1/configs/download_configs
Xuất file_config từ DB ra local, body_data là file_config_id

- GET: /api/v1/configs/compare_config_db_vs_host?host_id=  
So sánh từng dòng cấu hình trên tất cả file_config của Host có host_id=host_id tương ứng với database và nội dung đang dùng trên Host ==> Tìm ra những thay đổi chưa được commit trên Host đó

- GET: /api/v1/configs/compare_config_db_vs_host?file_config_id=
    Với mỗi file_config_id tìm thay đổi trong db và host

- GET: /api/v1/configs/compare_config_db_vs_db?file_config_1_id= & file_config_2_id=
So sánh 2 file_config trong DB với nhau, có thể là 2 file_config của cùng một service nhưng đặt trên 2 host khác nhau

- GET: /api/v1/configs/compare_config_host_vs_host?file_config_1_id= & file_config_2_id=
    So sánh 2 file_config trên 2 host với nhau.

- GET: /api/v1/configs/<file_config_id>
    Lấy ra nội dung cảu file_config 

- GET: /api/v1/configs/<file_config_id>/services 
    Lấy ra danh sách service đang sử dụng file_config   

- GET: /api/v1/configs/<file_config_id>/content?type=database|server|last_update
    Lấy ra nội dung file_config theo type để so sánh với nhau:
    + database: đang ở trong database
    + server: Nội dung thực tế trên server
    + last_update: Nội dung trước khi commit, update    

- POST: /api/v1/configs/update?file_config_id=file_config_id
    + Update file_config từ DB lên server
- POST: /api/v1/configs/commit?file_config_id=file_config_id    
    + Đẩy file_config từ server về DB
- POST: /api/v1/configs/rollback?file_config_id
    + Rollback file_config 


"CHANGE PASSWORD" 
- GET: /api/v1/passwords
    Liệt kê danh sách User, Password
- GET: /api/v1/passwords/<password_id>
    + Lấy các thông tin liên quan đến password này như file_config sử dụng, service sử dụng...
- PUT: /api/v1/passwords/<passwords_id>
    + Cập nhật password mới.




default:
  image: python_27

  before_script:
    - bundle install


build:
    stage: build
    tags:
        - docker
    script:
        - echo "Building"
        - mkdir build
        - touch build/info.txt
    artifacts:
        paths:
            - build/

test:
    stage: test
    tags:
        - docker
    script:
        - echo "Testing"
        - test -f "build/info.txt"
        - python lamtv10.py





grep "^[^#;]" smb.conf

UyPTCZKHqauD2PqxJHHh

oj7a969sX3-xJfnKs18K




docker build -t conda_centos_ansible_flask_app:v12 -f Dockerfile . 

docker run  -d  --name mysql --network=host --privileged -v /u01/docker/docker_log/mysql:/var/log/      -v /usr/share/docker/:/usr/share/docker/    -u mysql -e PXC_START='BOOTSTRAP'   -e SQL_SST_USER="sstuser" -e SQL_SST_PASSWD="fPWOWrsMGLaBaP74iK57XoOyJy8aAEew"  docker-registry:4000/mysqlp_v20:q

docker run -d --network=host  conda_centos_ansible_flask_app:v12






ansible all  -i /root/app/static/ansible/inventory/new_node -m setup  --tree  /root/app/static/ansible/facts


docker run --rm -t -i -v /home/srv/gitlab-runner/config:/etc/gitlab-runner   -v /etc/hosts:/etc/hosts  -v  /etc/ssl/certs/ca-bundle.crt:/etc/ssl/certs/ca-certificates.crt  gitlab/gitlab-runner register



CREATE USER 'lamtv10'@'localhost' IDENTIFIED BY 'lamtv10';
CREATE USER 'lamtv10'@'%' IDENTIFIED BY 'lamtv10';

GRANT ALL ON *.* TO 'lamtv10'@'localhost';
GRANT ALL ON *.* TO 'lamtv10'@'%';
flush privileges;


git clone ssh://git@172.16.29.193:2222/lamtv10/software_deployment.git 