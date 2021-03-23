FROM ubuntu:focal
 
RUN apt update
RUN apt upgrade -y
RUN apt install python3 python3-pip python3-venv -y
WORKDIR /malserver
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install Flask

EXPOSE 5000
CMD ["python3", "/malserver/app.py"]