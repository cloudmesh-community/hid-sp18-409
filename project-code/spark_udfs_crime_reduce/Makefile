docker-build:
	docker build -t kadupitiya/sparkproject .
	
docker-start:
	docker run kadupitiya/sparkproject
	
docker-stop:
	docker stop $$(docker ps -a -q -f status=running)


