from setuptools import setup
from os.path import abspath, join as pjoin, relpath, split

DISTNAME = 'insrisk'
DESCRIPTION = 'Library for Insurance Risk Management'
AUTHOR = 'SangJin'
AUTHOR_EMAIL = 'lee3jjang@gmail.com'
URL = 'https://github.com/lee3jjang/insrisk'
SETUP_DIR = split(abspath(__file__))[0]
with open(pjoin(SETUP_DIR, 'README.rst'), encoding='utf8') as readme:
    README = readme.read()
LONG_DESCRIPTION = README

setup(
    name=DISTNAME,
    version='v1.0.0',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    packages=['insrisk'],
    python_requires=">=3.6",
    zip_safe=False,
)