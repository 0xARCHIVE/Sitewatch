#!/usr/bin/env python3

"""
Base DB handler (abstract)
"""

from typing import List

from sitewatch.structs import SiteInfo

class BaseDbHandler:
    """Base DB handler (abstract)"""
    def get_sites(self) -> List[SiteInfo]:
        """Return list of SiteInfo structs"""
        raise NotImplementedError

    def store_sites(self, sites: List[SiteInfo]) -> None:
        """Store list of SiteInfo structs"""
        raise NotImplementedError
