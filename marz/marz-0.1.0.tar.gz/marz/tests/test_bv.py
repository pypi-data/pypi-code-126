# This code is part of Marz.
#
# (C) Copyright IBM, Paul D. Nation, 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""Test basic circuits"""
from qiskit.circuit import Qubit, QuantumRegister, QuantumCircuit

import marz


def bv_circ(bitstring):
    """Create a Bernstein-Vazirani circuit from a given bitstring.

    Parameters:
        bitstring (str): A bitstring.

    Returns:
        QuantumCircuit: Output circuit.
    """
    qc = QuantumCircuit(2, len(bitstring))
    qc.x(1)
    qc.h(1)
    for idx, bit in enumerate(bitstring[::-1]):
        qc.h(0)
        if int(bit):
            qc.cx(0, 1)
        qc.h(0)
        qc.measure(0, idx)
        if idx != len(bitstring)-1:
            qc.reset(0)
            # reset control
            qc.reset(1)
            qc.x(1)
            qc.h(1)

    return qc


def test_dynamic_bv():
    """Simplify meas+reset pairs on controls of dynamic BV"""
    qc = bv_circ('11111')
    new_qc = marz.collapse_meas_reset_pairs(qc)
    # validate number of resets
    assert new_qc.count_ops()['reset'] == 4

    # validate that all resets are on Q1
    for op in new_qc.data:
        if op.operation.name == 'reset':
            assert op.qubits[0] == Qubit(QuantumRegister(2, 'q'), 1)
