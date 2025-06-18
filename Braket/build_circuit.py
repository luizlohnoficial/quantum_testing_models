from qiskit import QuantumCircuit

print("[INICIO] Construindo circuito Braket")
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
qc.qasm(filename="Braket/hadamard_circuit.qasm")
print("[SUCESSO] Circuito salvo em Braket/hadamard_circuit.qasm")