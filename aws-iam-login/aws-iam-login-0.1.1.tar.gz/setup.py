# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aws_iam_login']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.24.11,<2.0.0', 'click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['aws-iam-login = aws_iam_login:main']}

setup_kwargs = {
    'name': 'aws-iam-login',
    'version': '0.1.1',
    'description': 'Configures STS credentials using a MFA authenticated session.',
    'long_description': '# AWS IAM Login\n\n`aws-iam-login` allows you to login using MFA as the IAM user itself. Once logged in your temporary credentials are\nstored in the `~/.aws/credentials` file for re-use.\n\n## Configuration\n\nYou will need to configure your roles and IAM User credentials in the same places as you are used to. So in your\n`~/.aws/credentials` file you will need to have the following:\n\n```ini\n[my-profile]\naws_access_key_id = XXXXXXX\naws_secret_access_key = XXXXXXXXXXXXXXXXXXXXXXXXXXXX\nmfa_serial = arn:aws:iam::111122223333:mfa/my-iam-user\n```\n\nThe only addition is the `mfa_serial` field.\n\n## Usage\n\nWhen you want to make use of the MFA authenticated session of a configured profile. You will need to configure the\nfollowing:\n\n```ini\n[profile my-role-1]\nrole_arn = arn:aws:iam::111122223333:role/my-role-1\nsource_profile = my-profile-sts\nregion = eu-west-1\n```\n\nThen when you perform your AWS cli calls you can use the `AWS_PROFILE=my-role-1` as you are used to. But the first time  it will fail. The reason for this is that the `my-profile-sts` source profile does not exist (or the credentials are expired).\nPerform the following command to login, this command will ask for your MFA Token:\n\n```bash\naws-iam-login my-profile\n```\n\nThis authenticates against the AWS API and request temporary credentials from AWS using your MFA Token. These credentials are then stored as `<profile-name>-sts`.\nSo the next time you use `AWS_PROFILE=my-role-1` the credentials will be present and not expired.\n\nBecause you are already authenticated using MFA there is no need to provide an MFA token when you assume the role.\nWhen you switch a lot between roles you really benefit from not having to type your MFA token each time you switch.\n',
    'author': 'Joris Conijn',
    'author_email': 'jorisconijn@binx.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
