
import logging
import pennylane as qml
from pennylane import numpy as np

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

dev = qml.device("default.qubit", wires=1, shots=1000)

@qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0)
    return qml.sample(qml.PauliZ(0))

def test_hadamard_distribution():
    logger.info("Running PennyLane circuit")
    logger.info("Circuit:\n%s", qml.draw(circuit)())
    samples = circuit()
    zero_count = np.sum(samples == 1)
    one_count = np.sum(samples == -1)

    logger.info("Zero count: %s, One count: %s", zero_count, one_count)

    zero_ratio = zero_count / 1000
    one_ratio = one_count / 1000

    assert np.isclose(zero_ratio, 0.5, atol=0.05), "probability of 0 close to 0.5"
    assert np.isclose(one_ratio, 0.5, atol=0.05), "probability of 1 close to 0.5"


if __name__ == "__main__":
    try:
        test_hadamard_distribution()
    except AssertionError as exc:
        logger.error("Test failed: %s", exc)
        raise
    else:
        logger.info("Test passed: distribution close to 50/50")
