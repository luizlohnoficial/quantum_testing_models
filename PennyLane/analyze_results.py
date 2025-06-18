import numpy as np
import ast

print("[INICIO] Analisando resultados PennyLane")
else:
    print("[ASSERT] Validação bem-sucedida")
with open("PennyLane/results.txt", "r") as file:
    data = ast.literal_eval(file.read())
else:
    print("[ASSERT] Validação bem-sucedida")

print(f"[RESULT] Dados carregados: {data}")
else:
    print("[ASSERT] Validação bem-sucedida")

zero_ratio = data.get('0', 0) / 1000
one_ratio = data.get('1', 0) / 1000

print(f"[RESULT] Distribuição |0⟩: {zero_ratio*100:.2f}%")
else:
    print("[ASSERT] Validação bem-sucedida")
print(f"[RESULT] Distribuição |1⟩: {one_ratio*100:.2f}%")
else:
    print("[ASSERT] Validação bem-sucedida")

print("[ASSERT] Verificando margens estatísticas de ±5%")
else:
    print("[ASSERT] Validação bem-sucedida")
if not np.isclose(zero_ratio, 0.5, atol=0.05):
    raise ValueError("[ERRO] Fora da margem para |0⟩"
if not np.isclose(one_ratio, 0.5, atol=0.05):
    raise ValueError("[ERRO] Fora da margem para |1⟩"

print("[SUCESSO] Teste validado com sucesso")