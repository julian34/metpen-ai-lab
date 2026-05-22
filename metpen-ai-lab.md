# metpen-ai-lab — Refined Implementation Plan

> Workspace name: **metpen-ai-lab**  
> Purpose: a reproducible VS Code + Dev Container + Python/Jupyter lab for research methods learning with responsible AI assistance.  
> Implementation style: **deterministic, explicit, minimal-but-not-over-simplified, and low-hallucination**.

---

## 0. Implementation guardrails for the AI agent

Follow these rules strictly.

1. **Do not invent requirements.** Only create files, folders, notebooks, scripts, and datasets listed in this plan.
2. **Do not invent real-data provenance.** If a real dataset is not downloaded from a verified public source, do not claim it is real.
3. **Synthetic data must be labeled synthetic everywhere.** Never present synthetic data as real empirical evidence.
4. **Use relative paths only.** Do not use personal machine paths such as `/Users/...`, `C:\...`, or `/home/...` except container-controlled project paths.
5. **Keep notebooks beginner-friendly.** Prefer clear Markdown explanations over complex code.
6. **Do not add optional tools unless listed.** Avoid extra frameworks, dashboards, databases, cloud services, authentication flows, or unexplained dependencies.
7. **When uncertain, create a placeholder with TODO instead of guessing.**
8. **Prioritize reproducibility over completeness.** A working 7-notebook teaching lab is the goal for the first implementation.
9. **Do not add public publishing steps, GitHub Classroom, autograding, or advanced CI** until the first implementation passes the stop condition.
10. **Do not use `postCreateCommand` for dependency installation.** Dependencies must be installed in the Docker image through `.devcontainer/Dockerfile`.

---

## 1. Learning language preference

Before generating notebooks, documentation, prompts, README text, chart explanations, and other student-facing content, ask the user:

```text
What language should the learning materials be presented in?
```

If the user does not answer, use **English** as the default language.

Apply the selected language consistently to:

- notebook Markdown explanations;
- learning outcomes;
- chart explanations;
- interpretation examples;
- reflection questions;
- README student instructions;
- AI usage policy;
- prompt templates;
- troubleshooting notes.

Keep these technical elements in English unless the user explicitly requests otherwise:

- folder names;
- file names;
- Python variable names;
- function names;
- package names;
- command-line commands.

Language rule for the implementation agent:

- Ask the language question before creating student-facing content.
- If there is no answer, default to English.
- Do not randomly mix languages.
- Keep technical identifiers in English for portability.

---

## 2. Required workflow: create Dev Container first

This project must be implemented inside a VS Code Dev Container.

Start locally only to create the folder structure and Dev Container files. After the Dev Container config exists, stop local work and reopen in container.

In VS Code:

1. Open the folder `metpen-ai-lab`.
2. Press `Ctrl+Shift+P` or `Cmd+Shift+P`.
3. Run **Dev Containers: Reopen in Container**.
4. Wait until the container finishes building.
5. Continue all remaining implementation inside the Dev Container session.

Important design choice:

- `devcontainer.json` must **not** use `postCreateCommand` for dependency installation.
- Python dependencies must be installed in `.devcontainer/Dockerfile` so they are baked into the Docker image.
- The Jupyter kernel must also be registered from the Dockerfile.
- If `requirements.txt` changes, rebuild the Dev Container image.

---

## 3. Balanced first-version scope

The original full plan had 10 notebooks. The first implementation should not be reduced too far, because correlation/regression and case-study work are important for research-method learning.

Therefore, implement **7 core notebooks** now:

```text
notebooks/
├── 00_orientation.ipynb
├── 01_data_loading.ipynb
├── 02_data_quality_cleaning.ipynb
├── 03_exploratory_analysis.ipynb
├── 04_descriptive_statistics.ipynb
├── 05_correlation_regression.ipynb
└── 06_case_study_template.ipynb
```

Keep the remaining original notebooks as future expansion only:

```text
future_notebooks/
├── hypothesis_testing.ipynb
├── reporting_template.ipynb
└── final_project_starter.ipynb
```

Do **not** create `future_notebooks/` in the first implementation. It is listed only to preserve the roadmap.

---

## 4. Minimal target structure for first implementation

Create only this structure for the first working version:

