
import pennylane as qml
from pennylane import numpy as np

dev = qml.device("default.qubit", wires=1, shots=1000)

@qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0)
    return qml.sample(qml.PauliZ(0))

def test_hadamard_distribution():
    samples = circuit()
    zero_count = np.sum(samples == 1)
    one_count = np.sum(samples == -1)

    zero_ratio = zero_count / 1000
    one_ratio = one_count / 1000

    assert np.isclose(zero_ratio, 0.5, atol=0.05)
    assert np.isclose(one_ratio, 0.5, atol=0.05)

test_hadamard_distribution()
