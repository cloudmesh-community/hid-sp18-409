SWAGGER_CODEGEN=java -jar modules/swagger-codegen-cli.jar

service:
	#creates the swagger service from the yaml file and places the controllers in the appropriate directory
	$(SWAGGER_CODEGEN) generate -i crimes.yaml -l python-flask -o server -D supportPython3=true
	cp crimes_controller.py server/swagger_server/controllers
	mkdir server/data
	cp crimedata_small.csv server/data
	cp requirements.txt server
	# Install dependencies and server side code
	cd server; pip install -r requirements.txt; python setup.py install; cd ..;
	
client:
	#creates the swagger client using the yaml file
	$(SWAGGER_CODEGEN) generate -i crimes.yaml -l python -o client -D supportPython3=true
	cp testClient.py client
	cd client; pip install -r requirements.txt; python setup.py install; cd ..;
	
start:
	#starts the services
ifeq ($(OS),Windows_NT)
	cd server; cygstart --hide python -m swagger_server; cd ..;	
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Linux)
		cd server; python -m swagger_server &; cd ..;
	endif
endif

stop:
	#stops the service
ifeq ($(OS),Windows_NT)
	taskkill /f /t /im python.exe	
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Linux)
		fuser -k 8080/tcp
	endif
endif

test:
	#executes a number of tests against the service
	cd client; python testClient.py; cd ..;

clean: 
	# removes the code generated
	rm -r server/
	rm -r client/