```text
metpen-ai-lab/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .vscode/
│   ├── settings.json
│   └── extensions.json
├── README.md
├── .gitignore
├── requirements.txt
├── docs/
│   ├── 01-how-to-open-in-devcontainer.md
│   ├── 02-ai-usage-policy.md
│   └── 03-faq-troubleshooting.md
├── data/
│   ├── raw/
│   │   └── README.md
│   ├── synthetic/
│   │   ├── README.md
│   │   └── synthetic_student_performance.csv
│   └── processed/
│       └── .gitkeep
├── notebooks/
│   ├── 00_orientation.ipynb
│   ├── 01_data_loading.ipynb
│   ├── 02_data_quality_cleaning.ipynb
│   ├── 03_exploratory_analysis.ipynb
│   ├── 04_descriptive_statistics.ipynb
│   ├── 05_correlation_regression.ipynb
│   └── 06_case_study_template.ipynb
├── prompts/
│   ├── prompt_01_explain_code.md
│   ├── prompt_02_choose_method.md
│   ├── prompt_03_interpret_results.md
│   └── prompt_04_reflect_on_limitations.md
├── scripts/
│   └── generate_synthetic_student_data.py
├── templates/
│   ├── ai_usage_log_template.md
│   ├── method_selection_template.md
│   └── interpretation_template.md
└── tests/
    ├── test_imports.py
    └── test_project_files.py
```

Removed from the first implementation to reduce hallucination risk:

- GitHub Actions workflow;
- version tags and publication workflow;
- GitHub Classroom integration;
- autograding;
- advanced notebook checking;
- many optional example files;
- unnecessary utility modules;
- optional package managers;
- final-project scaffolding before the basic lab works.

These can be added later after the basic repo runs successfully.

---

## 5. Phase A — Local bootstrap only

Run locally:

```bash
mkdir metpen-ai-lab
cd metpen-ai-lab
mkdir -p .devcontainer .vscode docs data/raw data/synthetic data/processed notebooks prompts scripts templates tests
```

Create the files in sections 5.1–5.3, then immediately reopen in Dev Container.

Dependencies are installed inside the Docker image through the Dockerfile, not through `postCreateCommand`.

### 5.1 `.devcontainer/devcontainer.json`

```json
{
  "name": "metpen-ai-lab",
  "build": {
    "dockerfile": "Dockerfile",
    "context": ".."
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-toolsai.jupyter",
        "ms-toolsai.datawrangler",
        "GitHub.copilot",
        "GitHub.copilot-chat",
        "yzhang.markdown-all-in-one"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "jupyter.askForKernelRestart": false,
        "files.autoSave": "afterDelay",
        "editor.formatOnSave": true,
        "notebook.lineNumbers": "on"
      }
    }
  },
  "remoteUser": "vscode"
}
```

Notes:

- Do not add `postCreateCommand` here.
- Keep `devcontainer.json` focused on container build configuration, VS Code extensions, and editor settings.
- Dependency installation belongs in the Dockerfile.

### 5.2 `.devcontainer/Dockerfile`

```dockerfile
FROM mcr.microsoft.com/devcontainers/python:3.11

RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspaces/metpen-ai-lab

COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && python -m ipykernel install --sys-prefix --name metpen-ai-lab --display-name "Python (metpen-ai-lab)"
```

Why dependencies are installed here:

- The image becomes self-contained for the lab dependencies.
- Students do not need a separate package-install step after the container is created.
- The environment is more reproducible because dependency installation is part of the image build.

If `requirements.txt` is updated, rebuild the Dev Container.

### 5.3 `requirements.txt`

```txt
jupyter
ipykernel
nbformat
pandas
numpy
matplotlib
seaborn
scipy
statsmodels
scikit-learn
openpyxl
missingno
pytest
```

### 5.4 Mandatory stop point

After these three files exist, stop and run:

```text
Dev Containers: Reopen in Container
```

Do not continue creating notebooks or datasets until the workspace is running inside the container.

---

## 6. Phase B — Continue inside Dev Container

### 6.1 Create `.gitignore`

```gitignore
__pycache__/
*.py[cod]
.ipynb_checkpoints/
.pytest_cache/
.env
.venv/
env/
.DS_Store
*.log
data/processed/*.csv
data/processed/*.xlsx
```

