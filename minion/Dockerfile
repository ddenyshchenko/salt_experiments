FROM centos:7.2.1511

RUN set -ex ;\
    yum install -y epel-release ;\
    yum install -y salt-minion dmidecode redhat-lsb-core

COPY minion /etc/salt/minion

ENTRYPOINT ["/usr/bin/salt-minion"]
