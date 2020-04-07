FROM registry.ocs.com/lamtv10/software_deployment/base_sfd_lamtv10
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
COPY . /root/app
VOLUME /root/app/static/ansible
CMD cd /root/app && python app_dev.py
