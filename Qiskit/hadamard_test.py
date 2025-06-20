try:
    from qiskit import QuantumCircuit, transpile
    from qiskit_aer import AerSimulator
except ImportError as exc:
    raise ImportError(
        "Qiskit and qiskit-aer are required to run this test. Install with `pip install qiskit qiskit-aer`."
    ) from exc
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

# Constantes para fácil manutenção
SHOTS = 1000
TOLERANCE = 0.05
EXPECTED_PROBABILITY = 0.5

def test_hadamard_distribution():
    logger.info("Criando circuito")
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    logger.info("Circuito:\n%s", qc.draw(output='text'))

    logger.info("Rodando no AerSimulator")
    backend = AerSimulator()
    compiled = transpile(qc, backend)
    job = backend.run(compiled, shots=1000)
    counts = job.result().get_counts()

    logger.info("Contagem: %s", counts)
    zero_ratio = counts.get('0', 0) / 1000
    one_ratio = counts.get('1', 0) / 1000

    assert np.isclose(zero_ratio, 0.5, atol=0.05), "probabilidade de 0 próximo a 0.5"
    assert np.isclose(one_ratio, 0.5, atol=0.05), "probabilidade de 1 próximo a 0.5"

    assert abs(zero_ratio - EXPECTED_PROBABILITY) <= TOLERANCE, (f"Probabilidade de |0› ({zero_ratio:.3f}) fora da tolerância (±{TOLERANCE})" )
    assert abs(one_ratio - EXPECTED_PROBABILITY) <= TOLERANCE, ( f"Probabilidade de |1› ({one_ratio:.3f}) fora da tolerância (±{TOLERANCE})" )


if __name__ == "__main__":
    try:
        test_hadamard_distribution()
    except AssertionError as exc:
        logger.error("Testes falharam: %s", exc)
        raise
    else:
        logger.info("Testes passaram: distribuição próxima a 50/50")
