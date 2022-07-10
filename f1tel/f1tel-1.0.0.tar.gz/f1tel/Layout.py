from matplotlib import pyplot as plt
from numpy import shape
import numpy as np

class Layout:
    def __init__(self, drivers, session, lap_number=None, x_axis="Time", y_axis=["Speed"]):
        self.drivers = drivers
        self.session = session
        self.lap_number = lap_number
        self.x_axis = x_axis
        self.y_axis = y_axis
        
        
    def plot(self):
        added_col = 0 if len(self.y_axis)%3 == 0 else 1
        fig, plots = plt.subplots(3, len(self.y_axis)//3 + added_col, sharex=True, sharey=False)
        if plots.ndim == 1:
            plots = plots.reshape(plots.shape[0], 1)
        x_metric = self.x_axis
        
        for i,y_metric in enumerate(self.y_axis):
            print("Plotting graph {}".format(y_metric))
            for driver in self.drivers:
                driver.plot(graph=plots[int(i%3)][int(i/3)], x_axis=x_metric, y_axis=y_metric, lap_number=self.lap_number)

            plots[int(i%3)][int(i/3)].set_ylabel(y_metric)
            plots[int(i%3)][int(i/3)].legend()
            
            if i%3 == 2:
                plots[int(i%3)][int(i/3)].set_xlabel(x_metric)

        plt.show()

class JSONLayout(Layout):

    def __init__(self, json_obj = None):
        if json_obj is None:
            raise ValueError("JSON object is None")
        self.json_obj = json_obj

        super(JSONLayout, self).__init__(self.json_obj["drivers"], self.json_obj["session"], self.json_obj["lap_number"])

    def plot(self):

        plots_windows = self.json_obj["plots_windows"]
        plt.style.use('_classic_test_patch')

        for plot_window in plots_windows:

            plots_layouts = plot_window["plots_layouts"]

            if len(plots_layouts) < 1:
                raise ValueError("There are no plots to plot")

            sharex = plots_layouts["sharex"] if "sharex" in plots_layouts else True
            sharey = plots_layouts["sharey"] if "sharey" in plots_layouts else False

            if len(plots_layouts) < 3:
                fig, plots = plt.subplots(len(plots_layouts), 1,sharex=sharex, sharey=sharey)
            else:
                added_col = 0 if len(plots_layouts)%3 == 0 else 1
                fig, plots = plt.subplots(3, len(plots_layouts)//3 + added_col,sharex=sharex, sharey=sharey)

            if "window_title" in plot_window:
                fig.canvas.set_window_title(str(plot_window["window_title"])+" (Lap {})".format(self.lap_number if self.lap_number is not None else "Fastest"))
            
            if "suptitle" in plot_window:
                fig.suptitle(str(plot_window["suptitle"])+" (Lap {})".format(self.lap_number if self.lap_number is not None else "Fastest"), fontsize=16)

            print("[-] Plotting window {}".format(fig.canvas.get_window_title()))

            x_metric = plot_window["x_axis"]

            if shape(plots) == ():
                plots = np.array([plots])

            if plots.ndim == 1:
                plots = plots.reshape(plots.shape[0], 1)

            for i, plot_layout in enumerate(plots_layouts):
                if plot_layout == {}:
                    continue
                y_metric = None
                plot_type = plot_layout["type"]
                if "y_axis" in plot_layout:
                    y_metric = plot_layout["y_axis"]
                if y_metric and y_metric != "":
                    for driver in self.drivers:
                        if plot_type == "line":
                            driver.plot(graph=plots[int(i%3)][int(i/3)], x_axis=x_metric, y_axis=y_metric, lap_number=self.lap_number)
                        elif plot_type == "map":
                            
                            preserve_sharex = plot_layout["preserve_sharex"] if "preserve_sharex" in plot_layout else False
                            preserve_sharey = plot_layout["preserve_sharey"] if "preserve_sharey" in plot_layout else False
                            
                            if len(self.drivers) == 1:
                                driver.plot_map(fig=fig, graph=plots[int(i%3)][int(i/3)], y_axis=y_metric, lap_number=self.lap_number, preserve_sharex=preserve_sharex, preserve_sharey=preserve_sharey)
                            else:
                                self.drivers[plot_layout["driver_index"]].plot_map(fig=fig, graph=plots[int(i%3)][int(i/3)], y_axis=y_metric, lap_number=self.lap_number, preserve_sharex=preserve_sharex, preserve_sharey=preserve_sharey)
                                break
                    if plot_type != "map":
                        plots[int(i%3)][int(i/3)].set_ylabel(y_metric)
                        plots[int(i%3)][int(i/3)].legend()
                if i%3 == 2:
                    plots[int(i%3)][int(i/3)].set_xlabel(x_metric)

        plt.show()