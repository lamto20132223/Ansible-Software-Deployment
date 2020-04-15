pwd
\cp -r /root/app/bk/playbooks/*  /root/app/static/ansible/playbooks/

#cp -nr /root/app/bk/inventory/* /root/app/static/ansible/inventory/

cp -nr /root/app/bk/inventory/* /root/app/static/ansible/inventory/

\cp -r /root/app/bk/inventory/group_vars/* /root/app/static/ansible/inventory/group_vars/

python app_dev.py