SHELL := /bin/bash

install:
	virtualenv venv --python=python; \
	source ./venv/bin/activate; \
	pip install -r requirements.txt;

test:
	source ./venv/bin/activate; \
        cd SLCBInternationalHello; \
	python -m pytest -v --log-cli-level=INFO ../tests/*.py -s;

release:
	git archive -o SLCBInternationalHello.zip HEAD;

clean:
	rm SLCBInternationalHello.zip; \
	rm -rf ./venv;
