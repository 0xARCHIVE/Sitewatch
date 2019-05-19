#!/usr/bin/env python3

"""
Sitewatch client
"""

from typing import List

from sitewatch.db import BaseDbHandler
from sitewatch.common.entities import Site

class SitewatchClient:
    """Sitewatch client"""
    def __init__(self, db_handler: BaseDbHandler) -> None:
        self.db_handler = db_handler

    def check_all_for_updates(self, notify: bool = True) -> List[Site]:
        """Check all sites for updates, return list of updates sites"""
        raise NotImplementedError
