#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# BrainPywer documentation build configuration file, created by
# sphinx-quickstart on Wed Oct 12 02:24:42 2016

import sys
import os
import shlex

sys.path.insert(0, os.path.abspath('..'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.linkcode',
    'sphinx.ext.coverage',
    'sphinx.ext.todo'
]

autodoc_default_flags = ['members', 'undoc-members']

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = 'BrainPywer'
copyright = '2016, BrainPywer Team'
author = 'BrainPywer Team'
version = '0.1.0'
release = '0.1.0'

language = None
exclude_patterns = ['_build']
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------
html_logo = 'logo.png'
html_favicon = 'favicon.png'
html_static_path = ['_static']
html_domain_indices = True
html_use_index = True
html_split_index = False
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True
html_use_opensearch = 'brainpywer.readthedocs.io'
html_search_language = 'en'
htmlhelp_basename = 'BrainPywerdoc'

# -- Options for manual page output ---------------------------------------
man_pages = [
    (master_doc, 'brainpywer', 'BrainPywer Documentation',
     [author], 1)
]
# -- Linkcode --
def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None
    filename = info['module'].replace('.', '/')
    return "https://github.com/BrainPywer/BrainPywer/blob/master/%s.py" % filename