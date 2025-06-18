from qiskit import QuantumCircuit

print("[INICIO] Construindo circuito Cirq")
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
qc.qasm(filename="Cirq/hadamard_circuit.qasm")
print("[SUCESSO] Circuito salvo em Cirq/hadamard_circuit.qasm")