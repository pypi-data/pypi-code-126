import base64
import logging

from python_sdk_client.cropin_api import CropinAPI

"""Example on how to use CropAPI.  
"""
if __name__ == '__main__':
    logging.info(">>>>>>>>>>>> starting")

    # authenticate
    cropin_api = CropinAPI("tes", "12121212", "password")

    # plot details without any filter
    plot_response = cropin_api.get_plot_details()
    print("plot details without any filters is : {}".format(plot_response))

    # plot details with ids passed
    plot_response = cropin_api.get_plot_details(plot_ids='62305d0110197fce8a2d7b40, 62c550ba793e6d7ad6e122d1')
    print("plot details when plot ids are passed : {}".format(plot_response))

    # plot details with externalId passed
    plot_response = cropin_api.get_plot_details(external_ids='8104202')
    print("plot details when external Id is passed: {}".format(plot_response))

    plot_response = cropin_api.get_plot_details(plot_ids='62305d0110197fce8a2d7b40, 62c550ba793e6d7ad6e122d1',
                                                external_ids='8104202')
    print("plot details when ids and external Id is passed: {}".format(plot_response))

    satellite_response = cropin_api.get_satellite_details()
    print("satellite metrics with no filters :{}".format(satellite_response))

    satellite_response = cropin_api.get_satellite_details(boundary_id='61e8ec4c09e1880458676b35')
    print("satellite metrics when boundaryId is passed : {}".format(satellite_response))

    yield_response = cropin_api.get_yield_details()
    print("yield data with no filter passed :{}".format(yield_response))

    weather_response = cropin_api.get_weather_details()
    print("weather data with no filter passed :{}".format(weather_response))

    download_response = cropin_api.download_image(plot_id='62305d0110197fce8a2d7b40', image_name='HLM',
                                                  image_type='TIFF', date='2021-02-03')
    print("download_response is: {}".format(download_response))

    # code to convert the bytes to image
    imgdata = base64.b64decode(download_response['bytes'])
    filename = 'image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
