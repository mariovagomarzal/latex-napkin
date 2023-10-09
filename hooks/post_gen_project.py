from pathlib import Path


# Remove curly braces from the project directory name
project_dir = Path.cwd()
project_dir.rename(project_dir.parent / "{{ cookiecutter.project_slug }}")


# Delete `requirements.txt` if not needed
keep_requirements = {{ cookiecutter.pythontex or cookiecutter.minted }}

if not keep_requirements:
    Path("requirements.txt").unlink()
