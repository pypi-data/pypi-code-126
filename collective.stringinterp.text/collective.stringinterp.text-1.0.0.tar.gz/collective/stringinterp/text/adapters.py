# -*- coding: utf-8 -*-

from zope.interface import implementer
from zope.component.interfaces import ComponentLookupError

from Products.CMFCore.utils import getToolByName

from plone.stringinterp.interfaces import IStringSubstitution
from plone.stringinterp.adapters import BaseSubstitution

# trick for don't campture category when running i18ndude
from plone.stringinterp import _ as PMF
# plone domain is used
from collective.stringinterp.text import _
from collective.stringinterp.text.interfaces import ITextExtractor


@implementer(IStringSubstitution)
class TextSubstitution(BaseSubstitution):
    """Full body text substitution"""

    category = PMF(u'All Content')
    description = _(u'Body text')

    def safe_call(self):
        try:
            adapter = ITextExtractor(self.context)
        except ComponentLookupError:
            return None
        if adapter.text:
            return "\n".join([l.strip() for l in adapter.text.splitlines()])
        return ""


@implementer(IStringSubstitution)
class IndentedTextSubstitution(TextSubstitution):
    """Like full body text substitution aobve, but with indentation chars"""

    description = _(u'Body text (indented)')

    def safe_call(self):
        text = TextSubstitution.safe_call(self)
        if text:
            return "\n".join(["\t" + l for l in text.splitlines()])


@implementer(ITextExtractor)
class PADiscussionTextExtractor(object):
    """Extract text field from plone.app.discussion comments"""

    def __init__(self, context):
        self.context = context

    @property
    def text(self):
        context = self.context
        text = context.getText()
        transforms = getToolByName(context, 'portal_transforms')
        stream = transforms.convertTo('text/plain', text, mimetype='text/html')
        return stream.getData().strip()


@implementer(ITextExtractor)
class DexterityTextExtractor(object):
    """Try to extract text from Dexterity contents
    """

    def __init__(self, context):
        self.context = context

    @property
    def text(self):
        context = self.context
        text = getattr(context, 'text', '')
        if isinstance(text, str):
            text = text
        else:
            text = getattr(context.text, 'output', '')
        transforms = getToolByName(context, 'portal_transforms')
        stream = transforms.convertTo('text/plain', text, mimetype='text/html')
        return stream.getData().strip()


@implementer(ITextExtractor)
class GeneralTextExtractor(object):
    """Try to extract text from something (AKA: there is a "text" attribute?)
    """

    def __init__(self, context):
        self.context = context

    @property
    def text(self):
        context = self.context
        text = getattr(context, 'text', '')
        if isinstance(text, str):
            text = text
        else:
            return ''
        transforms = getToolByName(context, 'portal_transforms')
        stream = transforms.convertTo('text/plain', text, mimetype='text/html')
        return stream.getData().strip()
