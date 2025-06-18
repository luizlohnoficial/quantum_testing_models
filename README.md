# Quantum Unit Testing - Verbose Pipeline com Governança

## Frameworks Abordados
- Qiskit (IBM Quantum)
- Cirq (Google)
- PennyLane (Xanadu)
- Braket (AWS)

## Pipeline
- ✅ Pipelines verbosas por framework.
- ✅ Logging estruturado com notações: [INICIO], [ETAPA], [RESULT], [ASSERT], [SUCESSO], [ERRO], [FIM].
- ✅ Segurança aplicada: eval removido, asserts convertidos em exceções explícitas.

## Execução
1. Instale dependências:
   pip install -r requirements.txt
2. Execute localmente os scripts na ordem:
   - build_circuit.py
   - run_circuit.py
   - analyze_results.py

## Estrutura dos Scripts
- build_circuit.py: Cria e salva o circuito.
- run_circuit.py: Executa o circuito no simulador e salva os resultados.
- analyze_results.py: Analisa os resultados e valida as distribuições.

Desenvolvido por Luiz Lohn com suporte do ChatGPT OpenAI.