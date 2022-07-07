from setuptools import setup
from setuptools import find_packages
# requires = ["threading","statistics","pyvisa","tkinter","ctypes.wintypes"]
setup(
    name='yc_tools',
    version='0.0.6',
    description='=用于YICHIP内部仪器设备的控制',
    author='Susunl',
    author_email='1253013130@qq.com',
    long_description_content_type ='text/markdown',
    license='MIT',
    packages = find_packages(),
    include_package_data = True,
    python_requires=">=3.5",
    zip_safe=False,
    platforms = 'any',
    classifiers=[ 'Programming Language :: Python :: 3'],
)
