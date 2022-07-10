from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.collections import LineCollection
from matplotlib.figure import Figure
import numpy as np

import fastf1


class Driver:

    def __init__(self, name: str=None, session: fastf1.core.Session=None):
        self.name = name
        self.session = session
        try:
            
            self.driver_data = self.session.laps.pick_driver(self.name)
            self.name = self.driver_data.iloc[0]["Driver"]
            self.driver_color = fastf1.plotting.DRIVER_COLORS[fastf1.plotting.DRIVER_TRANSLATE[self.name]]
            self.fastest_telemetry = self.get_fastest_lap_data()
        except KeyError as e:
            raise KeyError("{} is not a valid driver".format(self.name))
    

    def get_session(self):
        return self.session

    def get_data(self, lap_number: int=None):
        lap_data = []
        if lap_number is None:
            lap_data = self.fastest_telemetry
        else:
            lap_data = self.get_lap_data(lap_number)
        return lap_data

    def get_fastest_lap_data(self):
        return self.driver_data.pick_fastest().get_telemetry()

    def get_all_laps_data(self):
        return self.driver_data.get_telemetry()

    def get_lap_data(self, lap_number: int):

        data = self.driver_data.loc[self.driver_data['LapNumber'] == lap_number].get_telemetry()
        
        return data

    def _plot(self, graph, x, y):
        return graph.plot(x, y, label=self.name, color=self.driver_color)

    def plot_speed(self, graph, lap_number: int=None):
        lap_data = self.get_data(lap_number)
        return self._plot(graph, lap_data['Time'], lap_data['Speed'])

    def plot_drs(self, graph, lap_number: int=None):
        lap_data = self.get_data(lap_number)
        return self._plot(graph, lap_data['Time'], lap_data['DRS'])

    def plot_throttle(self, graph, lap_number: int=None):
        lap_data = self.get_data(lap_number)
        return self._plot(graph, lap_data['Time'], lap_data['Throttle'])

    def plot(self, graph, x_axis: str="Time", y_axis: str="Speed", lap_number: int=None):
        lap_data = self.get_data(lap_number)
        try:
            return self._plot(graph, lap_data[x_axis], lap_data[y_axis])
        except KeyError:
            raise KeyError("{} is not a valid metric".format(y_axis))

    def plot_map(self, fig: Figure, graph: Axes,y_axis: str="Gear", lap_number: int=None, preserve_sharex=False, preserve_sharey=False):
        lap_data = self.get_data(lap_number)
        
        x_values = lap_data['X']
        y_values = lap_data['Y']
        points = np.array([x_values, y_values]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        values = lap_data[y_axis].to_numpy().astype(float)
        cmap = cm.get_cmap("Paired")
        lc_comp = LineCollection(segments, cmap=cmap, norm=plt.Normalize(0, cmap.N+1))
        lc_comp.set_array(values)
        lc_comp.set_linewidth(4)
        gcm = graph.add_collection(lc_comp)
        if not preserve_sharex:
            graph.get_shared_x_axes().remove(graph.axes)
        if not preserve_sharey:
            graph.get_shared_y_axes().remove(graph.axes)
        graph.axes.set_xlim(min(x_values)-150, max(x_values)+150)
        graph.axes.set_ylim(min(y_values)-150, max(y_values)+150)
        graph.axes.set_xticks([])
        graph.axes.set_yticks([])
        graph.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)
        graph.grid(False)
        cbar = fig.colorbar(mappable=lc_comp, ax=graph, boundaries=np.arange(1, 10))
        cbar.set_ticks(np.arange(1.5, 9.5))
        cbar.set_ticklabels(np.arange(1, 9))
        return graph