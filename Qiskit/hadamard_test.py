
from qiskit import QuantumCircuit, Aer, execute
import numpy as np

def test_hadamard_distribution():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1000)
    counts = job.result().get_counts()

    zero_ratio = counts.get('0', 0) / 1000
    one_ratio = counts.get('1', 0) / 1000

    assert np.isclose(zero_ratio, 0.5, atol=0.05)
    assert np.isclose(one_ratio, 0.5, atol=0.05)

test_hadamard_distribution()
