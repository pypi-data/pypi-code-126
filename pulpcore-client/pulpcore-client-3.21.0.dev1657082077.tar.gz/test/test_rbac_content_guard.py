# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.rbac_content_guard import RBACContentGuard  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException

class TestRBACContentGuard(unittest.TestCase):
    """RBACContentGuard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RBACContentGuard
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulpcore.models.rbac_content_guard.RBACContentGuard()  # noqa: E501
        if include_optional :
            return RBACContentGuard(
                name = '0', 
                description = '0'
            )
        else :
            return RBACContentGuard(
                name = '0',
        )

    def testRBACContentGuard(self):
        """Test RBACContentGuard"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
