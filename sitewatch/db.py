#!/usr/bin/env python3

"""
DB handlers
"""

from typing import List
from sqlalchemy import create_engine

from sitewatch.structs import SiteInfo, SlackInfo

class BaseDbHandler:
    """Base DB handler (abstract)"""
    def get_sites(self) -> List[SiteInfo]:
        """Return list of SiteInfo structs"""
        raise NotImplementedError

    def store_sites(self, sites: List[SiteInfo]) -> None:
        """Store list of SiteInfo structs"""
        raise NotImplementedError

    def get_slackinfo(self, site: SiteInfo) -> List[SlackInfo]:
        """Return list of SlackInfo structs for a site"""
        raise NotImplementedError

class MysqlHandler(BaseDbHandler):
    """MySQL DB handler"""
    def __init__(self, host: str, port: int, user: str, pwd: str, dbname: str):
        self.engine = create_engine(f'mysql+pymysql://{user}:{pwd}@{host}:{port}/{dbname}')

    def get_sites(self) -> List[SiteInfo]:
        """Return list of SiteInfo structs"""
        raise NotImplementedError

    def store_sites(self, sites: List[SiteInfo]) -> None:
        """Store list of SiteInfo structs"""
        raise NotImplementedError

    def get_slackinfo(self, site: SiteInfo) -> List[SlackInfo]:
        """Return list of SlackInfo structs for a site"""
        raise NotImplementedError

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sites(Base):
    __tablename__ = 'sites'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    tag_id = Column(String)
    contents_hash = Column(string)
    timestamp = Column(int)
"""
