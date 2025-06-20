try:
    from qiskit import QuantumCircuit, transpile
    from qiskit_aer import AerSimulator
except ImportError as exc:
    raise ImportError(
        "Qiskit and qiskit-aer are required to run this test. Install with `pip install qiskit qiskit-aer`."
    ) from exc
import numpy as np

def test_hadamard_distribution():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    backend = AerSimulator()
    compiled = transpile(qc, backend)
    job = backend.run(compiled, shots=1000)
    counts = job.result().get_counts()

    zero_ratio = counts.get('0', 0) / 1000
    one_ratio = counts.get('1', 0) / 1000

    assert np.isclose(zero_ratio, 0.5, atol=0.05)
    assert np.isclose(one_ratio, 0.5, atol=0.05)

test_hadamard_distribution()
