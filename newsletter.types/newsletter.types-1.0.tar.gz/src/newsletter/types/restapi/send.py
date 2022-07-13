from plone.restapi.deserializer import json_body
from plone.restapi.services import Service
from zope.interface import alsoProvides
import plone.protect.interfaces
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from cs.htmlmailer.mailer import create_html_mail


class SendEmail(Service):
    def reply(self):
        try:
            if "IDisableCSRFProtection" in dir(plone.protect.interfaces):
                alsoProvides(
                    self.request,
                    plone.protect.interfaces.IDisableCSRFProtection,
                )

            context = aq_inner(self.context)
            data = json_body(self.request)
            email_from = data.get("from", "")
            email_to = data.get("to", "")
            email_subject = data.get("subject", "")
            if email_from and email_to and email_subject:
                context = aq_inner(self.context)
                mail = create_html_mail(
                    email_subject,
                    context.text.raw,
                    from_addr=email_from,
                    to_addr=email_to,
                    cc_addrs=[],
                )
                mailhost = getToolByName(context, "MailHost")
                mailhost.send(mail.as_string())
                self.request.response.setStatus(200)
                return {
                    "message": "Newsletter well sent",
                }
            else:
                self.request.response.setStatus(400)
                return "You must fill in all the fields"

        except:
            return "Error creating the newsletter"
