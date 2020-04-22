pwd
\cp -r /root/app/bk/playbooks/*  /root/app/static/ansible/playbooks/

#cp -nr /root/app/bk/inventory/* /root/app/static/ansible/inventory/

cp -nr /root/app/bk/inventory/* /root/app/static/ansible/inventory/

cp -nr /root/app/bk/group_vars_template/* /root/app/static/ansible/group_vars_template/

\cp -r /root/app/bk/group_vars_template/group_vars_default_template/* /root/app/static/ansible/group_vars_template/group_vars_default_template/

\cp -r /root/app/bk/group_vars_template/group_vars_for_software_management/* /root/app/static/ansible/group_vars_template/group_vars_for_software_management/

python app_dev.py