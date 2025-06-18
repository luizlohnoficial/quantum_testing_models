# Quantum Unit Testing - Segurança e Qualidade Corporativa

![Qiskit Tests](https://github.com/usuario/repositorio/actions/workflows/qiskit-tests.yml/badge.svg)
![Cirq Tests](https://github.com/usuario/repositorio/actions/workflows/cirq-tests.yml/badge.svg)
![PennyLane Tests](https://github.com/usuario/repositorio/actions/workflows/pennylane-tests.yml/badge.svg)
![Braket Tests](https://github.com/usuario/repositorio/actions/workflows/braket-tests.yml/badge.svg)
![Code Quality](https://github.com/usuario/repositorio/actions/workflows/code-quality.yml/badge.svg)

## Frameworks abordados
- Qiskit (IBM Quantum) — requer `qiskit-aer`
- Cirq (Google)
- PennyLane (Xanadu)
- Braket (AWS)

## Pipeline
- ✅ Pipelines separadas por framework
- ✅ Logging estruturado com notações: [INICIO], [ETAPA], [RESULT], [ASSERT], [SUCESSO], [ERRO], [FIM]
- ✅ Pipeline de qualidade com Black, Flake8 e Bandit
- ✅ Bandit validado: eval removido, asserts convertidos em exceptions seguras

## Autor
Desenvolvido por Luiz Lohn com suporte do ChatGPT OpenAI.