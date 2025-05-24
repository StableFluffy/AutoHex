push-twine:
	uv build
	uv run twine upload dist/*

format:
	uvx ruff format src

check:
	uvx ruff check src --fix
