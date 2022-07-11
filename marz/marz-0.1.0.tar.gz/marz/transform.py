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

# The exact_mappings routine is more or less a direct port of the VF2Layout
# pass code from Qiskit with minor modifications to simplify and return a
# different format.  The Qiskit code is under the following license:

# Some code licensed under

# This code is part of Qiskit.
#
# (C) Copyright IBM 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
# pylint: disable=protected-access

"""Circuit transformation tools"""
from qiskit.circuit.library import XGate
from qiskit.circuit import CircuitInstruction
from qiskit.circuit.parametertable import ParameterReferences, ParameterTable


def collapse_meas_reset_pairs(circuits):
    """ Collapse measure + reset pairs on qubits down to a
    single measurement followed by a conditional X-gate.

    Parameters:
        circuits (QuantumCircuit or list): One or more QuantumCircuits.

    Returns:
        QuantumCircuit or list: QuantumCircuits with measure+reset pairs collapsed.
    """
    passed_list = True
    if not isinstance(circuits, list):
        circuits = [circuits]
        passed_list = False

    out_circuits = []
    for qc in circuits:
        meas_set = set()
        meas_last_qubits = {}
        new_data = []

        # This code block is a copy of some of the "copy" method in qiskit.circuit.quantumcircuit
        new_qc = qc.copy_empty_like(qc.name)
        operation_copies = {
            id(instruction.operation): instruction.operation.copy() for instruction in qc._data}
        new_qc._parameter_table = ParameterTable(
            {
                param: ParameterReferences(
                    (operation_copies[id(operation)], param_index)
                    for operation, param_index in qc._parameter_table[param]
                )
                for param in qc._parameter_table
            }
        )
        # --------------------------------------------------------------------------------------
        for op in qc._data:
            name = op.operation.name
            if name == 'reset':
                measured_qubit = op.qubits[0]
                if measured_qubit in meas_set:
                    cntrl_x = XGate()
                    cntrl_x.condition = (meas_last_qubits[measured_qubit][1][0], 1)
                    inst = CircuitInstruction(cntrl_x,
                                              qubits=meas_last_qubits[measured_qubit][0],
                                              clbits=())
                    new_data.append(inst)
                    meas_set.remove(measured_qubit)
                    continue

            elif name == 'measure':
                meas_last_qubits[op.qubits[0]] = (op.qubits, op.clbits)
                meas_set.add(op.qubits[0])

            else:
                # If any instruction that is not a measurement uses a qubit
                # then remove that qubit from the measurement set
                for qubit in op.qubits:
                    if qubit in meas_set:
                        meas_set.remove(qubit)

            # Append anything else
            new_data.append(op.copy())
        # Atta
        new_qc._data = new_data
        out_circuits.append(new_qc)
    if not passed_list:
        return out_circuits[0]
    return out_circuits
