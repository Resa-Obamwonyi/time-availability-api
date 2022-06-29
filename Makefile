# DOCKER
all:
	@docker-compose up --build
	@docker-compose exec web python manage.py makemigrations
	@docker-compose exec web python manage.py migrate
	@docker-compose exec web python manage.py test 
