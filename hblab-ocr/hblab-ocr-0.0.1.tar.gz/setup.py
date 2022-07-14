from setuptools import setup, find_packages

# with open('requirements.txt', encoding="utf-8") as f:
#     requirements = f.readlines()

setup(
    name='hblab-ocr',
    version='0.0.1',
    license='MIT',
    author="Le Trong Hieu",
    author_email='hieult@hblab.vn',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/hblab-hieult/hblab-ocr',
    keywords='Package for Japaneses OCR',
    include_package_data=True,
    install_requires=['torch',
                      'torchvision',
                      'opencv-python',
                      'shapely',
                      'pyclipper',],
)
