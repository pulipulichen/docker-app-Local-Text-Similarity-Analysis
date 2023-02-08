FROM python:3.9-bullseye

RUN apt update
RUN apt install default-jre -y
RUN pip install tika


CMD ["bash"]