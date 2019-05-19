#!/usr/bin/env python3

"""Pkgutil style init"""

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

from sitewatch.db.base import BaseDbHandler
from sitewatch.db.mysql import MysqlHandler
