# 1. 문서 만드는 법

* sphinx-quickstart


## 1.1. Sphinx Material

* 설치
```
> pip install git+https://github.com/bashtage/sphinx-material.git
```

* `conf.py` 수정
```python
extensions = ['sphinx.ext.autodoc', 'nbsphinx']
html_theme = 'sphinx_material'
html_sidebars = {
    "**": ["globaltoc.html", "localtoc.html", "searchbox.html", "logo-text.html"]
}
html_theme_options = {
    "nav_title": 'Material for Sphinx',
    "nav_links": [{
        "href": "https://www.naver.com",
        "title": "My Title",
        "internal": False,
    }],
    "heroes": {
        "index": "This is Index Page",
        "nbtest": "Notebook Test Page",
        "my_package": "Sample Module Page",
    },
    'base_url': 'https://www.directdb.co.kr',
    'color_primary': 'blue',
    'color_accent': 'light-blue',
    'repo_url': 'https://github.com/lee3jjang/dbesg/',
    'repo_name': 'dbesg',
    'repo_type': 'github',
    'logo_icon': '&#xe60e',
    "master_doc": False,
    'html_minify': True,
    'css_minify': True,
    'version_dropdown': True,
    'google_analytics_account': 'UA-XXXXX',
    'version_info': {
      "release": "",
      "development": "devel",
      "v1.0.0": "v1.0.0",
   },
}
```

# 2. 배포하는 법

[참고자료](https://onlytojay.medium.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC-pip-install-%ED%8C%A8%ED%82%A4%EC%A7%80-%EB%A7%8C%EB%93%A4%EC%96%B4%EB%B3%B4%EA%B8%B0-42ea68f4fabd)

```
> python setup.py bdist_wheel
```