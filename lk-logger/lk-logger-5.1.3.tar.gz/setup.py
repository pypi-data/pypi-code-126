# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lk_logger', 'lk_logger.scanner']

package_data = \
{'': ['*']}

install_requires = \
['rich']

setup_kwargs = {
    'name': 'lk-logger',
    'version': '5.1.3',
    'description': 'Python advanced print with varnames.',
    'long_description': '# LK Logger\n\n[中文版](https://blog.csdn.net/Likianta/article/details/124358443)\n\nAdvanced print tool for Python.\n\n![](.assets/20220422181702.png)\n\nFeatures:\n\n-   Show source map, function name and varnames in printing.\n\n    ![](.assets/20220422183248.png)\n\n-   Easy to start. Just add two lines code to enable lk-logger.\n\n    ```python\n    # add this\n    import lk_logger\n    lk_logger.setup()\n\n    # then remain using `print` as usual...\n    print(\'Hello world\')\n    print(123, 456, 789)\n    ...\n    ```\n\n    It will replace Python\'s built-in `print` function to take care all the leftovers.\n\n-   Simple to write:\n\n    ```python\n    # before\n    a, b = 1, 2\n    print(\'a = {}, b = {}, a + b = {}\'.format(a, b, a + b))\n\n    # after\n    print(a, b, a + b)\n    ```\n\n    ![](.assets/20220422182815.png)\n\n    (Another example)\n\n    ![](.assets/20220422183714.png)\n\n-   Non-intrusive. After enable it like above, no more modifications on your source code projects (it is low-cost and low-effort to migrate). You will see the new effects at once.\n\n    This would be a good choice for developers who have dived into their projects with Python `print` to get a new start with a new logging util.\n\n-   Code highlight.\n\n    ![](.assets/20220321155834.png)\n\n## Install\n\n```shell\npip install lk-logger\n```\n\nThe latest version is 5.0.0 or higher.\n\n## Quick Start\n\n```python\nimport lk_logger\nlk_logger.setup(show_varnames=True)\n\nprint(\'hello world\')\n\na, b = 1, 2\nprint(a, b, a + b)\n\nprint(a, b, (c := a + b), c + 3)\n```\n\nScreenshot:\n\n![](.assets/20220321154014.png)\n\n## Advanced Usage\n\nUsually, the above example is enough to use.\n\nThe advanced feature is **"markup"** shorthand.\n\nUse a markup as in the first or the last parameter, the markup is a string that starts with \':\', consists of multiple marks.\n\nFor example:\n\n```python\nprint(\':i\', \'monday\')\nprint(\':i\', \'tuesday\')\nprint(\':i\', \'wednesday\')\n```\n\nIt prints weekdays with a numeric prefix:\n\n![](.assets/20220321155834.png)\n\nAnother one:\n\n```python\nimport lk_logger\nlk_logger.setup()\n\nprint(\'this is a divider\', \':d\')\n\nprint(\':v0\', \'this is a TRACE message\')\nprint(\':v1\', \'this is a DEBUG message\')\nprint(\':v2\', \'this is a INFO  message\')\nprint(\':v3\', \'this is a WARN  message\')\nprint(\':v4\', \'this is a ERROR message\')\nprint(\':v5\', \'this is a FATAL message\')\n```\n\n![](.assets/20220328191717.png)\n\n**Here is a list of all available marks:**\n\n| Mark | Description                                  |\n| :--- | :------------------------------------------- |\n| `:d` | divider line                                 |\n| `:i` | index                                        |\n| `:l` | long / loose format (multiple lines)         |\n| `:p` | parent layer                                 |\n| `:r` | rich format                                  |\n| `:s` | short / single line format                   |\n| `:t` | timestamp (not available in current version) |\n| `:v` | verbosity / log level                        |\n\n**Markup options:**\n\n```\n:d0     default divider line (default)\n:d1+    user defined (if not, fallback to :d0)\n\n:i0     reset index\n:i1     number width fixed to 1 (1, 2, 3, ... 9, 10, 11, ...) (default)\n:i2     number width fixed to 2 (01, 02, 03, ..., 99, 100, 101, ...)\n:i3     number width fixed to 3 (001, 002, 003, ..., 999, 1000, 1001, ...)\n:i4+    number width fixed to *\n:i9+    reserved, not defined yet (will be fallback to :i1)\n\n:l0     let lk-logger decides how to format long message (default)\n:l1     force expand all nodes\n\n:p0     self layer\n:p1     parent layer (default)\n:p2     grand parent layer\n:p3     great grand parent layer\n:p4     great great grand parent layer\n:p5+    great great great ... grand parent layer\n        note: be careful using :p2+, it may crash if the layer not exists\n\n:v0     trace\n        if you don\'t like using number, you can use an alias :vT\n        (:vT is not supported in current version. we\'ll bring it soon)\n:v1     debug (alias is :vD) (default)\n:v2     info (alias is :vI)\n:v3     warning (alias is :vW)\n:v4     error (alias is :vE)\n:v5     fatal (alias is :vF)\n:v6+    user defined (if not, fallback to :v0)\n```\n\n**Detailed examples:**\n\nSee [examples/02_all_markup_usages.py](examples/02_all_markup_usages.py).\n\nScreenshot:\n\n![](.assets/20220422184344.png)\n',
    'author': 'Likianta',
    'author_email': 'likianta@foxmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/likianta/lk-logger',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
