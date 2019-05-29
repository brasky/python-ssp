import os

from setuptools import find_packages, setup

def text_of(relpath):
    """
    Return string containing the contents of the file at *relpath* relative to
    this file.
    """
    thisdir = os.path.dirname(__file__)
    file_path = os.path.join(thisdir, os.path.normpath(relpath))
    with open(file_path) as f:
        text = f.read()
    return text

NAME = 'python-ssp'
VERSION = '0.0.1'
DESCRIPTION = 'Extract data from FedRAMP SSP templates'
KEYWORDS = 'fedramp ssp word'
AUTHOR = 'Elliot DeMatteis'
URL = 'https://github.com/brasky/python-ssp'
LICENSE = text_of('LICENSE')
PACKAGES = find_packages(exclude=['tests', 'tests.*'])
LONG_DESCRIPTION = text_of('README.md') + '\n\n' + text_of('HISTORY.rst')
LONG_DESCRIPTION_CONTENT_TYPE="text/markdown"
PACKAGES = find_packages(exclude=['tests', 'tests.*'])
CLASSIFIERS = [
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
]

INSTALL_REQUIRES = ['python-docx']
TEST_SUITE = ''
TESTS_REQUIRE = []

params = {
    'name':             NAME,
    'version':          VERSION,
    'description':      DESCRIPTION,
    'keywords':         KEYWORDS,
    'long_description': LONG_DESCRIPTION,
    'author':           AUTHOR,
    'url':              URL,
    'license':          LICENSE,
    'packages':         PACKAGES,
    'install_requires': INSTALL_REQUIRES,
    'tests_require':    TESTS_REQUIRE,
    'test_suite':       TEST_SUITE,
    'classifiers':      CLASSIFIERS,
}

setup(**params)