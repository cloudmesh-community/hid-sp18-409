# coding: utf-8

"""
    Crimes API

    Identify crime prone areas near you  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.filter_crimes_api import FilterCrimesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestFilterCrimesApi(unittest.TestCase):
    """FilterCrimesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.filter_crimes_api.FilterCrimesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_crimes_filter_get(self):
        """Test case for crimes_filter_get

        crimeList based on primary_type  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()