from pathlib import Path


def test_required_directories_exist():
    required_dirs = [
        "data/raw",
        "data/synthetic",
        "data/processed",
        "notebooks",
        "prompts",
        "templates",
        "scripts",
    ]
    for directory in required_dirs:
        assert Path(directory).exists(), f"Missing directory: {directory}"


def test_required_files_exist():
    required_files = [
        "README.md",
        "requirements.txt",
        ".devcontainer/devcontainer.json",
        ".devcontainer/Dockerfile",
        "scripts/generate_synthetic_student_data.py",
        "templates/ai_usage_log_template.md",
        "templates/method_selection_template.md",
        "templates/interpretation_template.md",
    ]
    for file in required_files:
        assert Path(file).exists(), f"Missing file: {file}"


def test_required_notebooks_exist():
    required_notebooks = [
        "notebooks/00_orientation.ipynb",
        "notebooks/01_data_loading.ipynb",
        "notebooks/02_data_quality_cleaning.ipynb",
        "notebooks/03_exploratory_analysis.ipynb",
        "notebooks/04_descriptive_statistics.ipynb",
        "notebooks/05_correlation_regression.ipynb",
        "notebooks/06_case_study_template.ipynb",
    ]
    for notebook in required_notebooks:
        assert Path(notebook).exists(), f"Missing notebook: {notebook}"
