# README.md

## Personality Checking App

This application allows users to submit answers to personality-related questions and receives a classification identifying them as either an introvert or extrovert. The project exemplifies the principles of continuous integration in machine learning with a focus on software engineering best practices, such as clean code architecture, lenting, code automation, dependancy managment, automated testing, and CI/CD pipelines.

### Features

- **Personality Classification**: Based on user input, the app predicts personality type.
- **Data Preprocessing**: Cleans and prepares data for model training.
- **Model Training and Inference**: Utilizes a Decision Tree Classifier to train and predict personality types.
- **Continuous Integration**: Implements automated testing and linting using GitHub Actions for seamless integration.

### Requirements

- Python 3.x
- Poetry for dependency management

### Installation

1. Clone the repository.
2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

### Usage

- **Build Model**:
  ```bash
  poetry run python src/runner_builder.py
  ```
  
- **Run Inference**: 
  ```bash
  poetry run python src/runner_inference.py
  ```

### Testing

Run all tests using pytest:
```bash
poetry run pytest -v -s
```
The project includes comprehensive unit tests for data preprocessing, model training, and inference pipelines, ensuring robustness and reliability.

### Linting

Ensure code quality by running flake8:
```bash
poetry run flake8
```

### CI/CD Workflow

This project uses GitHub Actions for continuous integration. The workflow includes automated testing and linting on every push and pull request, ensuring code quality and consistency across the codebase.

### Logging

Logs are maintained using Loguru. Check `myapp.log` for detailed logs.

### Configuration

Update settings in `src/configs` for environment variables and model settings.

### Clean Code Architecture

The project follows clean code principles, separating concerns across different modules and ensuring maintainability and scalability of the codebase.

### Code Automation

Additionally, the project leverages a Makefile for task automation. Below are the available commands:

- **Install Dependencies**:
  ```bash
  make install
  ```

- **Run Inference**:
  ```bash
  make run_inference
  ```

- **Build Model**:
  ```bash
  make run_builder
  ```

- **Run all Tests**:
  ```bash
  make test_all
  ```

- **Run Post-train Tests**:
  ```bash
  make test_posttrain
  ```

- **Run Pre-train Tests**:
  ```bash
  make test_pretrain
  ```

- **Run Training Tests**:
  ```bash
  make test_training
  ```

- **Check Code Quality**:
  ```bash
  make check
  ```

- **Clean Build Artifacts**:
  ```bash
  make clean
  ```