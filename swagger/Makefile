SWAGGER_CODEGEN=java -jar modules/swagger-codegen-cli.jar

service:
	#creates the swagger service from the yaml file and places the controllers in the appropriate directory
	$(SWAGGER_CODEGEN) generate -i crimes.yaml -l python-flask -o server -D supportPython3=true
	cp crimes_controller.py server/swagger_server/controllers
	if [ ! -d "/server/data" ]; then mkdir server/data; fi
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
	cd server; python -m swagger_server; cd ..;

stop:
	#stops the service
	fuser -k 8080/tcp


test:
	#executes a number of tests against the service
	cd client; python testClient.py; cd ..;

clean: 
	# removes the code generated
	rm -r server/
	rm -r client/
