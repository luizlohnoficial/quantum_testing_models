from qiskit import QuantumCircuit, execute
from qiskit_aer import Aer

print("[INICIO] Executando circuito Cirq")
qc = QuantumCircuit.from_qasm_file("Cirq/hadamard_circuit.qasm")
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1000)
result = job.result()
counts = result.get_counts()
with open("Cirq/results.txt", "w") as file:
    file.write(str(counts))
print(f"[RESULT] Contagens: {counts}")
print("[SUCESSO] Resultados salvos em Cirq/results.txt")