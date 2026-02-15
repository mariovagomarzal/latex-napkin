from pathlib import Path


# Delete `requirements.txt` if not needed
keep_requirements = << cookiecutter.pythontex or cookiecutter.minted >>

if not keep_requirements:
    Path("requirements.txt").unlink()
