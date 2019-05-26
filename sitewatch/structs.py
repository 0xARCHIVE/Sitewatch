#!/usr/bin/env python3

"""
Structs:
Site
"""

from typing import Optional
from dataclasses import dataclass

@dataclass
class SiteInfo:
    """Site struct"""
    _id: int
    url: str
    tag_id: Optional[str]
    hash: Optional[str]
    timestamp: int

@dataclass
class SlackInfo:
    """Slack struct"""
    _id: int
    webhook_url: str
    site_id: int
