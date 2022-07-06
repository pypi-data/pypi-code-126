# -*- coding: utf-8 -*-

import phonenumbers
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase


def create_email_message(
    mail_from: str,
    subject: str,
    text: str,
    mail_to: str = None,
    cc: str = None,
    bcc: str = None,
    html: str = None,
    attachments: list = None
) -> str:
    """ Create an email message

    :param mail_from
    :param mail_to
    :param subject
    :param text
    :param html
    :param attachments

    .. note:: it is possible to not have a mail_to, if there is a cc or bcc.
    """

    if attachments:
        msg = MIMEMultipart('mixed')
    elif text and html:
        msg = MIMEMultipart('alternative')
    else:
        msg = MIMEMultipart('alternative')

    msg['Subject'] = subject
    msg['From'] = mail_from

    if not (mail_to or cc or bcc):
        raise Exception(
            'mailMessage needs mail_to or cc or bcc!'
        )

    if mail_to:
        msg['To'] = mail_to
    if cc:
        msg['CC'] = cc
    if bcc:
        msg['BCC'] = bcc

    parts = []
    parts.append(MIMEText(text, 'plain', 'utf-8'))

    if html:
        parts.append(MIMEText(html, 'html', 'utf-8'))

    for attachment in attachments or []:
        attPart = MIMEBase(
            'application',
            'octet-stream'
        )
        attPart.set_payload(attachment['data'])
        encoders.encode_base64(attPart)
        attPart.add_header(
            'Content-Disposition',
            f"attachment; filename={attachment['filename']}"
        )
        parts.append(attPart)

    for part in parts:
        msg.attach(part)

    return msg


def process_phonenumber(
    phonenumber: str,
    numberfmt: str = 'international',
    checkonly: bool = False,
    return_valid_only: bool = False
) -> str:
    """ process phonenumber and return in specified format

    Checks if a phonenumber is valid, returns in specified format.

    .. note:: If return_valid_only is True, an empty string is returned
        (so the result can still be concatenaed) or otherwise processed as a string

    :param number_str: phone number string to be processed
    :param numberfmt: format in which the number is returned
    """

    phonenumber = ''.join(c for c in phonenumber if c in '01234567890+')

    try:
        pn = phonenumbers.parse(phonenumber, 'AT')  # country code will be parsed nonetheless
    except phonenumbers.phonenumberutil.NumberParseException:
        error_str = ' (not a phone number)'
        return phonenumber + error_str

    error_str = ''

    if not phonenumbers.is_possible_number(pn):
        if checkonly:
            return False

        if return_valid_only:
            return ''

        error_str = ' (impossible)'

    elif not phonenumbers.is_valid_number(pn):
        if checkonly:
            return False
        if return_valid_only:
            return ''

        error_str = ' (invalid)'

    if checkonly:
        return True
    else:
        return phonenumbers.format_number(
            pn,
            phonenumbers.PhoneNumberFormat.INTERNATIONAL
        ) + error_str
