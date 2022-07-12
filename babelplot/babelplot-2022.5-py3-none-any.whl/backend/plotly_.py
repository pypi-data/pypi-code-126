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

from __future__ import annotations

from typing import Callable, Optional, TypeVar

import numpy as nmpy
import plotly.graph_objects as plly  # noqa
from plotly.basedatatypes import BasePlotlyType as backend_plot_t  # noqa
from plotly.graph_objects import Figure as backend_figure_t  # noqa
from plotly.subplots import make_subplots as NewMultiAxesFigure  # noqa

from babelplot.backend.brick.html import Show as BackendShow
from babelplot.backend.specification.implemented import backend_e
from babelplot.backend.specification.plot import (
    UNAVAILABLE_for_this_DIM,
    plot_e,
    plot_type_h,
)
from babelplot.brick.log import LOGGER
from babelplot.type.dimension import dim_e
from babelplot.type.figure import figure_t as base_figure_t
from babelplot.type.frame import frame_t as base_frame_t
from babelplot.type.plot import plot_t as base_plot_t


NAME = backend_e.PLOTLY.value


backend_frame_h = TypeVar("backend_frame_h")
backend_content_t = backend_figure_t


def _NewFrame(
    figure: backend_figure_t,
    __: int,
    ___: int,
    *args,
    title: str = None,
    dim: dim_e = dim_e.XY,  # If _, then it is swallowed by kwargs!
    **kwargs,
) -> backend_frame_h:
    """"""
    return None


def _NewPlot(
    _: backend_frame_h,
    type_: plot_type_h | type(backend_plot_t),
    plot_function: Optional[Callable],
    *args,
    title: str = None,  # If _, then it is swallowed by kwargs!
    **kwargs,
) -> tuple[backend_plot_t, type(backend_plot_t)]:
    """"""
    if plot_function is None:
        if hasattr(plly, type_):
            plot_function = getattr(plly, type_)
        else:
            LOGGER.error(f"{type_}: Unknown {NAME} graph object.")

    output = plot_function(*args, **kwargs)

    return output, plot_function


def _ContentFromArrangedFrames(
    figure: backend_figure_t, arranged_plots: list[list[list[backend_plot_t]]], /
) -> backend_content_t:
    """"""
    n_rows = arranged_plots.__len__()
    n_cols = arranged_plots[0].__len__()

    if (n_rows > 1) or (n_cols > 1):
        frame_types = [n_cols * [{}] for _ in range(n_rows)]
        for row, plot_row in enumerate(arranged_plots):
            for col, plot_cell in enumerate(plot_row):
                print(dir(plot_cell[0]))
                frame_types[row][col] = {"type": plot_cell[0].type}
        contents = NewMultiAxesFigure(rows=n_rows, cols=n_cols, specs=frame_types)
        for row, plot_row in enumerate(arranged_plots, start=1):
            for col, plot_cell in enumerate(plot_row, start=1):
                for plot in plot_cell:
                    contents.add_trace(plot, row=row, col=col)
    else:
        contents = figure
        for plot in arranged_plots[0][0]:
            contents.add_trace(plot)

    return contents


def _HTMLofContent(_, content: backend_content_t, *__, **___) -> str:
    """"""
    # Note on include_plotlyjs:
    #     "cdn": works but must be online
    #     True => blank figure if using PySide6.QtWebEngineWidgets.QWebEngineView.setHtml because of html size limit.
    #         See note in babelplot.backend.brick.html.Show
    return content.to_html(include_plotlyjs=True)


# noinspection PyTypeChecker
plot_t: base_plot_t = type("plot_t", (base_plot_t,), {})
# noinspection PyTypeChecker
frame_t: base_frame_t = type(
    "frame_t",
    (base_frame_t,),
    {"plot_class": plot_t, "NewBackendPlot": staticmethod(_NewPlot)},
)
# noinspection PyTypeChecker
figure_t: base_figure_t = type(
    "figure_t",
    (base_figure_t,),
    {
        "frame_class": frame_t,
        "NewBackendFigure": backend_figure_t,
        "NewBackendFrame": staticmethod(_NewFrame),
        "BackendShow": staticmethod(BackendShow),
        "HTMLofContent": staticmethod(_HTMLofContent),
        "ContentFromArrangedFrames": staticmethod(_ContentFromArrangedFrames),
    },
)


