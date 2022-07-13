from folium import plugins
import folium
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from tasks import *

def get_map(df):
    """
    Get the dataframe with timestamps and return a map with toggle timestamps
    :param df: travel time dataframe
    :return: map: folium map
    """
    # change data path here
    data = read_data(df)

    lat = list(data["LATITUDE"])
    long = list(data["LONGITUDE"])
    speed = list(data["Speed (MPH)"])
    date = list(data['LOCAL TIME'])
    date2 = list(data['LOCAL DATE'])

    feature = folium.FeatureGroup(name="Travel Time Map")

    # change map center with the avg of the data
    map = folium.Map([data.Lat.mean(), data.Long.mean()], zoom_start=12)

    # add a marker for each point
    for lt, ln, s, t, dt in zip(lat, long, speed, date, date2):
        feature.add_child(folium.CircleMarker(location=[lt, ln], radius=4, tooltip=folium.Tooltip(text=dt + ' ' + t),
                                              fill_color=coloring(s), color=coloring(s), fill_opacity=0.7))

    # call for legend
    map = create_legend(map, 'Speed - MPH',
                        colors=['red', 'orange', 'yellow', '#98ebb0'],
                        labels=['0-20', '21-40', '41-55', '55+'])
    # display data points on the map and export
    map.add_child(feature)
    folium.LayerControl().add_to(map)
    return map