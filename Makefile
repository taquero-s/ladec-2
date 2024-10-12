dev:
	@poetry install --no-root --with dev

test:
	@poetry run pytest ./tests

lock:
	@poetry lock
	@poetry export --with benchmark --without-hashes -o requirements.txt