### 6.2 Create `.vscode/extensions.json`

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-toolsai.jupyter",
    "ms-toolsai.datawrangler",
    "GitHub.copilot",
    "GitHub.copilot-chat",
    "yzhang.markdown-all-in-one"
  ]
}
```

### 6.3 Create `.vscode/settings.json`

```json
{
  "python.defaultInterpreterPath": "/usr/local/bin/python",
  "editor.formatOnSave": true,
  "notebook.lineNumbers": "on",
  "files.autoSave": "afterDelay"
}
```

---

## 7. Dataset plan

### 7.1 Synthetic dataset for first implementation

Create one synthetic dataset first:

```text
data/synthetic/synthetic_student_performance.csv
```

Minimum requirements:

- at least 2,000 rows;
- no real names;
- no private information;
- clear synthetic label in `data/synthetic/README.md`;
- realistic relationships between variables;
- some missing values;
- a small number of duplicates for cleaning practice.

Required columns:

```text
student_id
cohort_year
program
semester
attendance_rate
assignment_score
quiz_average
midterm_score
final_exam_score
lms_logins
study_hours_per_week
internet_access
part_time_work_hours
commute_minutes
ai_tool_usage_frequency
previous_gpa
final_grade
passed
submission_delay_days
missing_reason_flag
```

Rules for realistic generation:

- `attendance_rate`, `assignment_score`, `quiz_average`, `midterm_score`, `final_exam_score`, `previous_gpa`, and `study_hours_per_week` should have plausible numeric ranges.
- `final_grade` should depend partly on attendance, assignments, quizzes, midterm, final exam, and previous GPA.
- `part_time_work_hours` may reduce study hours slightly.
- `submission_delay_days` may reduce assignment score slightly.
- Missingness should not be completely random everywhere.
- Duplicate rows should be rare and intentional for cleaning exercises.

### 7.2 Real dataset rule

For the first implementation, do not include a real dataset unless its source and license are documented in `data/raw/README.md`.

Use this placeholder first:

```md
# Raw Data

No real dataset is included yet.

When adding a real dataset, document:

- dataset name;
- source URL;
- license or terms of use;
- download date;
- original file name;
- variables used in the notebooks;
- any modification made before storing it here.
```

This avoids false claims about data provenance.

---

## 8. Synthetic data generator

Create:

```text
scripts/generate_synthetic_student_data.py
```

The script should:

1. use a fixed random seed;
2. generate at least 2,000 base rows;
3. create all required columns;
4. add realistic missing values;
5. add a few duplicate rows;
6. save the CSV to `data/synthetic/synthetic_student_performance.csv`;
7. print the final row and column count.

Do not use external APIs or internet access in the script.

---

## 9. Notebook design standard

Each notebook must use the same teaching structure:

1. Title
2. Learning outcomes
3. Short concept explanation
4. Why it matters in research methods
5. Code example
6. Output interpretation
7. Student task
8. Reflection question
9. AI-use suggestion
10. Common mistakes or caution note

Do not create overly complex notebooks. Each notebook should run top-to-bottom without manual changes.

### 9.1 Chart explanation template

Every visualization must include this Markdown structure:

```md
### What this chart shows

[Explain the variables shown.]

### Why this chart is appropriate

[Explain why this chart type fits the question.]

### Pattern observed

[Describe the visible pattern carefully.]

### Caution

