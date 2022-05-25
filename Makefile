dev:
	python -m poetry env remove "$(shell python -m poetry env info --path)/bin/python" || true
	python -m poetry lock
	python -m poetry install
	python -m poetry export -f requirements.txt --output ./docker/requirements.txt

build:
	docker build --memory 2048 -t workshop:latest -f ./docker/Dockerfile .

server:
	docker run \
		-it --rm \
		-v=$(PWD)/notebooks/:/opt/notebooks/:rw \
		-p 8000:8000 -p 4040:4040\
		workshop:latest

run:
	docker run \
		-it --rm \
		-
