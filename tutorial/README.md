# Tutorial Assignment: User defined functions(UDF) in Spark

## Overview

* This tutorial explains following:
	* How to intall Spark in Linux, Windows and MacOS.
	* How to create and utilize user defined functions(UDF) in Spark using Python.
  
## Instructions for Spark installation

###  Linux

* First, JDK should be installed to a path where there is no space in that path. Recommanded JAVA version is 8.
	* http://www.oracle.com/technetwork/java/javase/downloads/index.html
* Second, setup environment variables for jdk by addding bin folder path to to user path variable.
	* ```export PATH = $PATH:/usr/local/java8/bin```
* Next, download and extract Scala pre-built version.
	* http://www.scala-lang.org/download/
* Then, setup environment varibale for Scala by adding bin folder path to the user path variable.
	* ```export PATH = $PATH:/usr/local/scala/bin```
* Next, download and extract Apache Spark pre-built version.
	* https://spark.apache.org/downloads.html
* Then, setup environment varibale for spark by adding bin folder path to the user path variable.
	* ```export PATH = $PATH:/usr/local/spark/bin```
* Finally, for testing the installation, please type the following command.
	* ```spark-shell```

##  Windows

* First, JDK should be installed to a path where there is no space in that path. Recommanded JAVA version is 8.
	* http://www.oracle.com/technetwork/java/javase/downloads/index.html
* Second, setup environment variables for jdk by addding bin folder path to to user path variable.
	1. ```set JAVA_HOME=c:\java8 ```
	2. ```set PATH=%JAVA_HOME%\bin;%PATH%```
* Next, download and extract Apache Spark pre-built version.
	* https://spark.apache.org/downloads.html
* Then, setup environment varibale for spark by adding bin folder path to the user path variable.
	1. ```set SPARK_HOME=c:\spark```
	2. ```set PATH=%SPARK_HOME%\bin;%PATH%```
* Next, download the winutils.exe binary and Save winutils.exe binary to a directory (c:\hadoop\bin).
	* https://github.com/steveloughran/winutils
* Then, change the winutils.exe permission using following command using CMD with administrator permission.
	* ```winutils.exe chmod -R 777 C:\tmp\hive```
	* If your system doesnt have `hive` folder, make sure to create `C:\tmp\hive` directory.
* Next, setup environment varibale for hadoop by adding bin folder path to the user path variable.
	1. ```set HADOOP_HOME=c:\hadoop\bin```
	2. ```set PATH=%HADOOP_HOME%\bin;%PATH%```
* Then, install the latest Enthought Canopy for Python 3.5 (This is a bundled python installer for pyspark)
	* https://store.enthought.com/downloads/#default
* Finally, for testing the installation, please type the following command.
	* ```pyspark```

##  MacOS

* First, JDK should be installed to a path where there is no space in that path. Recommanded JAVA version is 8.
	* http://www.oracle.com/technetwork/java/javase/downloads/index.html
* Second, setup environment variables for jdk by addding bin folder path to to user path variable.
	* ```export JAVA_HOME=$(/usr/libexec/java_home)```
* Next, Install Apache Spark using Homebrew with following commands.
	1. ```brew update```
	2. ```brew install scala```
	3. ```brew install apache-spark```
* Then, setup environment varibale for spark with following commands.
	1. ```export SPARK_HOME="/usr/local/Cellar/apache-spark/2.1.0/libexec/"```
	2. ```export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/build:$PYTHONPATH```
	3. ```export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.4-src.zip:$PYTHONPATH```
* Next, install the latest Enthought Canopy for Python 3.5.
	* https://store.enthought.com/downloads/#default
* Finally, for testing the installation, please type the following command.
	* ```pyspark```

## Instructions for creating Spark User defined functions(UDF)
