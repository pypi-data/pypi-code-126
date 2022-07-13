# -*- coding: utf-8 -*-
import unittest

from plone import api
from plone.app.testing import TEST_USER_ID, setRoles
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject, queryUtility

from newsletter.types.content.newsletter_container import (
    INewsletterContainer,  # NOQA E501
)
from newsletter.types.testing import NEWSLETTER_TYPES_INTEGRATION_TESTING  # noqa


class NewsletterContainerIntegrationTest(unittest.TestCase):

    layer = NEWSLETTER_TYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_newsletter_container_schema(self):
        fti = queryUtility(IDexterityFTI, name='NewsletterContainer')
        schema = fti.lookupSchema()
        self.assertEqual(INewsletterContainer, schema)

    def test_ct_newsletter_container_fti(self):
        fti = queryUtility(IDexterityFTI, name='NewsletterContainer')
        self.assertTrue(fti)

    def test_ct_newsletter_container_factory(self):
        fti = queryUtility(IDexterityFTI, name='NewsletterContainer')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            INewsletterContainer.providedBy(obj),
            u'INewsletterContainer not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_newsletter_container_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='NewsletterContainer',
            id='newsletter_container',
        )

        self.assertTrue(
            INewsletterContainer.providedBy(obj),
            u'INewsletterContainer not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('newsletter_container', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('newsletter_container', parent.objectIds())

    def test_ct_newsletter_container_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='NewsletterContainer')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_newsletter_container_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='NewsletterContainer')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'newsletter_container_id',
            title='NewsletterContainer container',
        )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
