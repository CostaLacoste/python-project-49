brain-games:
	uv run brain-games
build:
	uv build
package-install: build
	uv pip install dist/*.whl
package-uninstall:
	uv pip uninstall brain-games
package-reinstall: build
	uv pip uninstall brain-games
	uv pip install --upgrade dist/*.whl