import pytest
import socket
from .. import dirutils


def test_prepare_outdirs():
    filename = "/users/opid22/inhouse/id222207/id22/20220701/GC_natrite_test4_45mdey/GC_natrite_test4_45mdey_0001/GC_natrite_test4_45mdey_0001.h5"
    include_proposal_outdir = False
    outdirs = dict()

    result = dirutils.prepare_outdirs(outdirs, filename, include_proposal_outdir)
    assert result == dict()

    include_proposal_outdir = True
    result = dirutils.prepare_outdirs(outdirs, filename, include_proposal_outdir)
    expected = {
        "primary": (
            None,
            "/users/opid22/inhouse/id222207/id22/20220701/ewoks_processed",
        )
    }
    assert result == expected

    outdirs = {
        "primary": "opid22@diffract22new:/users/opid22/data1/",
        "secondary": "opid22@diffract22new:/users/opid22/data1/",
    }
    with pytest.raises(ValueError):
        dirutils.prepare_outdirs(outdirs, filename, include_proposal_outdir)

    outdirs = {
        "primary": f"opid22@{socket.gethostname()}:/users/opid22/data1/",
        "secondary": "opid22@diffract22new:/users/opid22/data1/",
    }
    result = dirutils.prepare_outdirs(outdirs, filename, include_proposal_outdir)
    expected = {
        "primary": (None, "/users/opid22/data1/"),
        "secondary": ("opid22@diffract22new", "/users/opid22/data1/"),
        "proposal": (
            None,
            "/users/opid22/inhouse/id222207/id22/20220701/ewoks_processed",
        ),
    }
    assert result == expected
