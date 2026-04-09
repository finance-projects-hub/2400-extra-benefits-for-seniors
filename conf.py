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

# 👇 IMPORTANT (Markdown properly render karega)
myst_enable_extensions = [
    "colon_fence",
]

# Support both .rst and .md
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# 👇 Main file (index.md load karega)
master_doc = 'index'

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output -------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_css_files = [
    'style.css',
]

# 👇 SEO Title
html_title = "$2400 Extra Benefits for Seniors (2026 Guide)"

# Optional sidebar fix
html_sidebars = {
    '**': ['globaltoc.html']
}
