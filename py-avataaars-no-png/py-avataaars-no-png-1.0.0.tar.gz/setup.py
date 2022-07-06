# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_avataaars_no_png']

package_data = \
{'': ['*'],
 'py_avataaars_no_png': ['templates/*',
                         'templates/clothes/*',
                         'templates/clothes/graphics/*',
                         'templates/face/eyebrow/*',
                         'templates/face/eyes/*',
                         'templates/face/mouth/*',
                         'templates/face/nose/*',
                         'templates/top/*',
                         'templates/top/accessories/*',
                         'templates/top/facial_hair/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0']

setup_kwargs = {
    'name': 'py-avataaars-no-png',
    'version': '1.0.0',
    'description': 'SVG-Avatar generator library',
    'long_description': '# py-avataaars - Python component for Avataaars\n\n**FORK OF https://github.com/kebu/py-avataaars**\n\n\n## Changes\n- Switched from setup.py to Poetry\n- Removed svg2png-dependency -> **No PNG-support**\n\n## Original README\n\nPython port of https://github.com/fangpenlin/avataaars\n\n> The core React component for [Avataaars Generator](https://getavataaars.com/) developed by [Fang-Pen Lin](https://twitter.com/fangpenlin), based on the Sketch library [Avataaars](https://avataaars.com/) designed by [Pablo Stanley](https://twitter.com/pablostanley). \n\n### Features\n* SVG based\n* Light weight\n* Easy to use\n\n### Install\n```shell script\npip install py-avataaars\n```\n\n### Usage\n\nBasic usage:\n\n```python\nfrom py_avataaars import PyAvataaar\n\navatar = PyAvataaar()\navatar_svg = avatar.render_svg()\n```\n\nSpecify each part of avatar:\n```python\nimport py_avataaars as pa\navatar = pa.PyAvataaar(\n    style=pa.AvatarStyle.CIRCLE,\n    skin_color=pa.SkinColor.LIGHT,\n    hair_color=pa.HairColor.BROWN,\n    facial_hair_type=pa.FacialHairType.DEFAULT,\n    facial_hair_color=pa.HairColor.BLACK,\n    top_type=pa.TopType.SHORT_HAIR_SHORT_FLAT,\n    hat_color=pa.Color.BLACK,\n    mouth_type=pa.MouthType.SMILE,\n    eye_type=pa.EyesType.DEFAULT,\n    eyebrow_type=pa.EyebrowType.DEFAULT,\n    nose_type=pa.NoseType.DEFAULT,\n    accessories_type=pa.AccessoriesType.DEFAULT,\n    clothe_type=pa.ClotheType.GRAPHIC_SHIRT,\n    clothe_color=pa.Color.HEATHER,\n    clothe_graphic_type=pa.ClotheGraphicType.BAT,\n)\navatar_svg = avatar.render_svg()\n```\n',
    'author': 'Mawoka',
    'author_email': 'mawoka@mawoka.eu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mawoka-myblock/py-avataaars',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
