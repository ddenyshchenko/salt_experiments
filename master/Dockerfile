FROM centos:7.2.1511

RUN set -ex ;\
    yum install -y epel-release ;\
    yum install -y salt-master ;\
    yum install vim tree

COPY master /etc/salt/master

EXPOSE 4505
EXPOSE 4506

ENTRYPOINT ["/usr/bin/salt-master"]
