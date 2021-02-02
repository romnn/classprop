# -*- coding: utf-8 -*-

"""Top-level package for classprop."""

__author__ = """romnn"""
__email__ = "contact@romnn.com"
__version__ = "0.1.1"

from classprop.classprop import ClassPropertyMetaClass as _mc
from classprop.classprop import class_property

# Aliases
class_prop = class_property
classprop = class_property
classproperty = class_property
ClassPropertyMetaClass = _mc
