#!/usr/bin/env python3

"""
Slack module
"""

from typing import Dict

import requests

def send_message(webhook_url: str, message: str) -> None:
    """Send message to Slack"""
    if not isinstance(webhook_url, str):
        raise TypeError('Expected string webhook_url, got {}'.format(type(webhook_url)))
    json_data = _build_request(message)
    requests.post(webhook_url, json=json_data)

def _build_request(message: str) -> Dict[str, str]:
    """Build a JSON request for Slack message"""
    if not isinstance(message, str):
        raise TypeError('Expected string message, got {}'.format(type(message)))
    return {'text': message}
