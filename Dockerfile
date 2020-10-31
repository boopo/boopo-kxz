FROM centos
MAINTAINER lyz
ENV active prod
RUN mkdir -p src
COPY / /src
WORKDIR src
RUN yum install -y gcc &&yum -y install redis
EXPOSE 6379
RUN yum -y install python3 && pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
EXPOSE 12000
ENTRYPOINT python3 tornado_server.py





