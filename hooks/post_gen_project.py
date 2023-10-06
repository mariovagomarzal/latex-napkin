from pathlib import Path


keep_requirements = {{ cookiecutter.pythontex or cookiecutter.minted }}

if not keep_requirements:
    Path("requirements.txt").unlink()
