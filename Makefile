dev:
	python -m poetry env remove "$(shell python -m poetry env info --path)/bin/python" || true
	python -m poetry lock
	python -m poetry install
	python -m poetry export -f requirements.txt --output ./docker/requirements.txt

build:
	docker build --memory 2048 -t workshop:latest -f ./docker/Dockerfile .

notebook:
	docker run \
		-it --rm \
		-v=$(PWD)/notebooks/:/opt/notebooks/:rw \
		-p 8000:8000 -p 4040:4040 \
		workshop:latest

.PHONY: clean lint mypy lint dist

clean: clean-envs clean-pyc clean-output

clean-envs:
	rm -rf env

clean-pyc:
	find . -name '*.pyc' -exec rm -fr {} +
	find . -name '*.pyo' -exec rm -fr {} +
	find . -name '*~' -exec rm -fr {} +
	find . -name '__pycache__' -exec rm -fr {} +	 

clean-mypy:
	find . -name '.mypy_cache' -exec rm -fr {} +

clean-output:
	rm -rfv $(etl_path)/data/output/images/*
	rm -rfv $(etl_path)/data/output/files/*
	rm -rfv $(etl_path)/data/output/results/parquet/*
	rm -rfv $(etl_path)/data/output/results/pdf/*
	rm -rfv $(etl_path)/data/output/results/pictures/*

lint:
	pflake8 $(path_code)

mypy:
	@mypy $(path_code)

run:
	docker run \
		-it --rm \
		-v=$(PWD)/results/:/opt/etl/data/output/results/:rw \
		-p 4040:4040 \
		--entrypoint /bin/bash \
		workshop:latest \
		/opt/etl/workshop.sh
