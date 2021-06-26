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

project_name = 'OpenAg'  # for replacement in the documentation
# rst_epilogs get appended to pages - currently, we're adding the ability to reference the project name as a variable in pages
rst_epilog = '.. |project_name| replace:: {}'.format(project_name)

project = "OpenAg Documentation"  # for sphinx
copyright = '2021, Regents of the University of California'
author = 'Nicholas Santos, Spencer Cole, Anna Rallings, Alex Guzman, José M. Rodríguez-Flores, Alvar Escriva-Bou, Joshua Viers, and Josué Medellín-Azuara for ' \
         'the Water Systems Management Lab and Vicelab at the University of California, Merced'
latex_author = 'Nicholas Santos, Spencer Cole, Anna Rallings, Alex Guzman, \\\\' \
               'José M. Rodríguez-Flores, Alvar Escriva-Bou, Joshua Viers, \\\\' \
               'and Josué Medellín-Azuara for the Water Systems Management \\\\' \
               'Lab and Vicelab at the University of California, Merced'

# The full version, including alpha/beta/rc tags
release = '1.0'

latex_documents = [("index", "openag_documentation.tex", project, latex_author, "manual", False),]


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