import os
import sys
import numpy as np
import pytest
from pytest_lazyfixture import lazy_fixture as lf

thisfile = os.path.abspath(__file__)
modulepath = os.path.dirname(os.path.dirname(thisfile))

sys.path.insert(0, modulepath)

import tensorcircuit as tc

try:
    import torch
except ImportError:
    pytest.skip("torch is not installed")


@pytest.mark.parametrize("backend", [lf("tfb"), lf("jaxb"), lf("torchb")])
def test_quantumnet(backend):

    n = 6
    nlayers = 2

    def qpred(x, weights):
        c = tc.Circuit(n)
        for i in range(n):
            c.rx(i, theta=x[i])
        for j in range(nlayers):
            for i in range(n - 1):
                c.cnot(i, i + 1)
            for i in range(n):
                c.rx(i, theta=weights[2 * j, i])
                c.ry(i, theta=weights[2 * j + 1, i])
        ypred = tc.backend.stack([c.expectation_ps(x=[i]) for i in range(n)])
        return tc.backend.real(ypred)

    if tc.backend.name == "pytorch":
        use_interface = False
    else:
        use_interface = True

    ql = tc.TorchLayer(
        qpred, weights_shape=[2 * nlayers, n], use_interface=use_interface
    )

    yp = ql(torch.ones([3, n]))
    print(yp)

    np.testing.assert_allclose(yp.shape, np.array([3, n]))
