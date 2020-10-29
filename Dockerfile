FROM ubuntu

ENV PYTHONBUFFER=1

RUN apt update &&\
    apt install python3 curl python3-pip -y &&\
    pip3 install pandas numpy &&\
    pip3 install -i https://test.pypi.org/simple/ lambdata-vdeb==0.0.3