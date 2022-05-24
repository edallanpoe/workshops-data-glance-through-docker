dev:
	python -m poetry env remove "$(shell python -m poetry env info --path)/bin/python" || true
	python -m poetry lock
	python -m poetry install
	python -m poetry export -f requirements.txt --output ./docker/requirements.txt

build:
	docker build --memory 2048 -t workshop:latest -f ./docker/Dockerfile .

run:
	docker run \
		-it --rm \
		--add-host=docker.for.mac.host.internal:host-gateway \
		-v=$(PWD)/notebooks/:/opt/notebooks/:rw \
		-p=8888:8888 -p=4040:4040 \
		--network=bridge \
		workshop:latest
