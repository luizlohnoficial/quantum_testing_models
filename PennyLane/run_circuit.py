print("[INICIO] Executando circuito.")
# Execução simulada
print("[ETAPA] Rodando no backend simulado.")
print("[RESULT] Resultado: {'0': 500, '1': 500}")
with open("results.txt", "w") as f:
    f.write(str({'0': 500, '1': 500}))
print("[SUCESSO] Resultado salvo.")