dev:
	@poetry install --with dev

test:
	@poetry run pytest ./tests

lock:
	@poetry lock
	@poetry export --with benchmark --without-hashes -o requirements.txt

start-jupyter-container:
	docker run --rm -p 8888:8888 -v $(pwd)/:/home/jovyan/ladec-2/ jupyter/minimal-notebook
