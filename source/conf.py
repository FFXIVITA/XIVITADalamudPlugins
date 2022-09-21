import os
import sys

sys.path.insert(0, os.path.abspath('..'))


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FFXIVITA Dalamud Plugins'
copyright = '2022, FFXIVITA'
author = 'FFXIVITA'
release = '2.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx_ahd_theme',
    'myst_parser'
]
templates_path = ['_templates']
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
master_doc = 'index'
language = "en"
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'requirements.txt']
todo_include_todos = False
today_fmt = '%d-%m-%Y %H:%M'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_ahd_theme'
html_static_path = ['_static']
html_theme_options = dict(
    project_name="XIVITA Dalamud Plugins",
    logo_alt="FFXIVITA",
    logo="img/ffxivita.svg",
    logo_width=45,
    logo_url="/",
    footer_links=",".join([
        "FFXIVITA|https://ffxivita.it/",
        "Lista Plugin|https://plugins.ffxivita.it",
        "Discord|https://discord.gg/ffxivita",
    ]),
    header_links="Sito Ufficiale|https://ffxivita.it, Directory Plugin|https://plugins.ffxivita.it",
    github_url="https://github.com/ffxivita/XIVITADalamudPlugins/blob/main/source/"
)
