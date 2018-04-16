docker-compose-start:
	docker-compose up

docker-compose-silent-start:
	docker-compose up -d
	
docker-stop:
	docker stop $$(docker ps -a -q -f status=running)
	docker stop $$(docker ps -a -q)

docker-remove:
	docker rm $$(docker ps -a -q)