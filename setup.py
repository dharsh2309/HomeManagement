from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in home_management/__init__.py
from home_management import __version__ as version

setup(
	name="home_management",
	version=version,
	description="home management system",
	author="Dharshini",
	author_email="dharsh2309@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
