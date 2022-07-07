# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['mdsplit']
entry_points = \
{'console_scripts': ['mdsplit = mdsplit:run']}

setup_kwargs = {
    'name': 'mdsplit',
    'version': '0.2',
    'description': 'Split markdown files at headings',
    'long_description': "# mdsplit\n\n`mdsplit` is a python command line tool to\n**split markdown files** into chapters\n**at (a user-defined) [ATX heading](https://spec.commonmark.org/0.30/#atx-headings) level**.\n\nEach chapter (or subchapter) is written to its own file,\nwhich is named after the heading title.\nThese files are written to subdirectories representing the document's structure.\n\n**Note:**\n- The output is *guaranteed to be identical* with the input\n  (except for the separation into multiple files of course).\n    - This means: no touching of whitespace or changing `-` to `*` of your lists\n      like some viusual markdown editors tend to do.\n- Text before the first heading is written to a file with the same name as the markdown file.\n- Chapters with the same heading name are written to the same file.\n\n**Limitations:**\n- [Setext headings](https://spec.commonmark.org/0.30/#setext-headings) are not supported\n\n## Installation\n\nEither use pip:\n\n    pip install mdsplit\n    mdsplit\n\nOr simply download [mdsplit.py](mdsplit.py) and run it (it does not use any dependencies but python itself):\n\n    python3 mdsplit.py\n\n## Usage\n\n**Split by heading 1** and write to an output folder based on the input name \n\n```bash\nmdsplit in.md\n```\n\n```mermaid\n%%{init: {'themeVariables': { 'fontFamily': 'Monospace', 'text-align': 'left'}}}%%\nflowchart LR\n    subgraph in.md\n        SRC[# Heading 1<br>lorem ipsum<br><br># HeadingTwo<br>dolor sit amet<br><br>## Heading 2.1<br>consetetur sadipscing elitr]\n    end\n    SRC --> MDSPLIT(mdsplit in.md)\n    MDSPLIT --> SPLIT_A\n    MDSPLIT --> SPLIT_B\n    subgraph in/HeadingTwo.md\n        SPLIT_B[# HeadingTwo<br>dolor sit amet<br><br>## Heading 2.1<br>consetetur sadipscing elitr]\n    end\n    subgraph in/Heading 1.md\n        SPLIT_A[# Heading 1<br>lorem ipsum<br><br>]\n    end\n    style SRC text-align:left\n    style SPLIT_A text-align:left\n    style SPLIT_B text-align:left\n    style MDSPLIT fill:#000,color:#0F0\n```\n\n**Split by heading 2**\n\n```bash\nmdsplit in.md --max-level 2 --output out\n```\n\n```mermaid\n%%{init: {'themeVariables': { 'fontFamily': 'Monospace', 'text-align': 'left'}}}%%\nflowchart LR\n    subgraph in.md\n        SRC[# Heading 1<br>lorem ipsum<br><br># HeadingTwo<br>dolor sit amet<br><br>## Heading 2.1<br>consetetur sadipscing elitr]\n    end\n    SRC --> MDSPLIT(mdsplit in.md -l 2 -o out)\n    subgraph out/HeadingTwo/Heading 2.1.md\n        SPLIT_C[## Heading 2.1<br>consetetur sadipscing elitr]\n    end\n    subgraph out/HeadingTwo.md\n        SPLIT_B[# HeadingTwo<br>dolor sit amet<br><br>]\n    end\n    subgraph out/Heading 1.md\n        SPLIT_A[# Heading 1<br>lorem ipsum<br><br>]\n    end\n    MDSPLIT --> SPLIT_A\n    MDSPLIT --> SPLIT_B\n    MDSPLIT --> SPLIT_C\n    style SRC text-align:left\n    style SPLIT_A text-align:left\n    style SPLIT_B text-align:left\n    style MDSPLIT fill:#000,color:#0F0\n```\n\n## Development\n\nInstall [poetry](https://python-poetry.org)\n\nPrepare virtual environment and download dependencies\n\n    poetry install\n\nRun tests\n\n    poetry run pytest\n\nRelease new version\n\n    poetry build\n    poetry publish\n\n[Download statistics](https://pypistats.org/packages/mdsplit)",
    'author': 'Markus Straub',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/markusstraub/mdsplit',
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
