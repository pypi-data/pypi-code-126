# coding: utf-8

import json

import requests
from sentry.plugins.bases.notify import NotificationPlugin
from sentry_plugins.base import CorePluginMixin
from sentry.integrations import FeatureDescription, IntegrationFeatures

import sentry_feishu
from .forms import FeiShuOptionsForm

FeiShuTalk_API = "https://open.feishu.cn/open-apis/bot/v2/hook/{token}"


class FeiShuPlugin(CorePluginMixin, NotificationPlugin):
    """
    Sentry plugin to send error counts to FeiShu.
    """
    author = 'feng.chen'
    author_url = 'https://github.com/jnchenfeng/sentry_feishu'
    version = sentry_feishu.VERSION
    description = 'Send error counts to FeiShu.'
    resource_links = [
        ('Source', 'https://github.com/jnchenfeng/sentry_feishu'),
        ('Bug Tracker', 'https://github.com/jnchenfeng/sentry_feishu/issues'),
        ('README', 'https://github.com/jnchenfeng/sentry_feishu/blob/master/README.md'),
    ]

    slug = 'FeiShu'
    title = 'FeiShu'
    conf_key = slug
    conf_title = title
    project_conf_form = FeiShuOptionsForm
    feature_descriptions = [
        FeatureDescription(
            """
            Configure Sentry rules to trigger notifications based on conditions you set.
            """,
            IntegrationFeatures.ALERT_RULE,
        ),
    ]

    def is_configured(self, project):
        """
        Check if plugin is configured.
        """
        return bool(self.get_option('access_token', project))

    def notify_users(self, group, event, *args, **kwargs):
        if not self.is_configured(group.project):
            return
        self.post_process(group, event, *args, **kwargs)

    def post_process(self, group, event, *args, **kwargs):
        """
        Process error.
        """
        if not self.should_notify(group, event):
            return
        access_token = self.get_option('access_token', group.project)
        send_url = FeiShuTalk_API.format(token=access_token)
        project = event.group.project
        title = event.title.encode("utf-8").decode("utf-8")
        project_name = project.get_full_name().encode("utf-8").decode("utf-8")
        body = b"Sentry [%s] %s: %s" % (
            project.name.encode("utf-8"),
            event.group.get_level_display().upper().encode("utf-8"),
            event.title.encode("utf-8").splitlines()[0],
        )
        data = {"title": title, "msg_type": "text",
                "content": {"text": "{title} \n > {body}; \n[href]({url})".format(
                    title=title,
                    project_name=project_name,
                    body=body,
                    url=u"{}events/{}/".format(group.get_absolute_url(), event.event_id),
                )}}
        requests.post(
            send_url,
            json=data
        )
