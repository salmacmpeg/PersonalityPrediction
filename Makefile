.PHONY: install run_inference run_builder check clean runner_inference runner_builder test_all test_posttrain test_pretrain test_training	
.DEFAULT_GOAL:=runner_inference
run_inference: 
	poetry run python src/runner_inference.py
run_builder: 
	poetry run python src/runner_builder.py
check:install
	poetry run flake8
clean: 
	rm -rf `find . -type d -name  __pycache__`
runner_inference: check test_all run_inference clean
runner_builder: check test_all run_builder clean
install: pyproject.toml
	poetry install
test_all:
	poetry run pytest -v -s --html=src/logs/pytest_report.html
test_posttrain:
	poetry run pytest -v -s -m posttrain
test_pretrain:
	poetry run pytest -v -s -m pretrain
test_training:
	poetry run pytest -v -s -m training