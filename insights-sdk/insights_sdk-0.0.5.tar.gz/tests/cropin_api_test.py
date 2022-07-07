import logging

from python_sdk_client.clients_enum import EnvType
from python_sdk_client.cropin_api import CropinAPI

"""Example on how to use CropAPI.  
"""
if __name__ == '__main__':
    logging.info(">>>>>>>>>>>> starting")

    cropin_api = CropinAPI("test", "12121212", "password", EnvType.QA)
    print(cropin_api)

    api_response = cropin_api.get_plot_details(plot_ids=None)
    print("empty plotid list response:{}".format(api_response))

    api_response = cropin_api.get_plot_details(plot_ids='62305d0110197fce8a2d7b40, 62c550ba793e6d7ad6e122d1')
    print("plot id response: {}".format(api_response))

    sattelite_response = cropin_api.get_satellite_details(plot_ids=None)
    print("empty list response: {}".format(sattelite_response))
    sattelite_response = cropin_api.get_satellite_details(plot_ids='62305d0110197fce8a2d7b40, 62c550ba793e6d7ad6e122d1')
    print("with plotid list response: {}".format(sattelite_response))

    yield_response = cropin_api.get_yield_details(plot_ids=None)
    print(yield_response)

    weather_api = cropin_api.get_weather_details(plot_ids=None)
    print(weather_api)

    download_api = cropin_api.download_image(plot_id='62305d0110197fce8a2d7b40', image_name='HLM', image_type='TIFF', date='2021-02-03')
    print(download_api)

