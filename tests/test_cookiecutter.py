"""Test the template rendering."""
from pathlib import Path
import pytest


# Constants and auxiliary functions
DEFAULT_CONTEXT = {
    "project_slug": "latex-napkin",
    "author": "Your Name",
    "title": "Title",
    "date": "\\today",
    "documentclass": "article",
    "documentoptions": "a4paper, 11pt",
    "language": "english",
    "math_numeration": "section",
    "twoside": True,
    "minted": True,
    "pythontex": True,
}

LANGUAGE_NAMES = {
    "english": ["Theorem", "Definition", "Example", "Exercise"],
    "spanish": ["Teorema", "Definición", "Ejemplo", "Ejercicio"],
    "catalan": ["Teorema", "Definició", "Exemple", "Exercici"],
}

def path_without_braces(path: Path):
    """Return the path without curly braces."""
    return Path(str(path).replace("{", "").replace("}", ""))

def check_gitignore(project_path, minted, pythontex):
    """Check the .gitignore file."""
    gitignore_path = project_path / ".gitignore"

    # Check that the file exists
    assert gitignore_path.is_file()

    # Check that the file contains the correct lines
    gitignore_content = gitignore_path.read_text()
    assert "### TeX .gitignore" in gitignore_content

    python_line = "### Python .gitignore"
    if minted or pythontex:
        assert python_line in gitignore_content
    else:
        assert python_line not in gitignore_content

def check_readme(project_path, project_slug, minted, pythontex):
    """Check the README file."""
    readme_path = project_path / "README.md"

    # Check that the file exists
    assert readme_path.is_file()

    # Check that the file contains the correct lines
    readme_content = readme_path.read_text()
    assert f"# {project_slug}" in readme_content

    python_line = "## Requirements"
    if minted or pythontex:
        assert python_line in readme_content
    else:
        assert python_line not in readme_content

def check_requirements(project_path, minted, pythontex):
    """Check the requirements.txt file."""
    requirements_path = project_path / "requirements.txt"

    # Check that the file exists (or not)
    if minted or pythontex:
        assert requirements_path.is_file()
    else:
        assert not requirements_path.is_file()

def check_latexmkrc(project_path, minted, pythontex):
    """Check the .latexmkrc file."""
    latexmkrc_path = project_path / ".latexmkrc"

    # Check that the file exists
    assert latexmkrc_path.is_file()

    # Check that the file contains the correct lines
    latexmkrc_content = latexmkrc_path.read_text()
    assert "# Use luaLaTeX" in latexmkrc_content

    pythontex_line = "# Support for pythontex"
    if pythontex:
        assert pythontex_line in latexmkrc_content
    else:
        assert pythontex_line not in latexmkrc_content

    shell_escape_line = "-shell-escape"
    if minted or pythontex:
        assert shell_escape_line in latexmkrc_content
    else:
        assert shell_escape_line not in latexmkrc_content

def check_main(
    project_path,
    author,
    title,
    date,
    documentclass,
    documentoptions,
    twoside,
):
    """Check the main.tex file."""
    main_path = project_path / "main.tex"

    # Check that the file exists
    assert main_path.is_file()

    # Check that the file contains the correct lines
    main_content = main_path.read_text()
    assert f"\\title{{{title}}}" in main_content
    assert f"\\author{{{author}}}" in main_content
    assert f"\\date{{{date}}}" in main_content
    assert documentclass in main_content
    assert documentoptions in main_content

    # Check that the file contains the correct lines for twoside
    if (documentclass == "book") and not twoside:
        assert "oneside" in main_content
    elif (documentclass != "book") and twoside:
        assert "twoside" in main_content
    else:
        assert "oneside" not in main_content
        assert "twoside" not in main_content

# Preamble checks
def check_preamble_language(preamble_content, language):
    """Check the preamble.tex file for the language."""
    # Check document langugage
    assert language in preamble_content

    # Check math names
    for name in LANGUAGE_NAMES[language]:
        assert name in preamble_content

def check_preamble_minted(preamble_content, minted):
    """Check the preamble.tex file for minted."""
    if minted:
        assert "minted" in preamble_content
    else:
        assert "minted" not in preamble_content

def check_preamble_pythontex(preamble_content, pythontex):
    """Check the preamble.tex file for pythontex."""
    if pythontex:
        assert "pythontex" in preamble_content
    else:
        assert "pythontex" not in preamble_content

