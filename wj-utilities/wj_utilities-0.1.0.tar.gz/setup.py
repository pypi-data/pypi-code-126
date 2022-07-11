# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wj_common',
 'wj_common.common',
 'wj_common.utils',
 'wj_exception',
 'wj_exception.exception',
 'wj_exception.exception.utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'wj-utilities',
    'version': '0.1.0',
    'description': 'library for handle custom exception and commons functionalities for W&J micro services',
    'long_description': '# wj_common library\n\nExeption library for backend in Whale and Jaguar\n\n## Description \n\nEsta libreria tiene como objetivo brindar al desarrollador un método para responder desde el backend cuando ocurra un error, de acuerdo al [estándar](https://whaleandjaguar.atlassian.net/wiki/spaces/~62165c0271554c0069553da0/pages/1822883841/Estandarizaci+n+de+Respuestas+en+el+Backend) propuesto en W&J.\n\nPor otro lado se han dispuesto funcionalidades que son utiles en los diferentes micro servicios desarrollados en W&J. Esto con el fin de centralizar las funciones comunes y evitar la duplicación de código.\n\n## Getting started\n### Requirements \n\n- Docker\n- GNU make \n- Git\n\nActualmente se ha construido la librería en el repositorio para paquetes de prueba python [TestPyPI](https://test.pypi.org/) por lo que se puede instalar este paquet vía pip.\n\n### Install\n\n```\npip3 install -i https://test.pypi.org/simple/ wj-common\n```\n## Usage \n\nLa librería cuenta con dos paquetes: \n\n- [wj_common](docs/commons_functions/commons_functions.md): \nAquí se encuentran las funcionalidades útiles que se pueden emplear para el desarrollo de nuevas funcionalides en los servicios ofrecidos.\n\n- [wj_exception](docs/exceptions/exceptions.md): \nAquí se encuentran las excepciones personalizadas para el manejo de los errores de acuerdo al [estándar](https://whaleandjaguar.atlassian.net/wiki/spaces/~62165c0271554c0069553da0/pages/1822883841/Estandarizaci+n+de+Respuestas+en+el+Backend).\n\nPara obtener las respuestas de acuaerdo a lo planteado se deben usar ambos paquetes como se muestra en el siguiente ejemplo.\n\n```\nfrom wj_exception.exception.no_data import ItemNotFound\nfrom wj_common.utils import utils\n\ntry:\n    raise ItemNotFound()\nexcept Exception as e:\n    exception_resp = utils.get_response_error(exception=e)\n    status = e.status\n\nprint(f"response error = {exception_resp}\\nstatus = {status}")\n``` \n\nRespuesta obtenida:\n\n```\nresponse error = {\'error\': {\'code\': \'itemNotFound\', \'message\': \'data not found\',\'location\': \'<stdin> in line 2\'}}\nstatus = 404\n```\n## License\nGNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007\n\n',
    'author': 'Jose Arroyave',
    'author_email': 'josearroyave@whaleandjaguar.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
