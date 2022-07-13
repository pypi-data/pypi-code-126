# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    applyProfile,
)
from plone.testing import z2

import newsletter.types


class NewsletterTypesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=newsletter.types)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'newsletter.types:default')


NEWSLETTER_TYPES_FIXTURE = NewsletterTypesLayer()


NEWSLETTER_TYPES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(NEWSLETTER_TYPES_FIXTURE,),
    name='NewsletterTypesLayer:IntegrationTesting',
)


NEWSLETTER_TYPES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(NEWSLETTER_TYPES_FIXTURE,),
    name='NewsletterTypesLayer:FunctionalTesting',
)


NEWSLETTER_TYPES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        NEWSLETTER_TYPES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='NewsletterTypesLayer:AcceptanceTesting',
)
