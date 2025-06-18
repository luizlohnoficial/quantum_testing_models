# Quantum Unit Testing - Structured with Code Quality

![Quantum Tests](https://github.com/usuario/repositorio/actions/workflows/quantum-tests.yml/badge.svg)
![Code Quality](https://github.com/usuario/repositorio/actions/workflows/code-quality.yml/badge.svg)

Este repositório contém exemplos de testes unitários aplicados ao desenvolvimento de algoritmos para computação quântica.

## Frameworks abordados
- Qiskit (IBM Quantum) — requer `qiskit-aer`
- Cirq (Google)
- PennyLane (Xanadu)
- Braket (AWS)

## Pipeline
- ✅ Dividido em etapas: Construção, Execução e Análise
- ✅ Logging padronizado com notações [INICIO], [ETAPA], [RESULT], [ASSERT], [SUCESSO], [ERRO], [FIM]
- ✅ Workflows no GitHub Actions por etapa e pipeline de qualidade
- ✅ Formatação automática (Black), Lint (flake8) e Análise de Segurança (Bandit)

## Observações
- O Qiskit, desde a versão 0.43, separa o Aer (simulador) no pacote `qiskit-aer`.

## Autor
Desenvolvido por Luiz Lohn com suporte do ChatGPT OpenAI.