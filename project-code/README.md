# Location based crime data search and analysis with Spark UDF
  
## Overview
Crimes are horrifying and cost the progress of mankind in many ways
while influencing our society and day to day life. Because of that,
higher priority is always given by the government and politicians to
reduce the crime rate around the world. Crime solving and prevention
get notoriously difficult due to complex causes such as poverty,
parental neglect, low self-esteem, alcohol, drug abuse and etc. Crime
data analysis could be helpful to understand the patterns hidden
inside the crime data. One good way to prevent crimes is to raise the
awareness of the crime prone areas and the patterns in which crime are
committed.  In this paper, location based crime data search and
analysis framework is introduced and developed using a judicious
combination of Spark user defined functions and Haversine method. The
implemented framework allows users to analyze and see the crime
patterns exist near a specific location defined with an address and a
radius. Framework provides crime data analysis in geospatial, time
series and statistical forms. Using this framework, we were able to
clearly see seasonal effect in crime data near Chicago city area and
we also noticed that crime rate is monotonically decreasing when we
move away from the Chicago city area.

## Video demonstration
Here is the link to the [video](https://www.youtube.com/watch?v=PU7PLzCxKds) demonstartion of the project.

## Technology Usage
We used Python as the main programming language in this project and
few web technologies such as HTML, CSS, JQuery and Google maps java
script API are used for the front end development of the project. Full
description of programming environments and library packages which
used to implement the crime analyzing and visualization framework are 
listed as follows.

* Python programming environment  3.6   
* Flask                           0.12   
* connexion                       1.1.15 
* decorator                       4.2.1  
* python-dateutil                 2.6.0  
* setuptools                      21.0.0 
* numpy                           1.14.0 
* scipy                           0.18.1 
* pandas                          0.20.3 
* scikit-learn                    0.18  
* pyspark                         2.1.1  
* scikit-learn                    0.18  
* java run time environment       8.16.1
* Apache Spark standalone version 2.3.0 
* Swagger codegen                 2.1.2 
* HTML                            5       
* CSS                             -      
* Java Script                     -      
* JQuery                          -      
* Google Maps Java script API     -      
* Dygraphs                        -      
* Docker                          1.13.1 

## API's defined in swagger service

  * ```data```
  
  * ```data/fetch```
  
  * ```crimes```
  
  * ```/crimes/search```
  
  * ```/crimes/filter```
  
  * ```/crimes/reduceByYear```

  * ```/crimes/reduceByMonth```

  * ```/crimes/trigerSparkUDF```

## Instructions for docker installation

* git clone the project.
  * Alternatively you can also download the docker image from the docker hub. Then you dont need to do docker build.
  
  * ```docker pull kadupitiya/crime-project```

* you should install docker.

* Change the directory to **project-code** folder.

* Start the service using following make command (Before statring the docker-build and start please make sure that your 
computer is not using port 5050 for some other task as you are going to see the web application on port 5050).
  
  * ```make docker-compose-start```

* Now you should see that two services are up and running as shown in following:

	```
	{
	    Creating projectcode_sawgger_service_1 ... done
	    Creating projectcode_web_app_1         ... done
	    Attaching to projectcode_sawgger_service_1, projectcode_web_app_1
	    sawgger_service_1  | #starts the services
	    sawgger_service_1  | #echo /usr/src/app
	    sawgger_service_1  | #@echo Dockerfile Makefile README.md crimes.yaml data lib requirements.txt server
	    sawgger_service_1  | cd server; python -m swagger_server; cd ..;
	    web_app_1          |  * Running on http://0.0.0.0:5050/ (Press CTRL+C to quit)
	    sawgger_service_1  | /usr/local/lib/python3.6/site-packages/connexion/resolver.py:62: DtypeWarning: Co
	    19,20) have mixed types. Specify dtype option on import or set low_memory=False.
	    sawgger_service_1  |   return self.function_resolver(operation_id)
	    sawgger_service_1  |  * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
	}

	```
* Then you can open the following URL in any of the web browser to see the web application:

  * [http://localhost:5050/](http://localhost:5050/)

* Get the container ID using following command
  
  * ```docker ps```

* Stop the service using following commands
  
  * ```make docker-stop```
  
