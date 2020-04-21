export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook ansible_compute.yml
ansible-playbook ansible_controller.yml

#	yum groups install "Virtualization Host"
#	yum grouplist
#	yum groups install "Development tools"
#	yum groups install "Networking Tools"