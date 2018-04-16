FROM python:3-onbuild

MAINTAINER Kadupitiya kadupitige <kadupitiya@kadupitiya.lk>

# install curl
RUN apt-get update
RUN apt-get -q -y install curl
RUN apt-get -q -y install software-properties-common

# Setup java jdk 8
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
RUN apt-get update
RUN apt-get install -q -y oracle-java8-installer

# Copy required files
COPY ./ /usr/src/app
RUN ls -la /usr/src/app/*

WORKDIR /usr/src/app

# install pyspark  
RUN pip install -r requirements.txt

# tell the port number the container should expose
EXPOSE 8080

# Install the flask service using make commands
RUN make service

# start the crime framework
#CMD ["make", "docker-compose-start"]
CMD ["make", "start"]
