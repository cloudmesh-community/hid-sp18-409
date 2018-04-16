SWAGGER_CODEGEN=java -jar lib/swagger-codegen-cli.jar
YML=crimes.yaml
HOME=server
CLIENT=client
CONFIG=$(HOME)/config
DATA=$(HOME)/data
CONTR=$(HOME)/swagger_server/controllers

docker-build:
	docker build -t kadupitiya/swagger .
	
docker-start:
	docker run -p 8080:8080 kadupitiya/swagger

docker-stop:
	docker stop $$(docker ps -a -q -f status=running)

service:
	#creates the swagger service from the yaml file and places the controllers in the appropriate directory
	$(SWAGGER_CODEGEN) generate -i $(YML) -l python-flask -o $(HOME) -D supportPython3=true
	cp data/*_controller.py $(CONTR)
	cp data/util.py $(CONTR)
	cp data/base_auth.py $(CONTR)
	if ! [ -d $(DATA) ]; then mkdir $(DATA); fi
	if ! [ -d $(CONFIG) ]; then mkdir $(CONFIG); fi
	cp requirements.txt $(HOME)
	cp data/*.yml $(CONFIG)
	# Install dependencies and server side code
	cd $(HOME); pip install -r requirements.txt; python setup.py install; cd ..;

client:
	#creates the swagger client using the yaml file
	$(SWAGGER_CODEGEN) generate -i crimes.yaml -l python -o $(CLIENT) -D supportPython3=true
	cp testClient.py $(CLIENT)
	cd $(CLIENT); pip install -r requirements.txt; python setup.py install; cd ..;

start:
	#starts the services
	cd $(HOME); python -m swagger_server; cd ..;

stop:
	#stops the service
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

test:
	#executes a number of tests against the service
	cd $(CLIENT); python testClient.py; cd ..;

test-data:
	echo "Testing data API"
	curl -H "Authorization: Basic YWRtaW46MTIz" -H "Content-Type:application/json" -X GET http://localhost:8080/cloudmesh/crime_finder/data

test-data-fetch:
	echo "Testing data-fetch API"
	curl -H "Authorization: Basic YWRtaW46MTIz" -H "Content-Type:application/json" -X GET http://localhost:8080/cloudmesh/crime_finder/data/fetch

clean: 
	# removes the code generated
	if [ -d $(HOME) ]; then rm -r $(HOME); fi
	if [ -d $(CLIENT) ]; then rm -r $(CLIENT); fi

