#!/usr/bin/env python3

"""
MySQL DB handler tests
"""

import unittest
from unittest.mock import patch, Mock

from sitewatch.db.mysql import MysqlHandler
from sitewatch.db.mysql import Slack, create_slackinfo_from_slack
from sitewatch.db.mysql import Site, create_site_from_siteinfo, create_siteinfo_from_site
from sitewatch.structs import SiteInfo, SlackInfo

class TestMysqlHandler(unittest.TestCase):
    """MySQL DB handler tests"""
    def setUp(self) -> None:
        """Per-test setup"""
        # mock MysqlHandler.__init__ with a lambda that does nothing
        with patch.object(MysqlHandler, '__init__', lambda a, b, c, d, e, f: None):
            self.handler = MysqlHandler('test', 3306, 'test', 'test', 'test')

    def test_get_sites(self) -> None:
        """Test get_sites - successful"""
        mock_site = Mock(spec=Site)

        mock_session = Mock()
        mock_session.query.return_value = Mock()
        mock_session.query.return_value.all.return_value = [mock_site]

        self.handler.session = mock_session
        result = self.handler.get_sites()
        self.assertEqual(len(result), 1)
        self.assertTrue(isinstance(result[0], SiteInfo))

    def test_get_sites_none(self) -> None:
        """Test get_sites - query returned empty list"""

    def test_get_sites_error(self) -> None:
        """Test get_sites - query threw an error"""

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
