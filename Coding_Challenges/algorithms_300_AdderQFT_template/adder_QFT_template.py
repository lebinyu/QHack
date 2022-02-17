#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml


def qfunc_adder(m, wires):
    """Quantum function capable of adding m units to a basic state given as input.

    Args:
        - m (int): units to add.
        - wires (list(int)): list of wires in which the function will be executed on.
    """

    qml.QFT(wires=wires)
    
    # QHACK #
    # print(m)
    num=0
    for i in bin(m)[:1:-1]:
        # print(type(i))
        if i == '1':
            phase = 0
            for wire in range(num, len(wires)):
                # print(i)
                # print(len(wires))
                # print(num,wire)
                qml.RZ(2*np.pi/(2**(phase+1)),wires=wire)
                phase += 1    
        num+=1


    # qml.RZ(2*np.pi/(2**(1)),wires=0)
    # qml.RZ(2*np.pi/(2**(2)),wires=1)
    # qml.RZ(2*np.pi/(2**(3)),wires=2)
    # qml.RZ(2*np.pi/(2**(4)),wires=3)

    # qml.RZ(2*np.pi/(2**(1)),wires=2)
    # qml.RZ(2*np.pi/(2**(2)),wires=3)
    # QHACK #

    qml.QFT(wires=wires).inv()


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    # inputs = np.array([2,3])
    m = int(inputs[0])
    n_wires = int(inputs[1])
    wires = range(n_wires)

    dev = qml.device("default.qubit", wires=wires, shots=1)

    @qml.qnode(dev)
    def test_circuit():
        # Input:  |2^{N-1}>
        qml.PauliX(wires=0)

        qfunc_adder(m, wires)
        return qml.sample()

    output = test_circuit()
    print(*output, sep=",")
