# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ic_toolkit_edd']

package_data = \
{'': ['*']}

install_requires = \
['boto3', 'pandas', 'pymysql', 'typer[all]>=0.4.2,<0.5.0']

entry_points = \
{'console_scripts': ['ic = ic_toolkit_edd.main:app']}

setup_kwargs = {
    'name': 'ic-toolkit-edd',
    'version': '0.1.1',
    'description': '',
    'long_description': '# IC-ToolKit-EDD\n\n<img src="https://user-images.githubusercontent.com/71731452/177205395-ffe34180-5a7d-41f5-aba2-31ccc5b31031.gif" alt="exemplo imagem">\n\n> Esse projeto tem como objetivo facilitar a resolução de problemas da equipe de transformação.\n\n### Ajustes e melhorias\n\nÉ possivel implementar qualquer tipo de script nesse projeto\n\n## 💻 Pré-requisitos\n\nAntes de começar, verifique se você atendeu aos seguintes requisitos:\n<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->\n* Você instalou uma versão do Python superior a 3.7\n* Você tem uma máquina `<Windows / Linux>`.\n\n## 🚀 Instalando IC-ToolKit-EDD\n\nPara instalar o IC-ToolKit-EDD, siga estas etapas:\n\nLinux:\n```\npip3 install ic-toolkit-edd\n```\n\nWindows:\n```\npip install ic-toolkit-edd\n```\n\nWindows / Linux:\n\nUse o comando abaixo para informar as credencias do seu banco MySQL.\n```\nic config\n```\n> Obs: Isso vai gerar um arquivo .credentials em uma pasta .intuitivecare\n\n<img src="https://user-images.githubusercontent.com/71731452/177249673-6373a5e5-8d13-4c70-8d2b-fefab60002db.svg" width=500>\n\n## ☕ Comandos IC-ToolKit-EDD\n\nUse o comando abaixo para gerar um query com as hashs do diretorio atual\n\n```\nic gethash\n```\n> Obs: Um editor de texto ira abrir apos a execução do comando com a query gerada\n\n<img src="https://user-images.githubusercontent.com/71731452/177250804-c6833e17-9ec4-45a1-a166-6e07397f08d7.png" width=600>\n\n---\nUse o comando abaixo para baixar um ou mais arquivos da Amazon S3\n\n```\nic downorig <>\n```\n> Obs: Tambem é possivel baixar parseados e padronizados utilizando os comandos downpars ou downpadr\n\n<img src="https://user-images.githubusercontent.com/71731452/177250567-1464f5fa-292b-4b60-963c-f0892867780d.svg" width=600>\n\n## 🤝 Contribuindo\n\n### Adicionando novas funções\n\nPara adicionar novas funcionalidades basta seguir o exemplo do codigo abaixo\n  \n<img src="https://user-images.githubusercontent.com/71731452/177251543-1293882c-c50c-4492-b683-00d4005f6e10.svg" width=600>\n  \n> @app.command() possibilita a função ser chamada via CLI\n  \n',
    'author': 'Marcelo Assis',
    'author_email': '94455042+marceloapda@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
