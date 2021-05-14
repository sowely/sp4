FROM ubuntu
COPY main.py .
COPY sub.py .
RUN apt update
RUN apt install python3 -y
