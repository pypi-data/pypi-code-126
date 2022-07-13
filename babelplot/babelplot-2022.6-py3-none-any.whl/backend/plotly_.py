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

from babelplot.backend.brick.html import Show
from babelplot.backend.specification.implemented import backend_e
from babelplot.backend.specification.plot import PlotsFromTemplate, plot_e, plot_type_h
from babelplot.brick.log import LOGGER
from babelplot.type.figure import figure_t as base_figure_t
from babelplot.type.frame import frame_t as base_frame_t
from babelplot.type.plot import plot_t as base_plot_t


NAME = backend_e.PLOTLY.value


array_t = nmpy.ndarray
backend_frame_h = TypeVar("backend_frame_h")


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

    return plot_function(*args, **kwargs), plot_function


def _NewFrame(*_, **__) -> backend_frame_h:
    """"""
    return None


def _AsHTML(figure: figure_t, /) -> str:
    """"""
    n_rows, n_cols = figure.shape
    if (n_rows > 1) or (n_cols > 1):
        arranged_plots = [n_cols * [None] for _ in range(n_rows)]
        for frame, (row, col) in zip(figure.frames, figure.locations):
            arranged_plots[row][col] = [_plt.backend for _plt in frame.plots]

        frame_types = [n_cols * [{}] for _ in range(n_rows)]
        for row, plot_row in enumerate(arranged_plots):
            for col, plot_cell in enumerate(plot_row):
                frame_types[row][col] = {"type": plot_cell[0].type}

        contents = NewMultiAxesFigure(rows=n_rows, cols=n_cols, specs=frame_types)
        for row, plot_row in enumerate(arranged_plots, start=1):
            for col, plot_cell in enumerate(plot_row, start=1):
                for plot in plot_cell:
                    contents.add_trace(plot, row=row, col=col)
    else:
        contents = figure.backend
        for plot in figure.frames[0].plots:
            contents.add_trace(plot.backend)

    # Note on include_plotlyjs:
    #     "cdn": works but must be online
    #     True => blank figure if using PySide6.QtWebEngineWidgets.QWebEngineView.setHtml because of html size limit.
    #         See note in babelplot.backend.brick.html.Show
    return contents.to_html(include_plotlyjs=True)


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
        "BackendShow": Show,
        "AsHTML": _AsHTML,
    },
)


def _Scatter2(x, y, **kwargs) -> backend_plot_t:
    """"""
    return plly.Scatter(x=x, y=y, mode="markers", **kwargs)


def _Scatter3(x, y, z, **kwargs) -> backend_plot_t:
    """"""
    return plly.Scatter3d(x=x, y=y, z=z, mode="markers", **kwargs)


def _Polyline2(x, y, **kwargs) -> backend_plot_t:
    """"""
    return plly.Scatter(x=x, y=y, mode="lines", **kwargs)


def _Polyline3(x, y, z, **kwargs) -> backend_plot_t:
    """"""
    return plly.Scatter3d(x=x, y=y, z=z, mode="lines", **kwargs)


def _Polygon(xs: array_t, ys: array_t, *_, **kwargs) -> backend_plot_t:
    """"""
    xs = nmpy.concatenate((xs, [xs[0]]))
    ys = nmpy.concatenate((ys, [ys[0]]))

    return plly.Scatter(x=xs, y=ys, mode="lines", fill="toself", **kwargs)


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


def _Isocontour(*args, **kwargs) -> backend_plot_t:
    """"""
    if args.__len__() == 2:
        x = y = None
        values, value = args
    else:
        x, y, values, value = args
    parameters = {
        "z": values,
        "contours": {"start": value, "end": value, "size": 1, "showlabels": True},
        "contours_coloring": "lines",
        "line_width": 2,
    }
    if x is not None:
        parameters["x"] = x
        parameters["y"] = y
    parameters.update(kwargs)

    return plly.Contour(**parameters)


def _Isosurface(values, value, **kwargs) -> backend_plot_t:
    """"""
    if ("X" in kwargs) and ("Y" in kwargs) and ("Z" in kwargs):
        x = kwargs["x"]
        y = kwargs["y"]
        z = kwargs["z"]
    else:
        x, y, z = nmpy.meshgrid(
            range(values.shape[0]),
            range(values.shape[1]),
            range(values.shape[2]),
            indexing="ij",
        )

    return plly.Isosurface(
        x=x.flatten(),
        y=y.flatten(),
        z=z.flatten(),
        value=values.flatten(),
        isomin=value,
        isomax=value,
        # surface_count=1,
        # caps={"x_show": False, "y_show": False},
    )


def _Mesh(triangles: array_t, vertices: array_t, **kwargs) -> backend_plot_t:
    """"""
    return plly.Mesh3d(
        x=vertices[:, 0],
        y=vertices[:, 1],
        z=vertices[:, 2],
        i=triangles[:, 0],
        j=triangles[:, 1],
        k=triangles[:, 2],
    )


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


def _Pie(values, **kwargs) -> backend_plot_t:
    """"""
    return plly.Pie(values=values)


def _Image(image: array_t, **kwargs) -> backend_plot_t:
    """"""
    if image.ndim == 2:
        return plly.Heatmap(z=image)

    return plly.Image(z=image)


PLOTS = PlotsFromTemplate()

PLOTS[plot_e.SCATTER][1] = _Scatter2
PLOTS[plot_e.POLYLINE][1] = _Polyline2
PLOTS[plot_e.POLYGON][1] = _Polygon
PLOTS[plot_e.ISOSET][1] = _Isocontour
PLOTS[plot_e.BARH][1] = _BarH
PLOTS[plot_e.BARV][1] = _BarV
PLOTS[plot_e.PIE][1] = _Pie
PLOTS[plot_e.IMAGE][1] = _Image

PLOTS[plot_e.SCATTER][2] = _Scatter3
PLOTS[plot_e.POLYLINE][2] = _Polyline3
PLOTS[plot_e.ELEVATION][2] = _ElevationSurface
PLOTS[plot_e.ISOSET][2] = _Isosurface
PLOTS[plot_e.MESH][2] = _Mesh


TRANSLATIONS = {
    "alpha": "opacity",
    "color_face": "surfacecolor",
}
