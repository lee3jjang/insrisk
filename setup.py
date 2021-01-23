from setuptools import setup, find_packages

PROJECT_URLS = {
    'Source Code': 'https://github.com/lee3jjang/insrisk'
}

DISTNAME = 'insrisk'
DESCRIPTION = 'Library for Insurance Risk Management'
MAINTAINER = 'SangJin'
MAINTAINER_EMAIL = 'lee3jjang@gmail.com'

setup(
    name=DISTNAME,
    version='v1.0.0',
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    project_ruls=PROJECT_URLS,
    packages=find_packages(),
    python_requires=">=3.6",
    zip_safe=False,
)