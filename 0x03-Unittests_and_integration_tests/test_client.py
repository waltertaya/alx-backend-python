#!/usr/bin/env python3
''' Unittest for the client.py
'''

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    ''' TestCases for GithubOrgClient class
    '''

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        test_instance = GithubOrgClient(org_name)
        test_instance.org()
        mock_get_json.called_with_once(test_instance.ORG_URL.format(org=org_name))


if __name__ == '__main__':
    unittest.main()
