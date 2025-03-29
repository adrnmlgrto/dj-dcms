# Start Container (Detached)
up:
	docker compose up -d

# Stop Container
down:
	docker compose down

# Rebuild Container
rebuild:
	docker compose build --no-cache

# Access Container's Regular Shell
shell:
	docker compose exec web sh

# Access Container's Bash Shell
bash:
	docker compose exec web bash

# Create Superuser
django-createsuperuser:
	docker compose exec web uv run manage.py createsuperuser

# Django Check
django-check:
	docker compose exec web uv run manage.py check

# Django Runserver
django-runserver:
	docker compose exec web uv run manage.py runserver

# Access Django Shell
django-shell:
	docker compose exec web uv run manage.py shell

# Run Django Migrations
django-migrate:
	docker compose exec web uv run manage.py migrate