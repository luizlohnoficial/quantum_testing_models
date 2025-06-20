
import logging
from braket.circuits import Circuit
from braket.devices import LocalSimulator

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

def test_double_hadamard_returns_initial_state():
    logger.info("Building circuit")
    circuit = Circuit().h(0).h(0).measure(0)
    logger.info("Circuit:\n%s", circuit)
    logger.info("Running on LocalSimulator")
    simulator = LocalSimulator()

    result = simulator.run(circuit, shots=100).result()
    counts = result.measurement_counts
    logger.info("Counts: %s", counts)
    
    logger.info(assert counts.get('0', 0) == 100, "double hadamard should return |0>")

