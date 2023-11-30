# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'A COVID-is-airborne community view of the UK Covid-19 Inquiry'
copyright = 'Crown copyright, OGL v3.0 where that pertains to source transcripts'
author = 'UK Covid-19 Inquiry (HTMLized by Matthew Somerville) and various commentors'

# -- General configuration

extensions = [
    "recommonmark",
    "sphinxcontrib.jquery",
    'sphinx_reredirects'
]

redirects = {
     "./Hancock2": "../2023-11-30_module-2/1_Mr_Matt_Hancock",
     "./MH2": "../2023-11-30_module-2/1_Mr_Matt_Hancock"
}

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_show_sphinx = False

html_theme_options = {
    'analytics_anonymize_ip': True,
    'logo_only': False,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': '#030f98',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
#
exclude_patterns = ['module*', 'README_AS_WELL.md']
html_static_path = ['_static']
html_css_files = ['custom.css']

rst_epilog = """
.. include:: <s5defs.txt>
"""

# -- Options for EPUB output
epub_show_urls = 'footnote'
