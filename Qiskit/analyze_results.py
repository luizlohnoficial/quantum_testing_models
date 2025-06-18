import numpy as np

print("[INICIO] Analisando resultados Qiskit")
with open("Qiskit/results.txt", "r") as file:
    data = eval(file.read())

print(f"[RESULT] Dados carregados: {data}")

zero_ratio = data.get('0', 0) / 1000
one_ratio = data.get('1', 0) / 1000

print(f"[RESULT] Distribuição |0⟩: {zero_ratio*100:.2f}%")
print(f"[RESULT] Distribuição |1⟩: {one_ratio*100:.2f}%")

print("[ASSERT] Verificando margens estatísticas de ±5%")
assert np.isclose(zero_ratio, 0.5, atol=0.05), "[ERRO] Fora da margem para |0⟩"
assert np.isclose(one_ratio, 0.5, atol=0.05), "[ERRO] Fora da margem para |1⟩"

print("[SUCESSO] Teste validado com sucesso")