from icoscp.station import station
import pandas as pd
import folium


def test_get_id_list():
    stations = station.getIdList()
    assert isinstance(stations, pd.DataFrame)
    stations = station.getIdList(project='ALL', sort='name', outfmt='pandas')
    assert isinstance(stations, pd.DataFrame)
    stations = station.getIdList(project='ALL', sort='id', outfmt='pandas')
    assert isinstance(stations, pd.DataFrame)
    stations = station.getIdList(project='ICOS', outfmt='map', icon=None)
    assert isinstance(stations, folium.Map)
    stations = station.getIdList(project='NEON', outfmt='map', icon='flag')
    assert isinstance(stations, folium.Map)
    return
