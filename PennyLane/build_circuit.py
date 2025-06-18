from qiskit import QuantumCircuit

print("[INICIO] Construindo circuito PennyLane")
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
qc.qasm(filename="PennyLane/hadamard_circuit.qasm")
print("[SUCESSO] Circuito salvo em PennyLane/hadamard_circuit.qasm")