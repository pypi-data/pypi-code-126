import logging, os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from mpl_toolkits.axes_grid1 import make_axes_locatable

from SuPyMode.Plotting.PlotsUtils  import FieldMap, MidPointNorm
from SuPyMode.Tools.utils import ToList

import matplotlib
matplotlib.style.use('ggplot')



class Text():
    def __init__(self, Text, Position=[0,0], FontSize=8):
        self.Text = Text
        self.Position = Position
        self.FontSize = FontSize

    def Render(self, Ax):
        Ax.get_figure().text(x=0.1,#self.Position[0],
                y=0.9,#self.Position[1],
                s=self.Text,
                horizontalalignment='left',
                verticalalignment='bottom',
                fontsize  = self.FontSize,
                bbox      = dict(facecolor='white', edgecolor = 'black', boxstyle  = 'round'))


class Contour:
    def __init__(self, X, Y, Scalar, ColorMap='viridis', Title=None, xLabel=None, yLabel=None, IsoLines=None):
        self.X = X
        self.Y = Y
        self.Scalar = Scalar
        self.ColorMap = ColorMap
        self.Label = Label
        self.IsoLines = IsoLines


    def Render(self, Ax):
        Image = Ax.contour(self.X,
                            self.Y,
                            self.Scalar,
                            level = self.IsoLines,
                            colors="black",
                            linewidth=.5 )

        Image = Ax.contourf(self.X,
                            self.Y,
                            self.Scalar,
                            level = self.IsoLines,
                            cmap=self.ColorMap,
                            norm=colors.LogNorm() )



class Mesh:
    def __init__(self, X, Y, Scalar, ColorMap='viridis', DiscretNorm=False, Label=''):
        self.X = X
        self.Y = Y
        self.Scalar = Scalar
        self.ColorMap=ColorMap
        self.Label = Label


        self.Norm = colors.BoundaryNorm(DiscretNorm, 200, extend='both') if DiscretNorm is not False else None


    def Render(self, Ax):
        Image = Ax.pcolormesh(self.X,
                              self.Y,
                              self.Scalar,
                              cmap    = self.ColorMap,
                              shading = 'auto',
                              norm = self.Norm
                              )

        return Image



class FillLine:
    def __init__(self, X, Y0, Y1, Label=None, Color=None):
        self.X = X
        self.Y0 = Y0
        self.Y1 = Y1
        self.Label = Label
        self.Color = Color

    def Render(self, Ax):
        Ax.fill_between(self.X, self.Y0, self.Y1, color=self.Color, alpha=0.7)



class Line:
    def __init__(self, X, Y, Label=None, Fill=False, Color=None):
        self.X = X
        self.Y = Y
        self.Fill = Fill
        self.Label = Label
        self.Color = Color

    def Render(self, Ax):

        Ax.plot(self.X, self.Y, label=self.Label)

        if self.Fill:
            Ax.fill_between(self.X, self.Y.min(), self.Y, color=self.Color, alpha=0.7)



class Axis:
    def __init__(self, Row, Col, xLabel, yLabel, Title, Grid=True, Legend=True, LegendFontsize=7, xScale='linear', yScale='linear', xLimits=None, yLimits=None, Equal=False, ColorBar=False, ColorbarPosition='bottom'):
        self.Row    = Row
        self.Col    = Col
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.Title  = Title
        self.Legend = Legend
        self.LegendFontsize = LegendFontsize
        self.Artist = []
        self.MPLAxis = None
        self.Grid    = Grid
        self.xScale  = xScale
        self.yScale  = yScale
        self.xLimits = xLimits
        self.yLimits = yLimits
        self.Equal   = Equal
        self.ColorBar = ColorBar
        self.ColorbarPosition = ColorbarPosition


    def AddArtist(self, *Artist):
        for art in Artist:
            self.Artist.append(art)

    def Render(self):
        for art in self.Artist:
            Image = art.Render(self.MPLAxis)

        if self.Legend:
            self.MPLAxis.legend(fontsize=self.LegendFontsize, facecolor='white', edgecolor='k')

        self.MPLAxis.grid(self.Grid)

        if self.xLimits is not None: self.MPLAxis.set_xlim(self.xLimits)
        if self.yLimits is not None: self.MPLAxis.set_ylim(self.yLimits)

        self.MPLAxis.set_xlabel(self.xLabel)
        self.MPLAxis.set_ylabel(self.yLabel)
        self.MPLAxis.set_title(self.Title)

        self.MPLAxis.set_xscale(self.xScale)
        self.MPLAxis.set_yscale(self.yScale)

        if self.Equal:
            self.MPLAxis.set_aspect("equal")

        if self.ColorBar:
            divider = make_axes_locatable(self.MPLAxis)
            cax = divider.append_axes(self.ColorbarPosition, size="5%", pad=0.05)
            plt.colorbar(Image, cax=cax, )




class Scene:
    UnitSize = (10, 5)
    plt.rcParams['ytick.labelsize'] = 8
    plt.rcParams['xtick.labelsize'] = 8
    plt.rcParams["font.size"]       = 8
    plt.rcParams["font.family"]     = "serif"
    plt.rcParams['axes.edgecolor'] = 'black'
    plt.rcParams['axes.linewidth'] = 1.5

    def __init__(self, Title='', UnitSize=None):
        self.Axis = []
        self.Title = Title
        self.nCols = 1
        self.nRows = None
        if UnitSize is not None: self.UnitSize = UnitSize


    def AddAxes(self, *Axis):
        for ax in Axis:
            self.Axis.append(ax)


    def GetMaxColsRows(self):
        RowMax, ColMax = 0,0
        for ax in self.Axis:
            RowMax = ax.Row if ax.Row > RowMax else RowMax
            ColMax = ax.Col if ax.Col > ColMax else ColMax

        return RowMax, ColMax


    def GenerateAxis(self):
        RowMax, ColMax = self.GetMaxColsRows()

        self.nRows = len(self.Axis)

        FigSize = [ self.UnitSize[0]*(ColMax+1), self.UnitSize[1]*(RowMax+1) ]

        self.Figure, Ax  = plt.subplots(ncols=ColMax+1, nrows=RowMax+1, figsize=FigSize)

        if not isinstance(Ax, np.ndarray): Ax = np.asarray([[Ax]])
        if Ax.ndim == 1: Ax = np.asarray([Ax])

        self.Figure.suptitle(self.Title)

        for ax in self.Axis:
            ax.MPLAxis = Ax[ax.Row, ax.Col]


    def Render(self):
        self.GenerateAxis()

        for ax in self.Axis:
            ax.Render()

        plt.tight_layout()


    def Show(self, Save=False, Directory="Figure.png", dpi=500):
        self.Render()
        if Save:
            print(f'Saving file into {os.path.dirname(os.path.realpath(__file__))}/{Directory}')
            plt.savefig(Directory, dpi=dpi, transparent=False)

        plt.show()
