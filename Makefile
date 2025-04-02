up:
	docker-compose up -d --build
build:
	docker-compose build --no-cache --force-rm
stop:
	docker-compose stop
down:
	docker-compose down
restart:
	@make down
	@make up
destroy:
	docker-compose down --rmi all --volumes --remove-orphans
destroy-volumes:
	docker-compose down --volumes
ps:
	docker-compose ps
logs:
	docker-compose logs
login:
	docker-compose exec workspace bash
start:
	@make up
	@make login
run:
	@make up
	@echo "Waiting for container to be ready..."
# 必要なら調整（健康チェック導入もあり）run:
	@sleep 2
	docker-compose exec workspace bash -c "python main.py"
