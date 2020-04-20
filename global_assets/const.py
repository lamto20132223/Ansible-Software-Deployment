
name ='Flask Session Tutorial',
version ='0.0.1',
description ='Source code for the accompanying tutorial on how to use Blueprints in Flask.',
long_description ="long_description",
long_description_content_type ='text/markdown',
url ='https://github.com/hackersandslackers/flaskblueprint-tutorial',
author ='Todd Birchard',
author_email ='toddbirchard@gmail.com',
classifiers =[
                'Programming Language :: Python :: 3.7',
            ],
keywords ='Flask Flask-Assets Blueprints',
packages ="find_packages()",
install_requires =['Flask',
                  'Flask_assets'],
extras_require ={
                   'dev': ['check-manifest'],
                   'test': ['coverage'],
                   'env': ['python-dotenv']
               },
entry_points ={
                 'console_scripts': [
                     'install=wsgi:__main__',
                 ],
             },
project_urls ={
                 'Bug Reports': 'https://github.com/hackersandslackers/flaskblueprint-tutorial/issues',
                 'Source': 'https://github.com/hackersandslackers/flaskblueprint-tutorial/',
             },


import os
import sys

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
inventory_dir = ROOT_DIR +  '/static/ansible/inventory'
playbook_dir = ROOT_DIR +  '/static/ansible/playbooks'
facts_dir = ROOT_DIR +  '/static/ansible/facts'
role_dir = ROOT_DIR +  '/static/ansible/playbooks/roles'

tools_dir = ROOT_DIR+ '/static/tools'
ansible_group_vars_template_dir = ROOT_DIR + '/static/ansible/group_vars_template/group_vars_default_template/group_vars'
ansible_group_vars_sf_dir =  ROOT_DIR + '/static/ansible/group_vars_template/group_vars_for_software_management/group_vars'
ansible_group_vars_dir =ROOT_DIR + '/static/ansible/inventory/group_vars'