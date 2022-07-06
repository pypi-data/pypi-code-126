from setuptools import setup, find_packages
import os

os.environ['name'] = 'my_pypi_custom_package_dev'


setup(
    name=os.environ['name'],
    version='0.0.30',
    description='A custom package demo',
    # url='https://github.com/shuds13/pyexample',
    # author='Nik Hudson',
    author_email='example@example.com',
    license='Some licence',
#     packages=['my_max_package.my_utils', 'my_max_package.utils.gcs_utils'],
#     packages=['my_max_package'],
    packages=find_packages(),
#     package_dir={'my_max_package':'lib'},
    install_requires=[],

    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
)


#
# import dynamic_versioning
#
#
# # configure dynamic versioning
# dynamic_versioning.configure()
#
#
#
# setup(
# 	name='my_pypi_custom_package',
# 	description='A neat new tool you won\'t want to miss',
#     version = None,
#     packages=find_packages(),
# 	cmdclass={
# 		"sdist": dynamic_versioning.DynamicVersionSDist,
# 		"bdist": dynamic_versioning.DynamicVersionBDist,
# 		"install": dynamic_versioning.DynamicVersionInstall,
# 	}
# )