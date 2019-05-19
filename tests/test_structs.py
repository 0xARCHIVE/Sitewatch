#!/usr/bin/env python3

"""
Tests for structs:
SiteInfo
"""

import unittest

from sitewatch.structs import SiteInfo

class TestSiteInfoStruct(unittest.TestCase):
    """Test SiteInfo struct"""
    def test_create(self) -> None:
        """Create - correct usage"""
        test_siteinfo = SiteInfo(1, 'test', 'test', 'test', 1)
        self.assertTrue(isinstance(test_siteinfo, SiteInfo))

    def test_create_missing_args(self) -> None:
        """Create - missing required args"""
        with self.assertRaises(TypeError):
            SiteInfo()
