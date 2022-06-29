# DOCKER
start:
	@docker-compose up --build
	@docker-compose exec web python manage.py makemigrations
	@docker-compose exec web python manage.py migrate

down:
	@docker-compose down

test:
	@docker-compose exec web python manage.py test