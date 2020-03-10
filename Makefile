.PHONY: build

build:
	python3 setup.py sdist bdist_wheel

install:
	python3 -m pip install --upgrade --index-url https://test.pypi.org/simple/ --no-deps gcp_python_logging

test-upload:
	python3 -m twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*

upload:
	python3 -m twine upload dist/*