def check_preamble_section_titles(preamble_content, documentclass):
    """Check the preamble.tex file for section titles."""
    if documentclass != "article":
        assert "\\part" in preamble_content
        assert "\\chapter" in preamble_content
    else:
        assert "\\part" not in preamble_content
        assert "\\chapter" not in preamble_content

def check_preamble_headers(preamble_content, documentclass, twoside):
    """Check the preamble.tex file for headers."""
    if twoside:
        if documentclass != "article":
            assert "% Chapter and section titles in headers"\
                in preamble_content
        else:
            assert "% Section and subsection titles in headers"\
                in preamble_content
    else:
        if documentclass != "article":
            assert "% Chapter titles in headers"\
                in preamble_content
        else:
            assert "% Section titles in headers"\
                in preamble_content

def check_preamble_math_numeration(preamble_content, math_numeration):
    """Check the preamble.tex file for math numeration."""
    if math_numeration != "plain":
        assert f"numberwithin={math_numeration}" in preamble_content
    else:
        assert "numberwithin" not in preamble_content

def check_preamble(project_path, context):
    """Check the preamble.tex file."""
    # Check that the file exists
    preamble_path = project_path / "tex" / "preamble.tex"
    assert preamble_path.is_file()

    # Check that the file contains the correct lines
    preamble_content = preamble_path.read_text()
    check_preamble_language(preamble_content, context["language"])
    check_preamble_minted(preamble_content, context["minted"])
    check_preamble_pythontex(preamble_content, context["pythontex"])
    check_preamble_section_titles(
        preamble_content,
        context["documentclass"]
    )
    check_preamble_headers(
        preamble_content,
        context["documentclass"],
        context["twoside"],
    )
    check_preamble_math_numeration(
        preamble_content,
        context["math_numeration"]
    )

def check_macros(project_path):
    """Check the macros.tex file."""
    macros_path = project_path / "tex" / "macros.tex"

    # Check that the file exists
    assert macros_path.is_file()

# Fixtures
@pytest.fixture(
    params=[
        {}, # Default context
        # Language and custom content entries
        {
            "documentclass": "report",
            "documentoptions": "a4paper, 12pt",
            "author": "John Doe",
            "title": "My Title",
            "date": "My Date",
            "language": "spanish",
        },
        {
            "documentclass": "book",
            "langugage": "catalan",
        },
        # Twoside and documentclass
        {
            "documentclass": "book",
            "twoside": False,
        },
        {
            "documentclass": "report",
            "twoside": False,
        },
        {
            "documentclass": "article",
            "twoside": False,
        },
        # Math numeration
        {
            "math_numeration": "chapter",
        },
        {
            "math_numeration": "plain",
        },
        # Minted and pythontex
        {
            "minted": False,
            "pythontex": False,
        },
        {
            "minted": False,
            "pythontex": True,
        },
        {
            "minted": True,
            "pythontex": False,
        },
    ],
    ids=[
        "default",
        "spanish",
        "catalan",
        "book_oneside",
        "report_oneside",
        "article_oneside",
        "math_chapter",
        "math_plain",
        "no_minted_no_pythontex",
        "no_minted",
        "no_pythontex",
    ],
)
def context(request):
    """Return the context for the template."""
    return DEFAULT_CONTEXT | request.param


# Tests
def test_cookiecutter_template(cookies, context):
    result = cookies.bake(extra_context=context)
    path = path_without_braces(result.project_path)

    # Check that the project was created
    assert result.exit_code == 0
    assert result.exception is None
    assert path.is_dir()
    assert path.name == context["project_slug"]

    # Check validitity of the files
    check_gitignore(
        path,
        context["minted"],
        context["pythontex"],
    )
    check_readme(
        path,
        context["project_slug"],
        context["minted"],
        context["pythontex"],
    )
    check_requirements(
        path,
        context["minted"],
        context["pythontex"],
    )
    check_latexmkrc(
        path,
        context["minted"],
        context["pythontex"],
    )
    check_main(
        path,
        context["author"],
        context["title"],
        context["date"],
        context["documentclass"],
        context["documentoptions"],
        context["twoside"],
    )
    check_preamble(
        path,
        context,
    )
    check_macros(
        path,
    )
