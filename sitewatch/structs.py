#!/usr/bin/env python3

"""
Structs:
SiteInfo
SlackInfo
"""

import time
from typing import Optional
from dataclasses import dataclass

@dataclass
class SiteInfo:
    """Site struct"""
    url: str
    id: Optional[int] = None # pylint: disable=invalid-name
    tag_id: Optional[str] = None
    hash: Optional[str] = None
    timestamp: int = int(time.time())

@dataclass
class SlackInfo:
    """Slack struct"""
    webhook_url: str
    id: Optional[int] = None # pylint: disable=invalid-name
