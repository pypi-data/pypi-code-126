from PySide2 import QtWidgets, QtGui
from ciohoudini.buttoned_scroll_panel import ButtonedScrollPanel
from ciohoudini.notice_grp import NoticeGrp
# from ciohoudini import submit
from ciocore import config
import urllib.parse

class ResponseTab(ButtonedScrollPanel):

    def __init__(self, dialog):
        super(ResponseTab, self).__init__(dialog,
            buttons=[("close","Close") ])

    def populate(self,response):
        cfg = config.config().config

        print("response:", response)
        if response.get("code") in [200, 201, 204]:
            success_uri = response["response"]["uri"].replace("jobs", "job")
            url = urllib.parse.urljoin(cfg["url"], success_uri)
            message = "Success!\nClick to go to the Dashboard.\n{}".format(url)
            widget = NoticeGrp(message, "success", url)

        else:
            widget = NoticeGrp(response.get("response", "Can't get response"), "error")

        self.layout.addWidget(widget)
        self.layout.addStretch()

        self.configure_signals()

    def configure_signals(self):
        self.buttons["close"].clicked.connect(self.dialog.on_close)
