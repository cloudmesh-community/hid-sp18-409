FROM python:3-onbuild

MAINTAINER Kadupitiya kadupitige <kadupitiya@kadupitiya.lk>

# Copy required files
COPY ./ /usr/src/app2
RUN ls -la /usr/src/app2/*

WORKDIR /usr/src/app2

# install pyspark  
RUN pip install -r requirements.txt

# tell the port number the container should expose
EXPOSE 5050

# start the crime WebAPP
CMD python crimeService.py

