#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml

graph = {
    0: [1],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1],
    4: [1, 5, 7, 8],
    5: [4, 6],
    6: [5, 7],
    7: [4, 6],
    8: [4],
}


def n_swaps(cnot):
    """Count the minimum number of swaps needed to create the equivalent CNOT.

    Args:
        - cnot (qml.Operation): A CNOT gate that needs to be implemented on the hardware
        You can find out the wires on which an operator works by asking for the 'wires' attribute: 'cnot.wires'

    Returns:
        - (int): minimum number of swaps
    """
    # QHACK #
    qubit_length = np.array([[0,1,2,2,2,3,4,3,3],[1,0,1,1,1,2,3,2,2],[2,1,0,2,2,3,4,3,3],[2,1,2,0,2,3,4,3,3],[2,1,2,2,0,1,2,1,1],[3,2,3,3,1,0,1,2,2],[4,3,4,4,2,1,0,1,3],[3,2,3,3,1,2,1,0,2],[3,2,3,3,1,2,3,2,0]])
    qubit = cnot.wires
    # print(qubit)
    length = qubit_length[qubit[0],qubit[1]]
    # print(length)
    if length == 0:
        return 0
    else:
        return 2*(length-1)
    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    # inputs = [2,8]
    output = n_swaps(qml.CNOT(wires=[int(i) for i in inputs]))
    print(f"{output}")
