# pylint: disable=redefined-outer-name
import pytest


@pytest.fixture
def future_mock():
    """Build a mock of an instance of a Future.

    Creates a mock object, that behaves similar to a Future instance, given an
    http status code, which the client desires the mock to emulate.

    The mock object is similar to the output of the MockFuturesSession.get
    method and has the single "result" 'method' that returns an object with the
    "status_code" property.

    Args:
        status_code (int): the http status code that the client desires the mock
            to return

    Returns:
        FutureMock: an instance of a Futere Mock
    """

    class FutureMock:
        def __init__(self, status_code: int):
            self.result = lambda: type('HttpResponseMock', (), {'status_code': status_code})

    return FutureMock


@pytest.fixture
def future_session_mock(future_mock):
    """Build a mock of an instance of a FutureSession.

    Create a mock object that partially emulates the behaviour of a
    MockFuturesSession instance and "exposes" a mocked 'get' method.
    """

    class FutureSessionMock:
        def __init__(self, url_2_code):
            self.url_2_code = url_2_code

        def get(self, url: str):
            return future_mock(self.url_2_code[url])

    return FutureSessionMock


@pytest.fixture
def future_session_mock_from_boolean(future_session_mock):
    """Mock the FuturesSession class.

    Get a mock of the FuturesSession class.

    Args:
        found (bool): whether to emulate the mock returning 200 or not as an
            http "status code"
    """

    def get_future_check_adapter(found: bool):
        class FixedUrl2CodeWith404NotFound:
            def __init__(self, found: bool):
                self.status_code = {True: 200, False: 404}[found]

            def __getitem__(self, item: str):
                return self.status_code

        url_2_code = FixedUrl2CodeWith404NotFound(found)

        class FutureSessionMockAdapter:
            def __init__(self):
                self.future_session_mock = future_session_mock(url_2_code)

            def get(self, url: str):
                return self.future_session_mock.get(url)

        return FutureSessionMockAdapter

    return get_future_check_adapter
