FROM python:3.9-bullseye

RUN apt update
RUN apt install default-jre
RUN pip install tika


CMD ["bash"]