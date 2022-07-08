

import code
from django.http import JsonResponse

from django_numpy_json_encoder.numpy_encoder import NumpyJSONEncoder

class EncodedJsonResponse_success(JsonResponse):
    """
    An HTTP response class that consumes data to be serialized to JSON and encode numpy types like float32,int32 to float64,int64 to be accepted in json .

    :param data: Data to be dumped into json. By default only ``dict`` objects
      are allowed to be passed due to a security flaw before EcmaScript 5. See
      the ``safe`` parameter for more information.
    :param safe: Controls if only ``dict`` objects may be serialized. Defaults
      to ``True``

    """
    def __init__(self,data,safe=True,**kwargs) -> None:
        super().__init__(data=data,encoder=NumpyJSONEncoder,safe=safe, **kwargs)

class EncodedJsonResponse_failure(JsonResponse):
    """
    An HTTP response class that consumes error response and if error have int32,float32 will be encoded in int64,float64

    :param data: Data to be dumped into json. By default only ``dict`` objects
      are allowed to be passed due to a security flaw before EcmaScript 5. See
      the ``safe`` parameter for more information.
    :param safe: Controls if only ``dict`` objects may be serialized. Defaults
      to ``True``

    """
    def __init__(self,error_message,safe=True,**kwargs) -> None:
        super().__init__(content={"message":error_message["message"]},status=error_message["code"],encoder=NumpyJSONEncoder, **kwargs)

    