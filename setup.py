#!/usr/bin/env python
import os
from distutils.core import setup

from nagi import VERSION

# I really prefer Markdown to reStructuredText.  PyPi does not.  This allows me
# to have things how I'd like, but not throw complaints when people are trying
# to install the package and they don't have pypandoc or the README in the
# right place.
try:
   import pypandoc
   description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   description = ''

setup(
   name = 'nagi',
   version = VERSION,
   author = 'James Pearson',
   author_email = 'xiong.chiamiov@gmail.com',
   packages = ['nagi'],
   scripts = ['bin/nagi'],
   url = 'https://github.com/xiongchiamiov/nagi',
   license = 'GPLv2',
   description = 'Rename files according to the filenames given in a .torrent.',
   long_description = description,
   install_requires = [],
)

