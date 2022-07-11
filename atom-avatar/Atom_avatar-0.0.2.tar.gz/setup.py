import glob
import setuptools

setuptools.setup(
    name="Atom_avatar",
    version="0.0.2",
    author="Quadri Tosin Micheal",
    description="python avater maker with avatermaker.com svg",
    packages=["avatar"],
data_files=glob.glob('avatar/**'),
include_package_data=True
)
