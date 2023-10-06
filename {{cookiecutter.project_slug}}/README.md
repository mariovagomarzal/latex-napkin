# << cookiecutter.project_slug >>

<% if cookiecutter.pythontex or cookiecutter.minted %>
## Requirements
You need to have Python installed on your system. We recommend using
a virtual environment to install the required packages:

```bash
python -m venv "venv"
source "venv/bin/activate" # This may be different depending on your shell
```

Then, install the required packages:

```bash
pip install -r requirements.txt
```

<% endif %>
## Compile

Run the following command from the root of the project to compile the
document:

```bash
latexmk main.tex
```
