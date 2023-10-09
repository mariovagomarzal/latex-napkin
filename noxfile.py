import nox


def install_requirements(session, filename="requirements.txt"):
    """Install requirements from a file."""
    session.install("-r", filename)


@nox.session
def tests(session):
    """Run the test suite."""
    install_requirements(session)
    session.run("pytest")

@nox.session
def lint(session):
    """Lint using Ruff."""
    install_requirements(session)
    session.run("ruff", "check", ".")
