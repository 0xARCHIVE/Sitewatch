#!/usr/bin/env python3

"""
Example - use Sitewatch client to check all sites for updates
"""

from sitewatch import SitewatchClient
from sitewatch.db import MysqlHandler

def check_all_for_updates():
    """Example - use Sitewatch client to check all sites for updates"""
    mysql = MysqlHandler(host='host', port=123, user='user', pwd='pwd')
    client = SitewatchClient(db_handler=mysql)

    # check all sites for updates & automatically send out Slack notifications
    # returns a list of updated sites
    sites = client.check_all_for_updates(notify=True)
    print(len(sites))
