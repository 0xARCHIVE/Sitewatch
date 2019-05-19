#!/usr/bin/env python3

"""
Base DB handler tests
"""

import unittest

from sitewatch.db import BaseDbHandler

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
            handler.store_sites([])
