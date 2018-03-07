FROM python:3-onbuild

MAINTAINER Kadupitiya kadupitige <kadupitiya@kadupitiya.lk>

# Setup java 
RUN apt-get update
RUN apt-get install -q -y default-jre

# install net tools
RUN apt-get install -q -y net-tools
  
RUN pip install -r requirements.txt

# tell the port number the container should expose
EXPOSE 8080

# Install the flask service using make commands
RUN make service

# start the service
CMD ["make", "start"]