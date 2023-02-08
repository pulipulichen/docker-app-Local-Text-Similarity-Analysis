FROM python:3.9-bullseye

RUN apt update
RUN apt install default-jre -y

RUN pip install tika==2.6.0
RUN pip install pyexcel-ods3==3 0.6.1


CMD ["bash"]