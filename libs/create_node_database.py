
#https://vietstack.wordpress.com/2015/06/30/getting-start-with-oslo-config-library/

from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
import sqlalchemy as db 
from sqlalchemy import and_,or_
from datetime import datetime

import os
import uuid
from uuid import uuid4
import json
import yaml


import sys
sys.path.append('../')
from utils import *
import modals as model

Runner = model.Runner



####################################### DISCOVER NODE #######################################

def add_data_with_relationship():
    movie1 = Movie(title="tovanlam1", release_date=datetime(2015, 6, 5, 8, 10, 10, 10))
    session.add(movie1)

    actor1 = Actor(name="lamtv" , birthday = datetime(2015, 6, 5, 8, 10, 10, 10))
    actor1.movie.append(movie1)

    session.add(actor1)
    session.commit()
    #+++++>>> can sua lai database theo huong ...

#our_node = session.query(Node).filter_by(node_display_name='test1').first() 
#print(our_node)




#our_node = session.query(Node).filter_by(node_display_name='test1').all()
#for node in our_node:
#   print(node)



# count(): Returns the total number of rows of a query.
# filter(): Filters the query by applying a criteria.
# delete(): Removes from the database the rows matched by a query.
# distinct(): Applies a distinct statement to a query.
# exists(): Adds an exists operator to a subquery.
# first(): Returns the first row in a query.
# get(): Returns the row referenced by the primary key parameter passed as argument.
# join(): Creates a SQL join in a query.
# limit(): Limits the number of rows returned by a query.
# order_by(): Sets an order in the rows returned by a query.

# bourne_identity = Movie(title="The Bourne Identity", release_date=datetime(2002, 10, 11,10, 10, 10))
# furious_7 = Movie(title="Furious 7", release_date=datetime(2015, 4, 2,10, 10, 10))
# pain_and_gain = Movie(title="Pain & Gain", release_date=datetime(2013, 8, 23,10, 10, 10))


# matt_damon = Actor(name="Matt Damon", birthday = datetime(1970, 10, 8, 10, 10, 10))
# dwayne_johnson = Actor(name="Dwayne Johnson", birthday = datetime(1972, 5, 2, 10, 10, 10))
# mark_wahlberg = Actor(name="Mark Wahlberg", birthday = datetime(1971, 6, 5, 10, 10, 10))


# bourne_identity.actors = [matt_damon]
# furious_7.actors = [dwayne_johnson]
# pain_and_gain.actors = [dwayne_johnson, mark_wahlberg]


def test_contact():
    lamtv10=session.query(Actor).filter_by(name='lamtv').first() 
    
    
    matt_contact = Contact(phone_number="415 555 2671", address="Burbank, CA", actor=lamtv10)
    # dwayne_contact = ContactDetails("423 555 5623", "Glendale, CA", dwayne_johnson)
    # dwayne_contact_2 = ContactDetails("421 444 2323", "West Hollywood, CA", dwayne_johnson)
    # mark_contact = ContactDetails("421 333 9428", "Glendale, CA", mark_wahlberg)
    
    
    session.add(matt_contact)
    session.commit()

# del_lamtv10=session.query(Actor).filter_by(name='lamtv').first()

# #session.add(del_lamtv10)

# del_lamtv10.name="lamtv10"

# session.commit()


def test_add_nodes_b1():
    print("sdfsdfs")


    #node1 = Node(created_at=datetime.now(), updated_at=datetime.now(), deleted_at=None, management_ip="172.16.29.193", ssh_user="root", ssh_password="123456@Epc", status="set_ip", node_display_name="controller_01")
    node2= Node(created_at=datetime.now(), updated_at=datetime.now(), deleted_at=None, management_ip="172.16.29.194", ssh_user="root", ssh_password="123456@Epc", status="set_ip", node_display_name="controller_02")
    node3= Node(created_at=datetime.now(), updated_at=datetime.now(), deleted_at=None, management_ip="172.16.29.195", ssh_user="root", ssh_password="123456@Epc", status="set_ip", node_display_name="controller_03")


    node_info  = Node_info(node_name="tovanlam1", memory_mb=123)
    #session.add(node1)
    session.add(node2)
    session.add(node3)


    session.commit()


def test_and_nodes_b2():
    list_nodes=session.query(Node).all()
    os.system(' rm -rf /etc/ansible/inventory/new_node')
    file_new_node = open("/etc/ansible/inventory/new_node","a")
    file_new_node.write('[all]')
    file_new_node.write("\n")
    for node in list_nodes:
        file_new_node.write(node.management_ip+" " + "ansible_ssh_user="+str(node.ssh_user) + " "+ "ansible_ssh_pass="+str(node.ssh_password))
        file_new_node.write("\n")

    file_new_node.close()

    os.system('ansible all  -i /etc/ansible/inventory/new_node -m setup  --tree /etc/ansible/facts')

