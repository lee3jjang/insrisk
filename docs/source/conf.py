# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'insrisk'
copyright = '2021, SangJin'
author = 'SangJin'

# The full version, including alpha/beta/rc tags
release = 'v1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'nbsphinx',
    'sphinx.ext.autosummary',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ko'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_sidebars = {
    "**": ["globaltoc.html", "localtoc.html", "searchbox.html", "logo-text.html"]
}

html_theme_options = {
    "nav_title": 'insrisk ' + release,
    "nav_links": [
        {"href": "https://vm.dbins.co.kr", "title": "업무가상PC", "internal": False},
        {"href": "https://www.mdbins.com:8100", "title": "외부포탈", "internal": False},
        {"href": "https://mail.dbins.co.kr", "title": "외부메일", "internal": False},
    ],
    "heroes": {
        "index": "보험RM파트 업무용 라이브러리",
    },
    # 'base_url': 'https://www.directdb.co.kr',
    'color_primary': 'blue',
    'color_accent': 'light-blue',
    'repo_url': 'https://github.com/lee3jjang/insrisk',
    'repo_name': 'insrisk',
    'repo_type': 'github',
    'logo_icon': '&#xe80e',
    "master_doc": False,
    'html_minify': True,
    'css_minify': True,
    'version_dropdown': True,
    'google_analytics_account': 'UA-XXXXX',
    'version_info': {
      "release": "",
      "development": "devel",
   },
}