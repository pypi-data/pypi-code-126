# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['manim_gearbox', 'manim_gearbox.gear_mobject']

package_data = \
{'': ['*']}

install_requires = \
['manim>=0.13.1', 'scipy']

entry_points = \
{'manim.plugins': ['manim_gearbox = manim_gearbox']}

setup_kwargs = {
    'name': 'manim-gearbox',
    'version': '0.2.2',
    'description': 'This is an extension of Manim that helps drawing nice looking gears.',
    'long_description': '# manim-Gearbox\nThis is a plugin for Manim that enables you to draw realistic looking gears and mechanisms.\nSo far only involute gears are supported, with inside and outside gears.\n\nPlanned further development:\n- Rack and pinion\n- Cycloid gears, cycloid rack\n- Sliced gears\n- Animation helpers\n\n# Installation\n`manim-gearbox` is a package on pypi, and can be directly installed using pip:\n```\npip install manim-gearbox\n```\n# Usage\nMake sure include these two imports at the top of the .py file\n```py\nfrom manim import *\nfrom manim_gearbox import *\n```\n\n# Examples\n\n**2 basic gears**\n```py\nclass gear_example(Scene):\n\tdef construct(self):\n\t\t# small gear\n\t\tgear1=Gear(15, stroke_opacity=0, fill_color=WHITE,fill_opacity=1)\n\t\t# larger gear\n\t\tgear2=Gear(25,  stroke_opacity=0, fill_color=RED, fill_opacity=1)\n\t\t# shifting gear1 away from center\n\t\tgear1.shift(-gear1.rp * 1.5 * RIGHT)\n\t\t# position gear2 next to gear1 so that they mesh together\n\t\tgear2.mesh_to(gear1)\n\n\t\tself.add(gear1, gear2)\n\t\tself.play(Rotate(gear1, gear1.pitch_angle, rate_func=linear),\n\t\t\t\t  Rotate(gear2, - gear2.pitch_angle, rate_func=linear),\n\t\t\t\t  run_time=4)\n\t\t\n```\n![involute_gear_example](/media/involute_gear_example.gif)\n\n**inner gear**\n```py\nclass gear_example_inner(Scene):\n    def construct(self):\n        # smaller gear\n        gear1 = Gear(15, module=1, stroke_opacity=0, fill_color=WHITE,fill_opacity=1)\n        # larger gear with inner teeth\n        gear2 = Gear(36, module=1, inner_teeth=True, stroke_opacity=0, fill_color=RED, fill_opacity=1)\n        gear1.shift(gear1.rp * UP)\n        gear2.mesh_to(gear1)\n\n        self.add(gear1)\n        self.add(gear2)\n        self.play(Rotate(gear1, gear1.pitch_angle, rate_func=linear),\n                  Rotate(gear2, gear2.pitch_angle, rate_func=linear),\n                  run_time=10)\n\t\t\n```\n![inner_gear_example](/media/inner_gear_example.gif)\n',
    'author': 'GarryBGoode',
    'author_email': 'bgeri91@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/GarryBGoode/manim-GearBox',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
