# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.crime import Crime  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCrimesController(BaseTestCase):
    """CrimesController integration test stubs"""

    def test_crimes_get(self):
        """Test case for crimes_get

        Crimes
        """
        query_string = [('latitude', 1.2),
                        ('longitude', 1.2)]
        response = self.client.open(
            '/v1/crimes',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
