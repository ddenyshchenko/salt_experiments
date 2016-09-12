FROM centos:7.2.1511

RUN yum install -y epel-release && \
    yum install -y python-pip && \
    yum clean all && \
    pip install flask

RUN mkdir /opt/web
COPY ./app.py /opt/web/
COPY ./configs /opt/web/configs

CMD /opt/web/app.py
