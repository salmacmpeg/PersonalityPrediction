.PHONY: install run_inference run_builder check clean runner_inference runner_builder
.DEFAULT_GOAL:=runner_inference
run_inference: 
	poetry run python src/runner_inference.py
run_builder: 
	poetry run python src/runner_builder.py
check:install
	poetry run flake8
clean: 
	rm -rf `find . -type d -name  __pycache__`
runner_inference: check run_inference clean
runner_builder: check run_builder clean
install: pyproject.toml
	poetry install
