#config_loader.py

#yum install python-configparser
#https://vietstack.wordpress.com/2015/06/30/getting-start-with-oslo-config-library/

from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import and_,or_


import sqlalchemy as db 
import os
import json
import yaml
import configparser
import collections


import sys
sys.path.append('../')
from utils import *
import modals as model

Runner = model.Runner



def create_file_path(node_display_name,service_type, file_path ):
    node = session.query(model.Node).filter_by(node_display_name=node_display_name).first()
    service_info = session.query(model.Service_info).filter(and_(model.Service_info.service_type==service_type, model.Service_info.node.has(model.Node.node_display_name==node_display_name)  )).first()

    #service_info = model.Service_info(service_type="test", service_status="lamtv10", tag="test")
    
    file_config_name=file_path.split("/")[-1]
    file_config = model.File_config(file_name=file_config_name, file_path=file_path, service_name=service_type, created_at=datetime.now())
    file_config.node=node


    service_info.file_configs.append(file_config)

    node.service_infos.append(service_info)


    session.add(node)
    session.commit()


def pull_config(file_config):
    runner = Runner('ansible_pull.yml','multinode',{'extra_vars':{'target':file_config.node.node_info.node_name, 'file_to_fetch':file_config.file_path},'tags':['install','uninstall']},None, False,  None,None,None)
    print("pull_config")
    log_run=runner.run()
    print(log_run)


def import_config_to_json(file_config):

    file_path = '/etc/ansible/fetch_file/' + file_config.node.node_info.node_name + file_config.file_path  
    print("import_config_to_json")
    # configparser.default_section = "NOT_USE_DEFAULT"
    config= configparser.ConfigParser(default_section="NOT_USE_DEFAULT")
    
    config.read(file_path)
    #print(example)
    return config








def save_file_config_to_db(file_config):
    print("save_config_to_file")
        #node.service_infos=[service_info]
    pull_config(file_config)
    old_config = export_db_to__file_config(file_config)
    new_config = import_config_to_json(file_config)

    list_new_blocks= new_config.sections()
    list_old_blocks= old_config.sections()


    print("list_new_block: " +  str(list_new_blocks))
    print("list_old_block: " + str(list_old_blocks))

    #print(config[list_blocks[3]]['transport_url'])

    update=model.create_Update_Object("Create Update For Insert Config to Db")


    for block in list_new_blocks:
        print('[' + str(block) +']')
        if block not in list_old_blocks:
            for option in new_config[block]:
                new_openstack_config = model.Openstack_config(created_at=datetime.now(), key=option, value=new_config[block][option], service=file_config.service_name, block = block, activate=1)
                file_config.openstack_configs.append(new_openstack_config)
                new_openstack_config.update=update
                session.add(new_openstack_config)
                session.commit()
        # Bo xung va update config moi co trong new file config

        else: 
            for option in new_config[block]:
                print(option+str(":") + new_config[block][option])
                print(old_config[block])
                if  option not in old_config[block]:
                    new_openstack_config = model.Openstack_config(created_at=datetime.now(), key=option, value=new_config[block][option], service=file_config.service_name, block = block, activate=1)
                    file_config.openstack_configs.append(new_openstack_config)
                    new_openstack_config.update=update
                    session.add(new_openstack_config)
                    session.commit()

                elif new_config[block][option] != old_config[block][option]:

                    new_openstack_config = model.Openstack_config(created_at=datetime.now(), key=option, value=new_config[block][option], service=file_config.service_name, block = block, activate=1)
                    file_config.openstack_configs.append(new_openstack_config)
                    new_openstack_config.update=update

                    old_openstack_config = session.query(model.Openstack_config).filter(and_(model.Openstack_config.block==block, model.Openstack_config.key==option, model.Openstack_config.activate==1, model.Openstack_config.file_id==file_config.file_id ) ).first()
                    old_openstack_config.activate = 0

                    session.add(new_openstack_config)
                    session.add(old_openstack_config)

                    session.commit()



        # Update config cu khong co trong new config 
    for block in list_old_blocks:
        print('[' + str(block) +']')
        if block not in list_new_blocks:
            old_openstack_configs = session.query(model.Openstack_config).filter(and_(model.Openstack_config.block==block, model.Openstack_config.activate==1, model.Openstack_config.file_id==file_config.file_id ) ).all()
            for old_openstack_config in old_openstack_configs:
                old_openstack_config.activate=0
                session.add(old_openstack_config)
                session.commit()
        else:
            for option in old_config[block]:
                print(option+str(":") + old_config[block][option])
                if  option not in new_config[block]:
                    old_openstack_config = session.query(model.Openstack_config).filter(and_(model.Openstack_config.block==block, model.Openstack_config.key==option, model.Openstack_config.activate==1, model.Openstack_config.file_id==file_config.file_id ) ).first()
                    old_openstack_config.activate = 0

                    session.add(old_openstack_config)
                    session.commit()        






            #print("")
            ############################################################
            ############################################################
            ############################################################
            ############################################################
            ############################################################
            ############################################################







def export_db_to__file_config(file_config):
    print("load_json_config")
    config= configparser.ConfigParser(default_section="NOT_USE_DEFAULT")
    config_json={}
    config_json['DEFAULT']={}
    for openstack_config in file_config.openstack_configs:
        if openstack_config.activate==1:
            if openstack_config.block not in config_json:
                config_json[openstack_config.block] ={}
            config_json[openstack_config.block][str(openstack_config.key)]=openstack_config.value
           

    print(type(config_json))

    list_blocks = config_json.keys()
    print(list_blocks)
    list_blocks.sort()
    list_blocks.insert(0,list_blocks.pop(list_blocks.index('DEFAULT')))


    for block in  list_blocks:
        print(type(config_json[block]))
        #config_json[block] = dict(sorted(config_json[block].items(), key=lambda x:x[0].lower()))
        
        config_json[block] = collections.OrderedDict(sorted(config_json[block].items()))
        print(type(config_json[block]))
        print(config_json[block])
        config[block] = config_json[block]



    with open('example.ini', 'w') as configfile:
        config.write(configfile)

    return config



def update_file_config(file_config):
    pull_config(file_config)
    save_file_config_to_db(file_config)






if __name__=="__main__":



    print(global_conf)

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
    
    node = session.query(model.Node).filter_by(node_display_name='controller_01').first()
    service_setups = model.print_service_setup(node)


    swift_proxy_service = session.query(model.Service_setup).filter(and_(model.Service_setup.service_name=="swift_proxy", model.Service_setup.deployment.has(model.Deployment.node.has(model.Node.management_ip=='172.16.29.193')) )).first()

    print(swift_proxy_service)
    tasks = swift_proxy_service.tasks
    # for task in tasks:
    #     print(task)
    # for service_setup in service_setups:
    #     insert_task_from_ansible_task(service_setup)


    

    # session.add(node)
    # session.commit()


    #model.run_specific_task_using_python(tasks[4])

    #ex_config=import_config_to_json()

    file_config = session.query(model.File_config).filter(and_(model.File_config.file_path=="/usr/share/docker/glance/glance/glance-registry.conf", model.File_config.node.has(model.Node.node_display_name=="controller_01") )).first()



    #print(config.sections())


    print(file_config)
    #pull_config(file_config)
    #save_file_config_to_db(file_config)
    for config in file_config.openstack_configs:
        print(config)

    #create_file_path("controller_01", "test", "/usr/share/docker/glance/glance/glance-registry.conf")


    #
    save_file_config_to_db(file_config)
    export_db_to__file_config(file_config)


