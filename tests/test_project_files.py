from pathlib import Path
import sys
import pytest


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
        "docs/02-ai-usage-policy.md",
        "docs/03-faq-troubleshooting.md",
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


def test_synthetic_data_exists_or_can_be_generated():
    """Verifikasi bahwa data sintetis ada, atau script generator bisa dijalankan."""
    synthetic_file = Path("data/synthetic/synthetic_student_performance.csv")
    
    if synthetic_file.exists():
        # File sudah ada, cek ukurannya
        size_kb = synthetic_file.stat().st_size / 1024
        assert size_kb > 100, f"Synthetic data file too small ({size_kb:.1f}KB), might be corrupted"
    else:
        # File tidak ada, coba generate dengan script
        sys.path.insert(0, str(Path("scripts").resolve()))
        from generate_synthetic_student_data import main
        
        main()  # Ini akan raise exception jika gagal
        assert synthetic_file.exists(), "Failed to generate synthetic data"


def test_generator_script_has_main():
    """Verifikasi bahwa script generator punya fungsi main() yang bisa dipanggil."""
    sys.path.insert(0, str(Path("scripts").resolve()))
    
    from generate_synthetic_student_data import generate_synthetic_student_data, main
    
    # Cek bahwa fungsi ada dan callable
    assert callable(generate_synthetic_student_data), "generate_synthetic_student_data harus callable"
    assert callable(main), "main() harus callable"


def test_required_prompts_exist():
    """Verifikasi kehadiran prompt yang dirujuk di notebook."""
    required_prompts = [
        "prompts/prompt_01_explain_code.md",
        "prompts/prompt_02_choose_method.md",
        "prompts/prompt_03_interpret_results.md",
        "prompts/prompt_04_reflect_on_limitations.md",
    ]
    for prompt_file in required_prompts:
        assert Path(prompt_file).exists(), f"Missing prompt file: {prompt_file}"
        assert Path(prompt_file).stat().st_size > 0, f"Prompt file is empty: {prompt_file}"


def test_required_templates_have_content():
    """Verifikasi bahwa template files punya konten (bukan kosong)."""
    required_templates = [
        "templates/ai_usage_log_template.md",
        "templates/method_selection_template.md",
        "templates/interpretation_template.md",
    ]
    for template_file in required_templates:
        assert Path(template_file).exists(), f"Missing template: {template_file}"
        size = Path(template_file).stat().st_size
        assert size > 100, f"Template file too small ({size} bytes), might be corrupted: {template_file}"


def test_gitignore_excludes_processed_data():
    """Verifikasi bahwa .gitignore mengabaikan processed data files."""
    gitignore_path = Path(".gitignore")
    assert gitignore_path.exists(), ".gitignore file not found"
    
    content = gitignore_path.read_text()
    assert "data/processed" in content, ".gitignore should exclude data/processed files"
