
import cirq
import numpy as np

def test_hadamard_with_tolerance():
    qubit = cirq.LineQubit(0)
    circuit = cirq.Circuit(cirq.H(qubit), cirq.measure(qubit, key='m'))
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1000)
    counts = result.histogram(key='m')

    zero_ratio = counts.get(0, 0) / 1000
    one_ratio = counts.get(1, 0) / 1000

    assert np.isclose(zero_ratio, 0.5, atol=0.05)
    assert np.isclose(one_ratio, 0.5, atol=0.05)

test_hadamard_with_tolerance()
