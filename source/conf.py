# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from datetime import datetime

project = 'Title'
copyright = f"{datetime.now().year} wkmna"
author = 'wkmna'
description = ''
github_repo_url = "https://github.com/wk-mnA/public_page"
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

master_doc = "index"
extensions = [
    "sphinxcontrib.sass",
    'sphinx.ext.mathjax', 
    'sphinx.ext.todo', 
    'sphinx.ext.githubpages',
    "sphinx_multiversion",
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'custom_theme'
html_theme_path = ['.']
html_static_path = ['_static']
html_static_path = ['custom_theme']
# html_style = 'assets/css/style.css'
html_css_files = ["css/style.css"]

sass_src_dir = "_static/assets/css"
sass_out_dir = "_static/css"
sass_targets = {
 "style.scss": "style.css"
}
# html_css_files = ['_static/assets/css/style.scss']
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
    ]
}

html_theme_options = {
    "description": "This is a test website<br>Test",
    "github_user": "wk-mna",
    "github_repo": "public_page",
    "fixed_sidebar": True,
    # "show_prev_next" : True,
    # "navigation_with_keys" : True,
    # "tidelift_url": "https://tidelift.com/subscription/pkg/pypi-alabaster?utm_source=pypi-alabaster&utm_medium=referral&utm_campaign=docs",  # noqa
}
# extensions.append("releases")
# releases_github_path = "sphinx-doc/alabaster"
# # Our pre-0.x releases are unstable / mix bugs+features
# releases_unstable_prehistory = True