def load_node_info_to_database():
    node=session.query(Node).first()
    #for node in list_nodes:
    with open('/etc/ansible/facts/' + str(node.management_ip)) as data_node:
        node_data = json.load(data_node)
        print(node_data)


def load_node_info_to_database():
    nodes=session.query(Node).all()

    for node in nodes:
        node.updated_at=datetime.now()
        node.node_type="oenstack"
        status="udate_info_to_database"
        with open('/etc/ansible/facts/' + str(node.management_ip)) as data_node:
            node_data = json.load(data_node)
            ansible_facts=node_data['ansible_facts']
            #print(node_data)
            node_name = ansible_facts['ansible_hostname']
            memory_mb = ansible_facts['ansible_memtotal_mb']
            memory_mb_free=ansible_facts['ansible_memfree_mb']
            numa_topology=None 
            metrics= None 
            processor_core=ansible_facts['ansible_processor_cores']
            processor_count=ansible_facts['ansible_processor_count']
            processor_threads_per_core=ansible_facts['ansible_processor_threads_per_core']
            processor_vcpu=ansible_facts['ansible_processor_vcpus']
            os_family=ansible_facts['ansible_os_family']
            pkg_mgr=ansible_facts['ansible_pkg_mgr']
            os_version=ansible_facts['ansible_distribution_version']
            default_ipv4=ansible_facts['ansible_default_ipv4']['address']
            default_broadcast=ansible_facts['ansible_default_ipv4']['broadcast']
            default_gateway=ansible_facts['ansible_default_ipv4']['gateway']
            default_interface_id=ansible_facts['ansible_default_ipv4']['interface']

            node_info=Node_info(node_name=node_name,memory_mb=memory_mb,memory_mb_free=memory_mb_free,numa_topology=numa_topology,metrics=metrics,processor_core=processor_core,processor_count=processor_count,processor_threads_per_core=processor_threads_per_core, processor_vcpu=processor_vcpu,os_family=os_family, pkg_mgr=pkg_mgr,os_version=os_version,default_ipv4=default_ipv4,default_broadcast=default_broadcast,default_gateway=default_gateway,default_interface_id=default_interface_id)
            interface_resources=[]

            for interface in ansible_facts['ansible_interfaces']:
                if "docker" not in interface and "veth" not in interface and "virb" not in interface :

                    interface_info=ansible_facts['ansible_'+interface]
                    device_name=interface_info.get('device')
                    speed=interface_info.get('speed')
                    port_info=None 
                    active=str(interface_info.get('active'))
                    features=str(interface_info.get('features'))
                    macaddress=interface_info.get('macaddress')
                    module=interface_info.get('module')
                    mtu=interface_info.get('mtu')
                    pciid=interface_info.get('pciid')
                    phc_index=interface_info.get('phc_index')
                    type_interface=interface_info.get('type_interface')
                    if device_name==ansible_facts['ansible_default_ipv4']['interface']:
                        is_default_ip='True'
                    else:
                        is_default_ip='False'

                    interface_resource=Interface_resource(device_name=device_name,speed=speed,port_info=port_info,active=active,features=features,macaddress=macaddress,module=module,mtu=mtu,pciid=pciid,phc_index=phc_index,type_interface=type_interface,is_default_ip=is_default_ip)
                    interface_resources.append(interface_resource)
            node_info.interface_resources=interface_resources

            disk_resources=[]
            for device in ansible_facts['ansible_devices']:
                if "sd" in device:
                    device_data=ansible_facts['ansible_devices'][str(device)]
                    device_name=device 
                    size = int(float(device_data.get('size')[0:-2].replace(" ", "")))
                    model = device_data.get('model')
                    removable= device_data.get('removable')
                    sectors = device_data.get('sectors')
                    sectorsize=device_data.get('sectorsize')
                    serial = device_data.get('serial')
                    vendor = device_data.get('vendor')
                    support_discard=device_data.get('support_discard')
                    virtual=device_data.get('virtual')

                    disk_resource= Disk_resource(device_name=device_name, size=size, model=model, removable=removable,sectors=sectors,sectorsize=sectorsize,serial=serial, vendor=vendor,support_discard=support_discard,virtual=virtual)
                    disk_resources.append(disk_resource)

            node_info.disk_resources=disk_resources
            node.node_info=node_info
            session.add(node)
            session.commit()







def get_node_from_database():
    node = session.query(Node).filter_by(management_ip="172.16.29.193").first()

    print(node.node_info.interface_resources)


