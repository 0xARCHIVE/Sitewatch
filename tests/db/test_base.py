#!/usr/bin/env python3

"""
Base DB handler tests
"""

import unittest
from unittest.mock import Mock

from sitewatch.db import BaseDbHandler
from sitewatch.structs import SiteInfo

class TestBaseDbHandler(unittest.TestCase):
    """Base DB handler tests"""
    def test_abstract_get_sites(self) -> None:
        """Sanity check - should be NotImplemented"""
        handler = BaseDbHandler()
        with self.assertRaises(NotImplementedError):
            handler.get_sites()

    def test_abstract_store_sites(self) -> None:
        """Sanity check - should be NotImplemented"""
        handler = BaseDbHandler()
        with self.assertRaises(NotImplementedError):
            handler.store_sites([Mock(spec=SiteInfo)])

    def test_abstract_get_slackinfo(self) -> None:
        """Sanity check - should be NotImplemented"""
        handler = BaseDbHandler()
        with self.assertRaises(NotImplementedError):
            handler.get_slackinfo(Mock(spec=SiteInfo))
