#!/usr/bin/env python3

"""
Test Slack module
"""

import unittest
from unittest.mock import patch

#from sitewatch.slack import send_message
from sitewatch.slack import _build_request, send_message

class TestSendMessage(unittest.TestCase):
    """Test send_message"""
    def test_build_request(self) -> None:
        """Test build request valid input"""
        message = 'hello world'
        expected_json = {'text': 'hello world'}
        self.assertEqual(expected_json, _build_request(message))

    def test_build_request_bad(self) -> None:
        """Test build requests invalid input"""
        with self.assertRaises(TypeError):
            _build_request(1)

    def test_build_requests_empty(self) -> None:
        """Test build requests empty input"""
        with self.assertRaises(TypeError):
            _build_request() # pylint: disable=no-value-for-parameter

    @patch('requests.post')
    @patch('sitewatch.slack._build_request')
    def test_send_message(self, mock_build_req, mock_post) -> None:
        """Test send message valid input"""
        webhook_url = 'https://www.example.com'
        message = 'test'
        json_data = {'text': 'test'}
        mock_build_req.return_value = json_data

        send_message(webhook_url, message)
        mock_post.assert_called_with(webhook_url, json=json_data)

    def test_send_message_bad(self) -> None:
        with self.assertRaises(TypeError):
            send_request(1, 'test')