def _Scatter2(*args, **kwargs) -> backend_plot_t:
    """"""
    x, y = args

    return plly.Scatter(x=x, y=y, mode="markers", **kwargs)


def _Scatter3(*args, **kwargs) -> backend_plot_t:
    """"""
    x, y, z = args

    return plly.Scatter3d(x=x, y=y, z=z, mode="markers", **kwargs)


def _Polyline2(*args, **kwargs) -> backend_plot_t:
    """"""
    x, y = args

    return plly.Scatter(x=x, y=y, mode="lines", **kwargs)


def _ElevationSurface(*args, **kwargs) -> backend_plot_t:
    """"""
    if args.__len__() == 1:
        elevation = args[0]
        x, y = nmpy.meshgrid(
            range(elevation.shape[0]), range(elevation.shape[1]), indexing="ij"
        )
    else:
        x, y, elevation = args

    return plly.Surface(contours={}, x=x, y=y, z=elevation, **kwargs)


def _BarH(*args, **kwargs) -> backend_plot_t:
    """"""
    return _BarV(*args, orientation="h", **kwargs)


def _BarV(*args, **kwargs) -> backend_plot_t:
    """"""
    if args.__len__() == 1:
        counts = args[0]
        positions = tuple(range(counts.__len__()))
    else:
        positions, counts = args
    if kwargs.get("orientation") == "h":
        positions, counts = counts, positions

    return plly.Bar(x=positions, y=counts, **kwargs)


PLOTS = {
    plot_e.SCATTER: (
        UNAVAILABLE_for_this_DIM,
        _Scatter2,
        _Scatter3,
    ),
    plot_e.POLYLINE: (
        UNAVAILABLE_for_this_DIM,
        _Polyline2,
        UNAVAILABLE_for_this_DIM,
    ),
    plot_e.POLYGON: (
        UNAVAILABLE_for_this_DIM,
        UNAVAILABLE_for_this_DIM,
        UNAVAILABLE_for_this_DIM,
    ),
    plot_e.ARROWS: (
        UNAVAILABLE_for_this_DIM,
        UNAVAILABLE_for_this_DIM,
        UNAVAILABLE_for_this_DIM,
    ),
    plot_e.ELEVATION: (
        UNAVAILABLE_for_this_DIM,
        UNAVAILABLE_for_this_DIM,
        _ElevationSurface,
    ),
    plot_e.ISOSET: (
        UNAVAILABLE_for_this_DIM,
        plly.Contour,
        plly.Isosurface,
    ),
    plot_e.MESH: (
        UNAVAILABLE_for_this_DIM,
        UNAVAILABLE_for_this_DIM,
        plly.Mesh3d,
    ),
    plot_e.BARH: (
        UNAVAILABLE_for_this_DIM,
        _BarH,
        UNAVAILABLE_for_this_DIM,
    ),
    plot_e.BARV: (
        UNAVAILABLE_for_this_DIM,
        _BarV,
        UNAVAILABLE_for_this_DIM,
    ),
    plot_e.BAR3: (
        UNAVAILABLE_for_this_DIM,
        UNAVAILABLE_for_this_DIM,
        UNAVAILABLE_for_this_DIM,
    ),
    plot_e.PIE: (
        UNAVAILABLE_for_this_DIM,
        UNAVAILABLE_for_this_DIM,
        UNAVAILABLE_for_this_DIM,
    ),
    plot_e.IMAGE: (
        UNAVAILABLE_for_this_DIM,
        UNAVAILABLE_for_this_DIM,
        UNAVAILABLE_for_this_DIM,
    ),
}


TRANSLATIONS = {
    "alpha": "opacity",
    "color_face": "surfacecolor",
}
