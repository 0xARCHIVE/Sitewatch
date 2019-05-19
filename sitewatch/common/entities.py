#!/usr/bin/env python3

"""
Entities:
Site
"""

from dataclasses import dataclass

@dataclass
class Site:
    """Site entity"""
    db_id: int
    url: str
