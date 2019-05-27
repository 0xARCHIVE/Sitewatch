#!/usr/bin/env python3

"""
Base DB handler
"""

from typing import List

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
