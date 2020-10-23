FROM python:3
MAINTAINER lyz
ENV active prod
RUN mkdir -p src
COPY cumt-kxz src
WORKDIR src
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
EXPOSE 12000
ENTRYPOINT python3 tornado_server.py





