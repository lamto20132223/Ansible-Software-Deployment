FROM registry.ocs.com/lamtv10/software_deployment/base_sfd_lamtv10
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
COPY . /root/app
WORKDIR /root/app
RUN  bash ./copy.sh

#CMD cd /root/app && python app_dev.py

CMD bash ./start.sh