def add_role_to_node():
    node1 = session.query(Node).filter_by(management_ip="172.16.29.193").first()
    
    node_role1=Node_role(role_name="controller")

    node_role2=Node_role(role_name="compute")
    node_role3=Node_role(role_name="ceph")
    node_role4=Node_role(role_name="compute")
    node_role5=Node_role(role_name="controller")


    node1.node_roles=[node_role1, node_role2]


    node2 = session.query(Node).filter_by(management_ip="172.16.29.194").first()
    node2.node_roles=[node_role3]
    node3 = session.query(Node).filter_by(management_ip="172.16.29.195").first()
    node3.node_roles=[node_role4,node_role5]

    session.add(node1)
    session.add(node2)
    session.add(node3)

    session.commit()

def add_deployment_to_node():
    nodes = session.query(Node).all()
    for node in  nodes:
        deployment=Deployment(created_at=datetime.now(),updated_at=datetime.now(), finished_at=None, status='Init', name='deployment_'+ str(node.node_display_name) , progress='Init')
        node.deployment=deployment
        session.add(node)
        session.commit()




################################### DEFAULT_TEMPLATE #####################################
def load_from_template():
    nodes = session.query(Node).all()
    with open('/home/lamtv10/automation_tool/templates/role_service.json') as role_service_json:
        role_services = json.load(role_service_json)
        for node in nodes:
            print("node_name: " + node.node_display_name)
            role=node.node_roles[0]
            print(role.role_name)

            
            service_setups=[]
            for service in role_services[role.role_name]:
                service_setup=  Service_setup(service_type=role.role_name, service_name=service['service_name'], service_info="INIT", service_lib = None, service_config_folder=None, setup_index=service['index'],is_validated_success=None, validated_status=None)
                service_setups.append(service_setup)
            node.deployment.service_setups= service_setups
            session.add(node)
            session.commit()

def print_service_setup(node ):
    def sort_function(e):
        return e.setup_index
    service_setups = node.deployment.service_setups

    service_setups.sort(key=sort_function)

    for service_setup in service_setups:
        print(service_setup.service_name + " index: "+ str(service_setup.setup_index))

    return service_setups

def get_service_setup(node ,service_name):
    service_setups = node.deployment.service_setups


def insert_task_from_ansible_task(service_setup):
    service_role = service_setup.service_name

    with open('/etc/ansible/roles/'+service_setup.service_name+'/tasks/main.yml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        list_tasks = yaml.load(file)

        print(list_tasks)
        tasks=[]
        for i in  range(0,len(list_tasks)-1):
            item=list_tasks[i]
            task = Task(created_at=datetime.now(), finished_at=None, task_display_name=item['name'],setup_data=str(item)[0:100],task_type=None,status="Not validated", result=None, log=None,task_index=i)
            tasks.append(task)

        service_setup.tasks=tasks



def run_specific_task_using_python(task):
    print("OK")
    service_setup=task.service_setup
    node = service_setup.deployment.node

    #print(task.service_setup.deployment.node)
    target = node.node_info.node_name
    runner = Runner('ansible_compute.yml','multinode',{'extra_vars':{'target':target},'tags':['install','uninstall']},task.task_display_name, True,  None,None,None)

    #ansible-playbook ansible_compute.yml --extra-vars "target=target other_variable=foo" --tags "install, uninstall" --start-at-task=task.task_display_name --step

    print(runner.variable_manager)

    log_run=runner.run()
    print(log_run)





def load_config_to_database():
    print("load config to database")





if __name__=="__main__":


    CONF = {"database":{"connection":"mysql+pymysql://lamtv10:lamtv10@172.16.29.198/auto_lamtv10"}}
    db_engine = db.create_engine(CONF["database"]["connection"])
    Node_Base.metadata.create_all(db_engine)
    db_connection = db_engine.connect()


    #result = db_connection.execute("select * from nodes")
    #print(result)

    #db_connection.execute(db_nodes.insert(), {"id: "})

    Session = sessionmaker()
    Session.configure(bind=db_engine) 
    session = Session()
    #test_add_nodes()
    #print("lamtv10")
    #load_node_info_to_database()
    #get_node_from_database()
    #add_role_to_node()
    #node_role = session.query(Node_role).filter_by(role_name="compute").delete()
    
    #session.commit()

    #add_deployment_to_node()
    #load_from_template()
    
    node = session.query(Node).filter_by(node_display_name='controller_01').first()
    service_setups = print_service_setup(node)


    swift_proxy_service = session.query(Service_setup).filter(and_(Service_setup.service_name=="swift_proxy", Service_setup.deployment.has(Deployment.node.has(Node.management_ip=='172.16.29.193')) )).first()

    print(swift_proxy_service)
    tasks = swift_proxy_service.tasks
    # for task in tasks:
    #     print(task)
    # for service_setup in service_setups:
    #     insert_task_from_ansible_task(service_setup)


    

    # session.add(node)
    # session.commit()


    #run_specific_task_using_python(tasks[4])












