import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'Project'
author = 'Author'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',   # Markdown support
]

# Support both .rst and .md
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'

templates_path = ['templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output -------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'   

html_static_path = ['_static']

html_css_files = [
    'style.css',
]

html_title = "My Custom Page"

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_title = "$2400 Extra Benefits for Seniors (2026 Guide)"

# You can still add html_meta here if you want, but with the new Read the Docs addons
# custom template is the reliable way to inject meta tags.

# If you want to add other meta tags, do so in your _templates/layout.html
