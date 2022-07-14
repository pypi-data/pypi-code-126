from setuptools import setup, find_packages

setup(
        name='DrawTick',
        version='0.0.1',
        keywords = ["pip", "DrawTick"],
        description= "DrawTick",
        license = "MIT Licence",
        url='',
        author='liujun',
        author_email='62462156@qq.com',
        packages=find_packages(),
        include_package_data=True,
        plaforms = 'any',
        install_requires=["re","datetime","pandas", "matplotlib", "mpl_finance", "numpy", "json"]
)
