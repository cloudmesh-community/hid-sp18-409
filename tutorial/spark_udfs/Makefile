docker-start:
	docker build -t kadupitiya/tutorial .
	docker run kadupitiya/tutorial
	
docker-stop:
	docker stop $$(docker ps -a -q -f status=running)