[Explain what cannot be concluded from the chart alone.]
```

### 9.2 Interpretation style rule

Use cautious academic language. Avoid claiming causality unless the design supports it.

Example:

```text
The pattern suggests an association between attendance and final grade. However, this chart alone does not show that attendance causes higher grades. Other variables, such as prior achievement or study time, may also influence the result.
```

---

## 10. Required notebooks

### 10.1 `00_orientation.ipynb`

Purpose:

- confirm that the Dev Container works;
- introduce the project structure;
- explain responsible AI use;
- run a small Python check.

Required cells:

1. Markdown: welcome and learning outcomes
2. Markdown: how to run cells
3. Markdown: project folder map
4. Code: import `pandas`, `numpy`, `matplotlib`
5. Code: print Python version
6. Code: confirm current working directory
7. Markdown: reflection question

### 10.2 `01_data_loading.ipynb`

Purpose:

- load the synthetic CSV;
- inspect rows, columns, data types, and basic summaries.

Required cells:

1. Markdown: why data loading matters
2. Code: read `data/synthetic/synthetic_student_performance.csv`
3. Code: show `head()`, `tail()`, and `shape`
4. Code: show `info()`
5. Code: show `describe()`
6. Code: show value counts for selected categorical variables
7. Markdown: interpretation prompts
8. Markdown: student task

### 10.3 `02_data_quality_cleaning.ipynb`

Purpose:

- inspect missing values;
- identify duplicates;
- apply simple cleaning;
- create a cleaned version in `data/processed/`.

Required cells:

1. Markdown: why data quality matters
2. Code: count missing values
3. Code: visualize or summarize missingness
4. Code: count duplicate rows
5. Code: simple cleaning steps
6. Code: save `data/processed/student_performance_cleaned.csv`
7. Markdown: cleaning decision reflection

### 10.4 `03_exploratory_analysis.ipynb`

Purpose:

- create simple charts;
- compare groups;
- practice cautious visual interpretation.

Required charts:

1. Histogram of `final_grade`
2. Boxplot of `final_grade` by `program`
3. Scatter plot of `attendance_rate` and `final_grade`
4. Bar chart or count plot for one categorical variable

Each chart must have a Markdown explanation using the chart explanation template.

### 10.5 `04_descriptive_statistics.ipynb`

Purpose:

- calculate central tendency and dispersion;
- compare grouped descriptive summaries;
- choose appropriate summary statistics for variable types.

Required cells:

1. Markdown: what descriptive statistics are
2. Code: mean, median, min, max, standard deviation for selected numeric variables
3. Code: grouped summaries by `program`
4. Code: grouped summaries by `internet_access`
5. Markdown: when mean is useful and when median may be safer
6. Markdown: student task
7. Markdown: reflection on what descriptive statistics can and cannot prove

### 10.6 `05_correlation_regression.ipynb`

Purpose:

- distinguish correlation from causation;
- inspect relationships between variables;
- run a simple regression;
- interpret coefficients cautiously.

Required cells:

1. Markdown: correlation vs causation
2. Code: select numeric variables for correlation
3. Code: correlation matrix for selected variables
4. Code: scatter plot of `attendance_rate` and `final_grade`
5. Code: simple linear regression predicting `final_grade` from `attendance_rate`
6. Code: expanded regression using selected predictors such as `attendance_rate`, `previous_gpa`, `study_hours_per_week`, and `submission_delay_days`
7. Markdown: interpretation of coefficient direction and uncertainty
8. Markdown: limitations and possible confounders
9. Markdown: student task to test another predictor

Caution requirement:

- Explicitly state that regression on this synthetic observational-style dataset does not prove causality.

### 10.7 `06_case_study_template.ipynb`

Purpose:

- provide a semi-guided template for students to apply the workflow;
- connect research question, dataset understanding, method choice, analysis, interpretation, and limitations.

Required sections:

1. Case title
2. Research question
3. Dataset description
4. Variables selected
5. Data quality checks
6. Descriptive summary
7. Visualization
8. Method choice and justification
9. Analysis
10. Interpretation
11. Limitations
12. AI usage disclosure placeholder
13. Final reflection

The notebook should contain placeholders where students write their own answers.

---

## 11. Prompt files

### 11.1 `prompts/prompt_01_explain_code.md`

```md
Explain the following Python code in plain academic language.

Describe:

1. what the code does;
2. why it is useful for research methods;
3. what assumptions or risks I should check;
4. how I should interpret the output.

Do not only paraphrase the code. Connect it to reasoning.
```

### 11.2 `prompts/prompt_02_choose_method.md`

```md
I have this research question:
[insert question]

My variables are:
[insert variables]

My dataset characteristics are:
[insert sample size, variable types, missing values]

Suggest 2 possible methods.

For each method, explain:

- when it is appropriate;
- what assumptions I should check;
- what the output can answer;
- what the method cannot prove.

Do not make causal claims unless the design supports causality.
```

### 11.3 `prompts/prompt_03_interpret_results.md`

```md
I ran this analysis:
[insert method]

Here is the result:
[insert result]

Help me write a cautious interpretation in academic style.

Requirements:

- do not exaggerate causality;
- mention uncertainty or limitations;
- explain what the result supports;
- explain what it does not support.
```

### 11.4 `prompts/prompt_04_reflect_on_limitations.md`

```md
Based on this dataset and method, what are possible limitations of the analysis?

Focus on:

- sample limitations;
- measurement limitations;
- missing data;
- inappropriate generalization;
- possible confounders;
- limitations caused by synthetic or simulated data if applicable.
```

---

## 12. Responsible AI policy

Create `docs/02-ai-usage-policy.md`.

```md
# Responsible Use of AI

AI tools may be used to:

- explain code;
- debug errors;
- compare possible methods;
- improve writing clarity;
- help organize notebook structure.

AI tools may not be used to:

- fabricate data provenance;
- fabricate findings;
- submit analysis without verification;
- replace the student's own methodological reasoning;
- present synthetic data as real-world evidence.

Students must:

- verify all code before submission;
- explain why a method was chosen;
- disclose substantial AI assistance;
- revise AI-generated text critically;
- complete the AI Usage Log when AI substantially influenced the work.
```

---

## 13. Templates

### 13.1 `templates/ai_usage_log_template.md`

```md
# AI Usage Log

## Tool used

[fill in]

## Date

[fill in]

## Task

What were you trying to do?

## Prompt or request

What did you ask?

## Output summary

What did the AI suggest?

