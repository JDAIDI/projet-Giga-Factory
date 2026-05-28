import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Stratégie Gigafactories de Batteries'
copyright = '2026, JDAIDI OUSSAMA'
author = 'JDAIDI OUSSAMA'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'fr'

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Read the Docs integration -----------------------------------------------

html_context = {
    "display_github": True,
    "github_user": "JDAIDI",
    "github_repo": "projet-Giga-Factory",
    "github_version": "main",
    "conf_py_path": "/docs/",
}
