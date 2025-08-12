.PHONY: run install clean check runner
.DEFAULT_GOAL=runner

run: install
	cd src; poetry run python3 main.py

install: pyproject.toml
	poetry --no-root install

clean:
	rm -rf `find . -type d -name __pycache__`

check:
	poetry run flake8 src/

runner: check run clean