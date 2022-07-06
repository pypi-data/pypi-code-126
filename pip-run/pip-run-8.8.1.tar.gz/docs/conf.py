#!/usr/bin/env python3
# -*- coding: utf-8 -*-

extensions = ['sphinx.ext.autodoc', 'jaraco.packaging.sphinx', 'rst.linker']

master_doc = "index"

link_files = {
    '../CHANGES.rst': dict(
        using=dict(GH='https://github.com'),
        replace=[
            dict(
                pattern=r'(Issue #|\B#)(?P<issue>\d+)',
                url='{package_url}/issues/{issue}',
            ),
            dict(
                pattern=r'(?m:^((?P<scm_version>v?\d+(\.\d+){1,2}))\n[-=]+\n)',
                with_scm='{text}\n{rev[timestamp]:%d %b %Y}\n',
            ),
            dict(
                pattern=r'PEP[- ](?P<pep_number>\d+)',
                url='https://peps.python.org/pep-{pep_number:0>4}/',
            ),
            dict(
                pattern=r"pip #(?P<pip_issue>\d+)",
                url='{GH}/pypa/pip/issues/{pip_issue}',
            ),
        ],
    )
}

# Be strict about any broken references:
nitpicky = True

nitpick_ignore = [
    ('py:class', 'contextlib.suppress'),
]

# Include Python intersphinx mapping to prevent failures
# jaraco/skeleton#51
extensions += ['sphinx.ext.intersphinx']
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# Custom sidebar templates, maps document names to template names.
html_theme = 'alabaster'
templates_path = ['_templates']
html_sidebars = {'index': ['tidelift-sidebar.html']}
