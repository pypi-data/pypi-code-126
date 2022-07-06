import requests

def probe(url:str, range=(0, 200), headers=None) -> bytes:
    _headers = {
        **({} if headers is None else headers),
        "Range": f"bytes={'-'.join(str(r) for r in range)}"
    }
    
    resp = requests.get(url, headers=_headers)
    if resp.status_code >= 400:
        raise RuntimeError(f"probe error: {str(resp.status_code)}")
    no_byte_requested = range[1] - range[0] + 1
    no_byte_received = len(resp.content)
    assert no_byte_requested == no_byte_received, f'expect number of bytes received {no_byte_received} == requested {no_byte_requested}'
    return bytes(resp.content)


class PartialBuffer:
    def __init__(self, url: str, headers=None) -> None:
        self.url= url
        self.marker = 0
        self.headers = headers

    def read(self, size=-1):
        start_marker = self.marker
        current_marker = start_marker + size
        self.marker = current_marker
        return probe(self.url, (start_marker, current_marker - 1), self.headers)
        

