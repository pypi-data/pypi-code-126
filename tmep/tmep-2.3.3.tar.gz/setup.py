# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tmep']

package_data = \
{'': ['*']}

install_requires = \
['Unidecode>=1.3.4,<2.0.0']

entry_points = \
{'console_scripts': ['tmep-doc = tmep.doc:print_doc']}

setup_kwargs = {
    'name': 'tmep',
    'version': '2.3.3',
    'description': 'Template and Macros Expansion for Path names.',
    'long_description': ".. image:: http://img.shields.io/pypi/v/tmep.svg\n    :target: https://pypi.python.org/pypi/tmep\n    :alt: This package on the Python Package Index\n\n.. image:: https://github.com/Josef-Friedrich/tmep/actions/workflows/test.yml/badge.svg\n    :target: https://github.com/Josef-Friedrich/tmep/actions/workflows/test.yml\n    :alt: Tests\n\n.. image:: https://readthedocs.org/projects/tmep/badge/?version=latest\n    :target: https://tmep.readthedocs.io/en/latest/?badge=latest\n    :alt: Documentation Status\n\n====\ntmep\n====\n\nTemplate and Macros Expansion for Path names.\n\nInstallation\n============\n\nFrom PyPI\n----------\n\n.. code:: Shell\n\n    pip install tmep\n\nUsage\n=====\n\n.. code:: Python\n\n    >>> import tmep\n    >>> template = '$prename $lastname'\n    >>> values = {'prename': 'Franz', 'lastname': 'Schubert'}\n    >>> out = tmep.parse(template, values)\n    >>> print(out)\n    Franz Schubert\n\nThis module implements a string formatter based on the standard PEP\n292 string.Template class extended with function calls. Variables, as\nwith string.Template, are indicated with $ and functions are delimited\nwith %.\n\nThis module assumes that everything is Unicode: the template and the\nsubstitution values. Bytestrings are not supported. Also, the templates\nalways behave like the ``safe_substitute`` method in the standard\nlibrary: unknown symbols are left intact.\n\nThis is sort of like a tiny, horrible degeneration of a real templating\nengine like Jinja2 or Mustache.\n\nDevelopment\n===========\n\nTest\n----\n\n::\n\n    tox\n\n\nPublish a new version\n---------------------\n\n::\n\n    git tag 1.1.1\n    git push --tags\n    poetry build\n    poetry publish\n\n\nPackage documentation\n---------------------\n\nThe package documentation is hosted on\n`readthedocs <http://tmep.readthedocs.io>`_.\n\nGenerate the package documentation:\n\n::\n\n    python setup.py build_sphinx\n\n\nFunctions\n=========\n\n.. code ::\n\n    alpha\n    -----\n\n    %alpha{text}\n        This function first ASCIIfies the given text, then all non alphabet\n        characters are replaced with whitespaces.\n\n    alphanum\n    --------\n\n    %alphanum{text}\n        This function first ASCIIfies the given text, then all non alpanumeric\n        characters are replaced with whitespaces.\n\n    asciify\n    -------\n\n    %asciify{text}\n        Translate non-ASCII characters to their ASCII equivalents. For\n        example, “café” becomes “cafe”. Uses the mapping provided by the\n        unidecode module.\n\n    delchars\n    --------\n\n    %delchars{text,chars}\n        Delete every single character of “chars“ in “text”.\n\n    deldupchars\n    -----------\n\n    %deldupchars{text,chars}\n        Search for duplicate characters and replace with only one occurrance\n        of this characters.\n\n    first\n    -----\n\n    %first{text} or %first{text,count,skip} or\n    %first{text,count,skip,sep,join}\n        Returns the first item, separated by ; . You can use\n        %first{text,count,skip}, where count is the number of items (default\n        1) and skip is number to skip (default 0). You can also use\n        %first{text,count,skip,sep,join} where sep is the separator, like ; or\n        / and join is the text to concatenate the items.\n\n    if\n    --\n\n    %if{condition,truetext} or %if{condition,truetext,falsetext}\n        If condition is nonempty (or nonzero, if it’s a number), then returns\n        the second argument. Otherwise, returns the third argument if\n        specified (or nothing if falsetext is left off).\n\n    ifdef\n    -----\n\n    %ifdef{field}, %ifdef{field,text} or %ifdef{field,text,falsetext}\n        If field exists, then return truetext or field (default). Otherwise,\n        returns falsetext. The field should be entered without $.\n\n    ifdefempty\n    ----------\n\n    %ifdefempty{field,text} or %ifdefempty{field,text,falsetext}\n        If field exists and is empty, then return truetext. Otherwise, returns\n        falsetext. The field should be entered without $.\n\n    ifdefnotempty\n    -------------\n\n    %ifdefnotempty{field,text} or %ifdefnotempty{field,text,falsetext}\n        If field is not empty, then return truetext. Otherwise, returns\n        falsetext. The field should be entered without $.\n\n    initial\n    -------\n\n    %initial{text}\n        Get the first character of a text in lowercase. The text is converted\n        to ASCII. All non word characters are erased.\n\n    left\n    ----\n\n    %left{text,n}\n        Return the first “n” characters of “text”.\n\n    lower\n    -----\n\n    %lower{text}\n        Convert “text” to lowercase.\n\n    nowhitespace\n    ------------\n\n    %nowhitespace{text,replace}\n        Replace all whitespace characters with replace. By default: a dash (-)\n        %nowhitespace{$track,_}\n\n    num\n    ---\n\n    %num{number,count}\n        Pad decimal number with leading zeros.\n        %num{$track,3}\n\n    replchars\n    ---------\n\n    %replchars{text,chars,replace}\n        Replace the characters “chars” in “text” with “replace”.\n        %replchars{text,ex,-} > t--t\n\n    right\n    -----\n\n    %right{text,n}\n        Return the last “n” characters of “text”.\n\n    sanitize\n    --------\n\n    %sanitize{text}\n        Delete in most file systems not allowed characters.\n\n    shorten\n    -------\n\n    %shorten{text} or %shorten{text,max_size}\n        Shorten “text” on word boundarys.\n        %shorten{$title,32}\n\n    time\n    ----\n\n    %time{date_time,format,curformat}\n        Return the date and time in any format accepted by strftime. For\n        example, to get the year some music was added to your library, use\n        %time{$added,%Y}.\n\n    title\n    -----\n\n    %title{text}\n        Convert “text” to Title Case.\n\n    upper\n    -----\n\n    %upper{text}\n        Convert “text” to UPPERCASE.\n\n\n",
    'author': 'Josef Friedrich',
    'author_email': 'josef@friedrich.rocks',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Josef-Friedrich/tmep',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
