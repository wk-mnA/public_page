# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'docs'
copyright = '2023, wkmna'
author = 'wkmna'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

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

html_theme = 'alabaster'
html_static_path = ['_static']
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

# html_theme_options = {
#      "icon_links": [
#          {
#              "name": "GitHub",
#              "url": "https://gitlab.com/jacst/goodpractice/",  # required
#              "icon": "fab fa-gitlab",
#              "type": "fontawesome",  # Default is fontawesome
#          },
#          {
#              "name": "Get the Board",
#              "url": "https://twitter.com/jacst_jp",
#              "icon": "fab fa-twitter",
#          },
#      ],
# }