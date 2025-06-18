import ast
import numpy as np

print("[INICIO] Analisando resultados.")
with open("results.txt", "r") as file:
    data = ast.literal_eval(file.read())

print(f"[RESULT] Dados: {data}")

zero_ratio = data.get('0', 0) / 1000
one_ratio = data.get('1', 0) / 1000

if not np.isclose(zero_ratio, 0.5, atol=0.05):
    raise ValueError("[ERRO] Fora da margem para |0⟩")
print("[ASSERT] Distribuição |0⟩ OK")

if not np.isclose(one_ratio, 0.5, atol=0.05):
    raise ValueError("[ERRO] Fora da margem para |1⟩")
print("[ASSERT] Distribuição |1⟩ OK")

print("[SUCESSO] Teste finalizado.")