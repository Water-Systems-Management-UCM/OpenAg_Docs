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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# we import this to modify image handling - see further down
from sphinx.builders.html import StandaloneHTMLBuilder

# -- Project information -----------------------------------------------------

project = 'OpenAg'
copyright = '2021, UC Merced Water Systems Management Lab, Vicelab, and the Center for Information Technology Research in the Interest of Society'
author = 'UC Merced Water Systems Management Lab, Vicelab, and the Center for Information Technology Research in the Interest of Society'

# The full version, including alpha/beta/rc tags
release = '0.2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'sphinx.ext.autosectionlabel',
	'sphinx.ext.mathjax',
	'sphinx.ext.todo'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# include numbering for figures
numfig = True

# -- Options for HTML output -------------------------------------------------

# set it so the HTML builder prefers gifs over PNGs so that we can include a GIF
# when we have one, but the LaTeX/PDF builder will still include the correct
# non-animated version. See https://stackoverflow.com/a/45970146/587938
new_supported_image_types = [
    'image/svg+xml',
    'image/gif',
    'image/png',
    'image/jpeg'
]

# construct it this way so that if Sphinx adds default support for additional images, such
# as HEIC, then what we do is add any of those to the end. We start with the ones
# we want to support in this order, then subtract them from the defaults and add
# any remaining items
additional_default_supported_images = list(set(StandaloneHTMLBuilder.supported_image_types) - set(new_supported_image_types))
StandaloneHTMLBuilder.supported_image_types = new_supported_image_types + additional_default_supported_images

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']