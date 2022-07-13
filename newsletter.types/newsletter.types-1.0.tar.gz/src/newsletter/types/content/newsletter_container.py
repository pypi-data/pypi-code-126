# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container

# from plone.namedfile import field as namedfile
from plone.supermodel import model

# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer

from newsletter.types import _


class INewsletterContainer(model.Schema):
    """Marker interface and Dexterity Python Schema for NewsletterContainer"""

    newsletter_header_image_url = schema.TextLine(
        title=_(u"newsletter_header_image_url"),
        required=False,
    )

    newsletter_footer_title = schema.TextLine(
        title=_(u"newsletter_footer_title"),
        required=False,
    )

    newsletter_footer_address = schema.TextLine(
        title=_(u"newsletter_footer_address"),
        required=False,
    )

    newsletter_footer_telephone = schema.TextLine(
        title=_(u"newsletter_footer_telephone"),
        required=False,
    )
    newsletter_news_title = schema.TextLine(
        title=_(u"newsletter_news_title"),
        required=False,
    )
    newsletter_news_url = schema.TextLine(
        title=_(u"newsletter_news_url"),
        required=False,
    )
    newsletter_news_morelinktext = schema.TextLine(
        title=_(u"newsletter_news_morelinktext"),
        required=False,
    )


@implementer(INewsletterContainer)
class NewsletterContainer(Container):
    """Content-type class for INewsletterContainer"""
