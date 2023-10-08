# latex-napkin

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter),
[latex-napkin](https://github.com/mariovagomarzal/latex-napkin) is a
LaTeX template with a custom style inspired by the nice book
[An infinitly large napkin](https://github.com/vEnhance/napkin) by
[Evan Chen](https://github.com/vEnhance) and with a few extra features
that I find useful.

## Features

- A `.latexmkrc` file that automatically compiles the document with
  `latexmk` and, if needed, with `pythontex`.
- Custom document title, section styles and headers.
- Useful math environments and macros.

## Usage

To use this template, you need to have Python and Cookiecutter installed.
Refer to the [Cookiecutter
documentation](https://cookiecutter.readthedocs.io/en/latest/installation.html)
for more information.

Then, run the following command:

```bash
cookiecutter gh:mariovagomarzal/latex-napkin
```

You will be prompted to enter a few values:
```
  [1/11] project_slug (latex-napkin):
  [2/11] author (Your Name):
  [3/11] title (Title):
  [4/11] date (\today):
  [5/11] Select documentclass
    1 - article
    2 - report
    3 - book
    Choose from [1/2/3] (1):
  [6/11] documentoptions (a4paper, 11pt):
  [7/11] Select language
    1 - english
    2 - spanish
    3 - catalan
    Choose from [1/2/3] (1):
  [8/11] Select math_numeration
    1 - section
    2 - chapter
    3 - plain
    Choose from [1/2/3] (1):
  [9/11] Select twoside
    1 - True
    2 - False
    Choose from [1/2] (1):
  [10/11] Select minted
    1 - True
    2 - False
    Choose from [1/2] (1):
  [11/11] Select pythontex
    1 - True
    2 - False
    Choose from [1/2] (1):
```

The template will be downloaded and the files will be generated in the
current directory with the following structure:

```
latex-napkin/
├── .gitignore
├── .latexmkrc
├── README.md
├── main.tex
├── requirements.txt
└── tex
    ├── macros.tex
    └── preamble.tex
```

Then, you can compile the document with `latexmk`:

```bash
latexmk main.tex
```

### Template options

- `project_slug`: The name of the directory where the files will be
  generated.
- `author`: The author of the document.
- `title`: The title of the document.
- `date`: The date of the document.
- `documentclass`: The document class. It can be `article`, `report` or
  `book`.
- `documentoptions`: The options of the document class.
- `language`: The language of the document. It can be `english`,
  `spanish` or `catalan`.
- `math_numeration`: The numeration of the math environments. It can be
    `section`, `chapter` or `plain`.
- `twoside`: Whether the document is `twoside` or `oneside`.
- `minted`: Whether the document uses `minted` or not.
- `pythontex`: Whether the document uses `pythontex` or not.

## License

This project is licensed under the terms of the
[MIT license](/LICENSE) by
[Mario Vago Marzal](https://githuh.com/mariovagomarzal).
