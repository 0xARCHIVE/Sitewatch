#!/usr/bin/env python3

"""
MySQL DB handler
"""

from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from sitewatch.db.base import BaseDbHandler
from sitewatch.structs import SiteInfo, SlackInfo

Base = declarative_base() # pylint: disable=invalid-name

class MysqlHandler(BaseDbHandler):
    """MySQL DB handler"""
    def __init__(self, host: str, port: int, user: str, pwd: str, dbname: str):
        self.engine = create_engine(f'mysql+pymysql://{user}:{pwd}@{host}:{port}/{dbname}')
        session_maker = sessionmaker(bind=self.engine)
        self.session = session_maker()

        Base.metadata.create_all(self.engine)

    def get_sites(self) -> List[SiteInfo]:
        """Return list of SiteInfo structs"""
# get Sites from db session
# convert Site to SiteInfo
        raise NotImplementedError

    def store_sites(self, sites: List[SiteInfo]) -> None:
        """Store list of SiteInfo structs"""
# convert SiteInfo to Site
# store Site using db session
        raise NotImplementedError

    def get_slackinfo(self, site: SiteInfo) -> List[SlackInfo]:
        """Return list of SlackInfo structs for a site"""
# get Slacks from db session
# convert Slack to SlackInfo
        raise NotImplementedError

class Site(Base): # pylint: disable=too-few-public-methods
    """Site table"""
    __tablename__ = 'site'

    id = Column(Integer, primary_key=True) # pylint: disable=invalid-name
    url = Column(String(250))
    tag_id = Column(String(250), nullable=True)
    hash = Column(String(250), nullable=True)
    timestamp = Column(Integer)
    slacks = relationship('Slack', secondary='site_slack_link')

class Slack(Base): # pylint: disable=too-few-public-methods
    """Slack table"""
    __tablename__ = 'slack'
    id = Column(Integer, primary_key=True) # pylint: disable=invalid-name
    webhook_url = Column(String(250))
    sites = relationship('Site', secondary='site_slack_link')

class Link(Base): # pylint: disable=too-few-public-methods
    """Site-Slack link table"""
    __tablename__ = 'site_slack_link'
    site_id = Column(Integer, ForeignKey('site.id'), primary_key=True)
    slack_id = Column(Integer, ForeignKey('slack.id'), primary_key=True)

def create_site_from_siteinfo(site: SiteInfo) -> Site:
    """Create Site object (SqlAlchemy) from SiteInfo"""
    return Site(id=site.id, url=site.url, tag_id=site.tag_id,
                hash=site.hash, timestamp=site.timestamp)

def create_siteinfo_from_site(site: Site) -> SiteInfo:
    """Create SiteInfo from Site object (SqlAlchemy)"""
    return SiteInfo(id=site.id, url=site.url, tag_id=site.tag_id,
                    hash=site.hash, timestamp=site.timestamp)

def create_slackinfo_from_slack(slack: Slack) -> SlackInfo:
    """Create SlackInfo from Slack object (SqlAlchemy)"""
    return SlackInfo(id=slack.id, webhook_url=slack.webhook_url)
