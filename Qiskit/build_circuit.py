from qiskit import QuantumCircuit

print("[INICIO] Construindo circuito Qiskit")
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
qc.qasm(filename="Qiskit/hadamard_circuit.qasm")
print("[SUCESSO] Circuito salvo em Qiskit/hadamard_circuit.qasm")