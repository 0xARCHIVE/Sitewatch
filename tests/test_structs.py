#!/usr/bin/env python3

"""
Tests for structs:
SiteInfo
SlackInfo
"""

import unittest

from sitewatch.structs import SiteInfo, SlackInfo

class TestSiteInfoStruct(unittest.TestCase):
    """Test SiteInfo struct"""
    def test_create(self) -> None:
        """Create - correct usage"""
        test_siteinfo = SiteInfo(id=1, url='test', tag_id='test', hash='test', timestamp=1)
        self.assertTrue(isinstance(test_siteinfo, SiteInfo))

    def test_create_missing_args(self) -> None:
        """Create - missing required args"""
        with self.assertRaises(TypeError):
            SiteInfo()

    def test_create_optional(self) -> None:
        """Create - missing optional args"""
        test_siteinfo = SiteInfo(url='test.com')
        self.assertTrue(isinstance(test_siteinfo, SiteInfo))

class TestSlackInfoStruct(unittest.TestCase):
    """Test SlackInfo struct"""
    def test_create(self) -> None:
        """Create - correct usage"""
        test_slackinfo = SlackInfo(id=1, webhook_url='test')
        self.assertTrue(isinstance(test_slackinfo, SlackInfo))

    def test_create_missing_args(self) -> None:
        """Create - missing required args"""
        with self.assertRaises(TypeError):
            SlackInfo()
