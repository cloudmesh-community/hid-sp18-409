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

# install SPARK
ARG SPARK_ARCHIVE=http://www.gtlib.gatech.edu/pub/apache/spark/spark-2.3.0/spark-2.3.0-bin-hadoop2.7.tgz
ENV SPARK_HOME /usr/local/spark-2.3.0-bin-hadoop2.7
 
ENV PATH $PATH:${SPARK_HOME}/bin
RUN curl -s ${SPARK_ARCHIVE} | tar -xz -C /usr/local/

# install pyspark  
RUN pip install -r requirements.txt

# start the service
CMD ["spark-submit", "main.py"]