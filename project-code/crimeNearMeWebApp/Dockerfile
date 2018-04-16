FROM python:3-onbuild

MAINTAINER Kadupitiya kadupitige <kadupitiya@kadupitiya.lk>

# install python libs
RUN pip install --upgrade pip && \
	pip install -r requirements.txt

# Copy required files
COPY ./ /usr/src/app2
RUN ls -la /usr/src/app2/*

WORKDIR /usr/src/app2

# tell the port number the container should expose
EXPOSE 5050

# start the crime WebAPP
CMD python crimeService.py