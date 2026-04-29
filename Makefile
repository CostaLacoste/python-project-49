brain-games:
	uv run python -m brain_games.scripts.brain_games
brain-even:
	uv run python -m brain_games.scripts.brain_even
brain-calc:
	uv run python -m brain_games.scripts.brain_calc
build:
	uv build
package-install: build
	uv pip install dist/*.whl
package-uninstall:
	uv pip uninstall hexlet-code
package-reinstall: build
	uv pip uninstall hexlet-code
	uv pip install --upgrade dist/*.whl
lint:
	uv run ruff check brain_games