DOCKER_COMPOSE := docker-compose

# --- Билд Docker образа ---
build:
	@echo "Сборка Docker образа..."
	$(DOCKER_COMPOSE) build

# --- Поднять сервис---
up:
	@echo "Запуск контейнера..."
	$(DOCKER_COMPOSE) up -d

# --- Остановить сервис ---
down:
	@echo "Остановка контейнера..."
	$(DOCKER_COMPOSE) down