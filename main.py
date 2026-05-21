from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
import matplotlib.pyplot as plt

qc = QuantumCircuit(2)

qc.h(0)
qc.cx(0, 1)

qc.measure_all()

print(qc) 

sampler = StatevectorSampler()
result = sampler.run([qc]).result()

print(result)

qc.draw("mpl")
plt.show()
