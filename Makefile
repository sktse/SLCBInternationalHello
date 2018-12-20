SHELL := /bin/bash

install:
	virtualenv venv --python=python; \
	source ./venv/bin/activate; \
	pip install -r requirements.txt;

install-win:
	virtualenv venv --python=python; \
	source ./venv/bin/activate; \
	pip install -r requirements.txt; \
	pip install -r requirements-win.txt;

test:
	source ./venv/bin/activate; \
        cd SLCBInternationalHello; \
	python -m pytest -v --log-cli-level=INFO ../tests/*.py -s ${ARGS};

release:
	mkdir tmp; \
	git archive -o ./tmp/SLCBInternationalHello-git.zip HEAD; \
	mkdir tmp/SLCBInternationalHello; \
	mv ./tmp/SLCBInternationalHello-git.zip ./tmp/SLCBInternationalHello/; \
	unzip ./tmp/SLCBInternationalHello/SLCBInternationalHello-git.zip -d ./tmp/SLCBInternationalHello/; \
	cd ./tmp; \
	zip -r ../SLCBInternationalHello.zip ./SLCBInternationalHello/ -x ./SLCBInternationalHello/SLCBInternationalHello-git.zip; \
	cd ..; \
	rm -rf ./tmp;

build-readme:
	source ./venv/bin/activate; \
    python ./builds/build_readme.py;

clean:
	rm SLCBInternationalHello.zip; \
	rm -rf ./venv;
