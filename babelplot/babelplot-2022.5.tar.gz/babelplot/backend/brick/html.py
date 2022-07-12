# Copyright CNRS/Inria/UCA
# Contributor(s): Eric Debreuve (since 2022)
#
# eric.debreuve@cnrs.fr
#
# This software is governed by the CeCILL  license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

import os as osys
import tempfile as tmpf
from typing import Optional, Protocol, TypeVar

from PySide6.QtCore import QUrl as url_t
from PySide6.QtWebEngineWidgets import QWebEngineView as widget_t
from PySide6.QtWidgets import QApplication as application_t

from babelplot.type.base import backend_figure_h, backend_frame_h
from babelplot.type.figure import figure_t


backend_content_h = TypeVar("backend_content_h")


class html_p(Protocol):
    def ContentFromArrangedFrames(
        self, arranged_frames: list[list[Optional[backend_frame_h]]], /
    ) -> backend_content_h:
        ...

    @staticmethod
    def HTMLofContent(
        figure: backend_figure_h, content: backend_content_h, *args, **kwargs
    ) -> str:
        ...


def Show(figure: figure_t | html_p, /) -> None:
    """"""
    arranged_frames: list[list[Optional[backend_frame_h]]]
    arranged_frames = [figure.shape[1] * [None] for _ in range(figure.shape[0])]
    for frame, (row, col) in zip(figure.frames, figure.locations):
        if frame.backend is None:
            frame_or_plot = [_plt.backend for _plt in frame.plots]
        else:
            frame_or_plot = frame.backend
        arranged_frames[row][col] = frame_or_plot

    content = figure.ContentFromArrangedFrames(figure.backend, arranged_frames)
    html = figure.HTMLofContent(figure.backend, content)

    # The application must be instantiated in the same thread/process as the one running exec()
    if (application := application_t.instance()) is None:
        application = application_t()

    widget = widget_t()
    SetHTMLFromFile = lambda sss: _SetHTMLFromFile(sss, widget, html)
    widget.loadFinished.connect(SetHTMLFromFile)
    widget.setHtml(html)
    widget.show()

    application.exec()


def _SetHTMLFromFile(success: bool, widget: widget_t, html: str, /) -> None:
    """
    From: https://doc.qt.io/qtforpython-6/PySide6/QtWebEngineWidgets/QWebEngineView.html#PySide6.QtWebEngineWidgets.PySide6.QtWebEngineWidgets.QWebEngineView.setHtml
        Content larger than 2 MB cannot be displayed...
        ...
        Thereby, the provided code becomes a URL that exceeds the 2 MB limit set by Chromium.
        If the content is too large, the loadFinished() signal is triggered with success=false.
    Solution: Use a temporary file (with html extension) and setUrl.
    """
    if not success:
        transfer = tmpf.NamedTemporaryFile(mode="w", suffix=".html", delete=False)
        with open(transfer.name, "w") as accessor:
            accessor.write(html)
        url = url_t.fromLocalFile(transfer.name)
        widget.setUrl(url)
        DeleteTemporaryFile = lambda: osys.remove(transfer.name)
        application_t.instance().lastWindowClosed.connect(DeleteTemporaryFile)
