import os
import numpy as np
import pytest
import rlcluster 


@pytest.fixture(scope="module")
def testdata():
    rootdir = os.path.dirname(os.path.abspath('__file__'))
    tdata = os.path.join(rootdir, 'test/testdata.npy')
    t =  np.load(tdata)
    return t

def test_rlcluster(testdata):
    result = rlcluster.cluster(testdata)
    assert isinstance(result, rlcluster.RLClusterResult)
    assert len(result.centres) == 2
    assert result.centres[0] == 1702
    assert result.centres[1] == 2317