## What I accepted

What did you keep?

## What I changed

What did you modify?

## Verification

How did you verify correctness?

## Reflection

What did you learn?
```

### 13.2 `templates/method_selection_template.md`

```md
# Method Selection Template

## Research question

[write here]

## Variables

- Outcome variable:
- Predictor/grouping variable(s):
- Control or contextual variable(s):

## Candidate methods

1. [method 1]
2. [method 2]

## Selected method

[write here]

## Justification

Explain why this method fits the research question and variables.

## Assumptions or cautions

List assumptions, risks, or limitations.
```

### 13.3 `templates/interpretation_template.md`

```md
# Interpretation Template

## Result being interpreted

[insert result]

## What the result suggests

[write cautiously]

## What the result does not prove

[write limitation]

## Possible alternative explanations

[write here]

## Next analysis step

[write here]
```

---

## 14. README content

Create `README.md`.

```md
# metpen-ai-lab

A reproducible VS Code + Python + Jupyter lab for learning research methods with responsible AI assistance.

## Start here

Use the Dev Container workflow.

1. Install Docker.
2. Install VS Code.
3. Install the Dev Containers extension.
4. Open this folder in VS Code.
5. Run `Dev Containers: Reopen in Container`.
6. Open `notebooks/00_orientation.ipynb`.

## What students will learn

- Load and inspect datasets.
- Identify basic data quality issues.
- Clean and save processed data.
- Create simple visualizations.
- Calculate descriptive statistics.
- Explore correlation and simple regression.
- Build a small case-study analysis.
- Write cautious interpretations.
- Use AI tools responsibly and transparently.

## Folder guide

- `notebooks/`: guided learning notebooks.
- `data/synthetic/`: synthetic practice dataset.
- `data/processed/`: cleaned outputs generated by notebooks.
- `docs/`: setup notes and AI policy.
- `prompts/`: reusable AI prompts.
- `templates/`: reusable learning templates.
- `scripts/`: dataset generation script.
- `tests/`: basic project checks.

## Important note about data

The first version uses synthetic data for practice. Synthetic data is useful for learning workflows but must not be treated as real empirical evidence.

## Dev Container note

Dependencies are installed during Docker image build through `.devcontainer/Dockerfile`. This project intentionally does not use `postCreateCommand` for dependency installation.
```

---

## 15. Basic tests

### 15.1 `tests/test_imports.py`

```python
def test_imports():
    import pandas
    import numpy
    import matplotlib
    import seaborn
    import scipy
    import statsmodels
    import sklearn
```

### 15.2 `tests/test_project_files.py`

```python
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
```

Run:

```bash
pytest
```

---

## 16. Simple implementation checklist

### Environment

- [ ] Dev Container builds successfully.
- [ ] `devcontainer.json` does not contain `postCreateCommand`.
- [ ] Python packages are installed during Docker image build.
- [ ] Jupyter kernel appears as `Python (metpen-ai-lab)` without running `postCreateCommand`.
- [ ] `pytest` runs.

### Language

- [ ] User was asked what language the learning materials should use.
- [ ] If the user did not answer, English was used.
- [ ] Student-facing explanations use one consistent language.
- [ ] Technical file names and code identifiers remain in English unless explicitly requested otherwise.

### Data

- [ ] Synthetic dataset has at least 2,000 rows.
- [ ] Synthetic dataset has the required columns.
- [ ] Synthetic data is clearly documented as synthetic.
- [ ] No real personal data is included.
- [ ] Real dataset folder does not claim provenance unless source and license are documented.

### Notebooks

- [ ] All 7 notebooks exist.
- [ ] All notebooks open in VS Code.
- [ ] All notebooks run top-to-bottom.
- [ ] Charts have explanations.
- [ ] Correlation/regression notebook explicitly warns against causal overclaiming.
- [ ] Case-study template includes method choice, interpretation, limitations, and AI disclosure.

### AI policy

- [ ] AI policy exists.
- [ ] AI usage log template exists.
- [ ] Prompts emphasize explanation, verification, and limitations.

---

## 17. Stop condition

The first implementation is complete when:

1. the Dev Container builds with Python dependencies already installed in the Docker image;
2. `devcontainer.json` contains no `postCreateCommand`;
3. the synthetic dataset is generated;
4. all 7 notebooks run in order;
5. the cleaned CSV is created in `data/processed/`;
6. `pytest` passes;
7. README tells students exactly where to start;
8. the selected learning-material language is used consistently.

Do not add public publishing steps, GitHub Classroom, autograding, advanced CI, or extra notebooks until these eight conditions are met.
