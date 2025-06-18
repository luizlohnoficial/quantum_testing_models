
from braket.circuits import Circuit
from braket.devices import LocalSimulator

def test_double_hadamard_returns_initial_state():
    circuit = Circuit().h(0).h(0).measure(0)
    simulator = LocalSimulator()

    result = simulator.run(circuit, shots=100).result()
    counts = result.measurement_counts

    assert counts.get('0', 0) == 100

test_double_hadamard_returns_initial_state()
