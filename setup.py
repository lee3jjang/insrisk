from setuptools import setup

DISTNAME = 'insrisk'
DESCRIPTION = 'Library for Insurance Risk Management'
AUTHOR = 'SangJin'
AUTHOR_EMAIL = 'lee3jjang@gmail.com'
URL = 'https://github.com/lee3jjang/insrisk'

setup(
    name=DISTNAME,
    version='v1.0.0',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    url=URL,
    packages=['insrisk'],
    python_requires=">=3.6",
    zip_safe=False,
)