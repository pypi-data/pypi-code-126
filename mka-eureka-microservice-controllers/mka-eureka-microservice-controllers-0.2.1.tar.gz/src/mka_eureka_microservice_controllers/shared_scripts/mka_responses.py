

import code
from django.http import JsonResponse

from django_numpy_json_encoder.numpy_encoder import NumpyJSONEncoder
from django_numpy_json_encoder.numpy_encoder import NumpyJSONEncoder
import decimal
import json
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)


class MultipleJsonEncoders():
    """
    Combine multiple JSON encoders
    """
    def __init__(self, *encoders):

        self.encoders = encoders
        print(self.encoders)
        self.args = ()
        self.kwargs = {}

    def default(self, obj):
        print("mmmmmmmmmmmmmmmmmmmmm")
        for encoder in self.encoders:
            print(encoder)
            try:
                return encoder(*self.args, **self.kwargs).default(obj)
            except TypeError:
                pass
        raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

    def __call__(self, *args, **kwargs):
        self.args = args
        print("mmsssmmmmmmmmmmmmmmmmmmm")
        self.kwargs = kwargs
        enc = json.JSONEncoder(*args, **kwargs)
        enc.default = self.default
        return enc

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
        print("callled")
        super().__init__(data=data,encoder = MultipleJsonEncoders(NumpyJSONEncoder,DecimalEncoder),safe=safe, **kwargs)

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

    