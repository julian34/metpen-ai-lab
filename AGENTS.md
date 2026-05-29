# Agent Instructions

This project is a Python and Jupyter-based reproducible lab environment (Metpen AI Lab) designed for learning research methods with responsible AI.

## Project Architecture & Conventions

- **Language of Instruction:** The primary language for documentation and notebooks in this project is **Indonesian**. When generating notebook content, comments, or UI texts, use Indonesian unless requested otherwise.
- **Data Context:** The current raw data in `data/synthetic/` is synthetic. It is intended for workflow learning only and must not be treated as real-world empirical evidence.
- **Dependency Management:** Dependencies are defined in `requirements.txt` but are installed during the Dev Container Docker image build. Do not add `pip install` commands directly into notebooks or ask the user to run them in `postCreateCommand`.
- **Testing:** This project uses `pytest`. Test files are located in the `tests/` directory. Run them using `pytest tests/`.

## Important Links

- **AI Usage Policy:** When questions arise about what is allowed, refer the user to [docs/02-ai-usage-policy.md](docs/02-ai-usage-policy.md). Ensure any AI-assisted workflow adheres to these rules (e.g. fill the AI Usage Log for substantial changes).
- **Templates:** Use files in [templates/](templates) when structuring outputs like interpretation of results or method selection.
- **Prompts:** There are reusable prompts located in [prompts/](prompts). Use them as a reference when assisting with AI interactions for analysis or code explanation.

## Workflows

When guiding a user on a notebook:
1. Load dataset (e.g. from `data/synthetic/`)
2. Perform cleaning, output to `data/processed/`
3. Emphasize methodological reasoning instead of just giving the final code. Help the user reflect and understand.