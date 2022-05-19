# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'qETRC'
copyright = '2022, xep'
author = 'xep'

release = '1.1.6'
version = '1.1.6'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# myst_enable_extensions = [
#     "amsmath",
#     "dollarmath",
# ]

latex_engine = 'xelatex'
latex_use_xindy = False
latex_elements = {
    'preamble': '\\usepackage[UTF8]{ctex}\n',
}

intersphinx_mapping = {
    # 'pyETRC-rtd':('https://pyetrc-rtd.readthedocs.io/zh_CN/master/', None)
}
