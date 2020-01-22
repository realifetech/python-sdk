import os
import re

from pkg_resources import parse_requirements
from setuptools import find_packages, setup

del os.link

PACKAGE_NAME = 'livestyled'


def parse_version(package_name):
    """
    if environment variable PACKAGE_VERSION set use that as version number
    else open `VERSION_FILE` and find `__version__ = x.y.z`.
    thanks to http://stackoverflow.com/a/7071358
    """
    version = os.environ.get('PACKAGE_VERSION', None)
    if version:
        return version

    VERSION_RE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    VERSION_FILE = '{}/__init__.py'.format(package_name)
    with open(VERSION_FILE, 'r') as f:
        file_contents = f.read()
    match = re.search(VERSION_RE, file_contents, re.M)
    if match:
        return match.group(1)
    else:
        raise RuntimeError('Unable to find version string in {}.'.format(VERSION_FILE))


requirements_fn = os.path.join(os.path.dirname(__file__), 'requirements.txt')

setup(
    name=PACKAGE_NAME,
    version=parse_version(PACKAGE_NAME),
    packages=find_packages(),
    include_package_data=True,
    author='LiveStyled',
    author_email='dev@livestyled.com',
    url='https://github.com/livestyled/python-sdk',
    install_requires=[str(req) for req in parse_requirements(open(requirements_fn).read())],
    entry_points="""
    [console_scripts]
    """
)
