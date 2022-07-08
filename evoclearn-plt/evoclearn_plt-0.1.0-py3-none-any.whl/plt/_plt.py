# -*- coding: utf-8 -*-

from xml.etree import ElementTree
from tempfile import NamedTemporaryFile

import cairosvg
from svgpathtools import svg2paths, Path
import matplotlib.pyplot as plt
import matplotlib.image as pli
import matplotlib.animation as animation
import numpy as np

from evoclearn.core import VOCALTRACT_PARAMS
from evoclearn.core import vocaltractlab as vtl


def _fix_vtl_svg_bbox_inplace(svgfn, padpx=10):
    paths, _ = svg2paths(svgfn)
    path = Path(*paths)
    xmin, xmax, ymin, ymax = path.bbox()
    width = xmax - xmin
    height = ymax - ymin
    doc = ElementTree.parse(svgfn)
    rootelem = next(doc.iter())
    rootelem.set("viewBox", f"{xmin-padpx} {ymin-padpx} {width+(2*padpx)} {height+(2*padpx)}")
    doc.write(svgfn)


def plot_targets(seq):
    fig, axs = plt.subplots(1, len(seq), figsize=(5*len(seq), 5))
    for i in range(len(seq)):
        t = seq.iloc[i][list(VOCALTRACT_PARAMS)]
        with NamedTemporaryFile() as outfh:
            vtl.tract_to_svg_file(t, outfh.name)
            _fix_vtl_svg_bbox_inplace(outfh.name)
            with NamedTemporaryFile() as outfh2:
                cairosvg.svg2png(outfh.read(), write_to=outfh2.name)
                img = pli.imread(outfh2.name)
        axs[i].imshow(img)
        axs[i].set_title(seq.index[i])
        axs[i].set_xticks([])
        axs[i].set_yticks([])
    return fig


def plot_trajectory(seq, **kwargs):
    fig, ax = plt.subplots()
    ims = []
    for i in range(len(seq)):
        t = seq.iloc[i][list(VOCALTRACT_PARAMS)]
        with NamedTemporaryFile() as outfh:
            vtl.tract_to_svg_file(t, outfh.name)
            _fix_vtl_svg_bbox_inplace(outfh.name)
            with NamedTemporaryFile() as outfh2:
                cairosvg.svg2png(outfh.read(), write_to=outfh2.name)
                img = pli.imread(outfh2.name)
                im = ax.imshow(img)
                ims.append([im])
    anim = animation.ArtistAnimation(fig, ims, **kwargs)
    plt.close()
    return anim


def _plot_tube(tube, ax, title, ylim):
    tube_locations = list(np.cumsum(tube.tubes["tube_length"].to_numpy()))
    tube_areas = list(tube.tubes["tube_area"])
    ax.step([0.0] + tube_locations, tube_areas[:1] + tube_areas, lw=3, label=title)
    ax.set_xlim(0.0, tube_locations[-1])
    ax.set_ylim(0.0, None)
    xticks = np.cumsum(tube.tubes["tube_length"])
    ax.set_xticks(xticks)
    ax.set_xticklabels(np.around(xticks, decimals=2), rotation=60, ha="right")
    ax.set_xlabel("tube length (cm)")
    ax.set_ylabel("cross-sectional area (cm²)")
    ax.grid(True)
    ax.legend(loc="best")
    ax2 = ax.twiny()
    ax2.set_xlim(0.0, tube_locations[-1])
    ax2.set_xticks(np.cumsum(tube.tubes["tube_length"]))
    ax2.set_xticklabels([e[1] for e in tube.tubes.index], rotation=60, ha="left")
    ax2.set_ylim(*ylim)


def plot_tubes(seq, orientation="horizontal", figsize=(30, 8), ylim=(0.0, 9.0)):
    if orientation == "horizontal":
        plotgrid = (1, len(seq))
    elif orientation == "vertical":
        plotgrid = (len(seq), 1)
    else:
        raise NotImplementedError(f"orientation={orientation}")
    fig, axs = plt.subplots(*plotgrid, figsize=figsize)
    for i in range(len(seq)):
        t = seq.iloc[i][list(VOCALTRACT_PARAMS)]
        tube = vtl.tube(t)
        _plot_tube(tube, axs[i], str(seq.index[i]), ylim)
    return fig
