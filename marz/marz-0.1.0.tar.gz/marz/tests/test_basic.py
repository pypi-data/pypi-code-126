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
from qiskit import QuantumCircuit
from qiskit.circuit import Clbit, ClassicalRegister, QuantumRegister

import marz


def test_simple():
    """Test simple"""
    qc = QuantumCircuit(1, 1)
    qc.measure(0, 0)
    qc.reset(0)

    new_qc = marz.collapse_meas_reset_pairs(qc)

    ans_qc = QuantumCircuit(1, 1)
    ans_qc.measure(0, 0)
    ans_qc.x(0).c_if(Clbit(ClassicalRegister(1, 'c'), 0), 1)

    assert new_qc == ans_qc


def test_simple_null():
    """Test simple no change in circuit"""
    qc = QuantumCircuit(1, 1)
    qc.measure(0, 0)
    qc.x(0)
    qc.reset(0)

    new_qc = marz.collapse_meas_reset_pairs(qc)

    assert new_qc == qc


def test_simple_multi_reg():
    """Test simple, multiple registers"""
    cr1 = ClassicalRegister(1, 'c1')
    cr2 = ClassicalRegister(1, 'c2')
    qr = QuantumRegister(1, 'q')
    qc = QuantumCircuit(qr, cr1, cr2)
    qc.measure(0, 1)
    qc.reset(0)

    new_qc = marz.collapse_meas_reset_pairs(qc)

    ans_qc = QuantumCircuit(qr, cr1, cr2)
    ans_qc.measure(0, 1)
    ans_qc.x(0).c_if(Clbit(ClassicalRegister(1, 'c2'), 0), 1)

    assert new_qc == ans_qc


def test_simple_multi_reg_null():
    """Test simple, multiple registers, null change"""
    cr1 = ClassicalRegister(1, 'c1')
    cr2 = ClassicalRegister(1, 'c2')
    qr = QuantumRegister(2, 'q')
    qc = QuantumCircuit(qr, cr1, cr2)
    qc.measure(0, 1)
    qc.reset(1)  # reset not on same qubit as meas

    new_qc = marz.collapse_meas_reset_pairs(qc)

    assert new_qc == qc


def test_simple_multi_resets():
    """Only first reset is collapsed"""
    qc = QuantumCircuit(1, 2)
    qc.measure(0, 0)
    qc.reset(0)
    qc.reset(0)

    new_qc = marz.collapse_meas_reset_pairs(qc)

    ans_qc = QuantumCircuit(1, 2)
    ans_qc.measure(0, 0)
    ans_qc.x(0).c_if(Clbit(ClassicalRegister(2, 'c'), 0), 1)
    ans_qc.reset(0)

    assert new_qc == ans_qc


def test_simple_multi_resets2():
    """Reset BEFORE measurement not collapsed"""
    qc = QuantumCircuit(2, 2)
    qc.measure(0, 0)
    qc.reset(0)
    qc.reset(1)
    qc.measure(1, 1)

    new_qc = marz.collapse_meas_reset_pairs(qc)

    ans_qc = QuantumCircuit(2, 2)
    ans_qc.measure(0, 0)
    ans_qc.x(0).c_if(Clbit(ClassicalRegister(2, 'c'), 0), 1)
    ans_qc.reset(1)
    ans_qc.measure(1, 1)

    assert new_qc == ans_qc


def test_barriers_work():
    """Test that barriers block consolidation"""
    qc = QuantumCircuit(1, 1)
    qc.measure(0, 0)
    qc.barrier(0)
    qc.reset(0)

    new_qc = marz.collapse_meas_reset_pairs(qc)
    assert new_qc == qc
