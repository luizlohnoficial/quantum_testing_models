
import logging
import cirq
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

def test_hadamard_with_tolerance():
    logger.info("Preparing circuit")
    qubit = cirq.LineQubit(0)
    circuit = cirq.Circuit(cirq.H(qubit), cirq.measure(qubit, key='m'))
    logger.info("Running on Cirq Simulator")
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1000)
    counts = result.histogram(key='m')
    logger.info("Counts: %s", counts)

    zero_ratio = counts.get(0, 0) / 1000
    one_ratio = counts.get(1, 0) / 1000

    assert np.isclose(zero_ratio, 0.5, atol=0.05)
    assert np.isclose(one_ratio, 0.5, atol=0.05)

test_hadamard_with_tolerance()
