# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest

from plone import api
from plone.app.testing import TEST_USER_ID, setRoles

from newsletter.types.testing import NEWSLETTER_TYPES_INTEGRATION_TESTING  # noqa: E501

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that newsletter.types is properly installed."""

    layer = NEWSLETTER_TYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if newsletter.types is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'newsletter.types'))

    def test_browserlayer(self):
        """Test that INewsletterTypesLayer is registered."""
        from plone.browserlayer import utils

        from newsletter.types.interfaces import INewsletterTypesLayer
        self.assertIn(
            INewsletterTypesLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = NEWSLETTER_TYPES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('newsletter.types')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if newsletter.types is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'newsletter.types'))

    def test_browserlayer_removed(self):
        """Test that INewsletterTypesLayer is removed."""
        from plone.browserlayer import utils

        from newsletter.types.interfaces import INewsletterTypesLayer
        self.assertNotIn(INewsletterTypesLayer, utils.registered_layers())
