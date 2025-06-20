try:
    from qiskit import QuantumCircuit, transpile
    from qiskit_aer import AerSimulator
except ImportError as exc:
    raise ImportError(
        "Qiskit and qiskit-aer are required to run this test. Install with `pip install qiskit qiskit-aer`."
    ) from exc
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

def test_hadamard_distribution():
    logger.info("Creating circuit")
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    logger.info("Circuit:\n%s", qc.draw(output='text'))

    logger.info("Running on AerSimulator")
    backend = AerSimulator()
    compiled = transpile(qc, backend)
    job = backend.run(compiled, shots=1000)
    counts = job.result().get_counts()

    logger.info("Counts: %s", counts)
    zero_ratio = counts.get('0', 0) / 1000
    one_ratio = counts.get('1', 0) / 1000

    assert np.isclose(zero_ratio, 0.5, atol=0.05)
    assert np.isclose(one_ratio, 0.5, atol=0.05)

test_hadamard_distribution()
