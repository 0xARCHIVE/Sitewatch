#!/usr/bin/env python3

"""
MySQL DB handler tests
"""

import unittest

from sitewatch.db.mysql import Slack, create_slackinfo_from_slack
from sitewatch.db.mysql import Site, create_site_from_siteinfo, create_siteinfo_from_site
from sitewatch.structs import SiteInfo, SlackInfo

class TestCreateSqlAlchemyTypes(unittest.TestCase):
    """Test create_*_from_* functions"""
    def test_create_site_from_siteinfo(self) -> None:
        """Create sqlalchemy site from SiteInfo"""
        test_siteinfo = SiteInfo(id=1, url='test.com', tag_id='test', hash='123', timestamp=1)
        site = create_site_from_siteinfo(test_siteinfo)
        self.assertTrue(isinstance(site, Site))

        test_siteinfo = SiteInfo(url='test.com')
        site = create_site_from_siteinfo(test_siteinfo)
        self.assertTrue(isinstance(site, Site))

    def test_create_siteinfo_from_site(self) -> None:
        """Create SiteInfo from sqlalchemy site"""
        test_site = Site(id=1, url='test.com', tag_id='test', hash='123', timestamp=1)
        siteinfo = create_siteinfo_from_site(test_site)
        self.assertTrue(isinstance(siteinfo, SiteInfo))

        test_site = Site(id=None, url='test.com', tag_id=None, hash=None, timestamp=1)
        siteinfo = create_siteinfo_from_site(test_site)
        self.assertTrue(isinstance(siteinfo, SiteInfo))

    def test_create_slackinfo_from_slack(self) -> None:
        """Create SlackInfo from sqlalchemy slack"""
        test_slack = Slack(id=1, webhook_url='test.com')
        slackinfo = create_slackinfo_from_slack(test_slack)
        expected_slackinfo = SlackInfo(id=1, webhook_url='test.com')
        self.assertTrue(isinstance(slackinfo, SlackInfo))
        self.assertEqual(slackinfo, expected_slackinfo)

        test_slack = Slack(id=None, webhook_url='test.com')
        slackinfo = create_slackinfo_from_slack(test_slack)
        expected_slackinfo = SlackInfo(webhook_url='test.com')
        self.assertTrue(isinstance(slackinfo, SlackInfo))
        self.assertEqual(slackinfo, expected_slackinfo)
