from email.message import EmailMessage

import aiosmtplib

from . import models
from .settings import settings


async def mail(subject, body):
    if settings.SMTP_SERVER is None:
        print("No mail")
        return

    message = EmailMessage()
    message["From"] = settings.SMTP_FROM
    message["To"] = settings.SMTP_TO
    message["Subject"] = subject
    message.set_content(body)
    await aiosmtplib.send(
        message,
        hostname=settings.SMTP_SERVER,
        use_tls=True,
        username=settings.SMTP_LOGIN,
        password=settings.SMTP_PASS,
    )


async def comment_added(comment: models.Comment):
    subject = f"New comment in '{comment.thread.path}'"
    body = f"{comment.author_name} has added this comment:\n{comment.text}"
    await mail(subject, body)


async def comment_updated(comment: models.Comment):
    subject = f"Comment updated in '{comment.thread.path}'"
    body = f"{comment.author_name} has added this comment:\n{comment.text}"
    await mail(subject, body)


async def comment_deleted(comment: models.Comment):
    subject = f"Comment deleted in '{comment.thread.path}'"
    body = f"{comment.author_name} has deleted his comment:\n{comment.text}"
    await mail(subject, body)
