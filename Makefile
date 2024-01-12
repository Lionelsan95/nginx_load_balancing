up:
	docker-compose up -d
up-build:
	docker-compose up -d --build --remove-orphans
up-log:
	docker-compose up --build --remove-orphans
down:
	docker-compose stop
list:
	docker-compose ps