dev:
	@poetry install --no-root --with dev

test:
	@poetry run pytest ./tests
