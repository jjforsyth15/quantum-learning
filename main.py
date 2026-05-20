from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(1)

qc.h(0)

qc.measure_all()

sampler = StatevectorSampler()
result = sampler.run([qc]).result()

print(qc)
print(result)

qc.draw("mpl")