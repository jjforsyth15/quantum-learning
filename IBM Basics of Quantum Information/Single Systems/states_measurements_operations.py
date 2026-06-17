from qiskit.quantum_info import Statevector, Operator
from numpy import sqrt
from IPython.display import display
from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit


# u = Statevector([1 / sqrt(2), 1 / sqrt(2)])
# v = Statevector([(1 + 2.0j) / 3, -2 / 3])
# w = Statevector([1 / 3, 2 / 3])

# display(u.draw("text"))
# display(u.draw("latex"))
# print(u.draw("latex_source"))

# display(u.is_valid())
# display(w.is_valid())

# display(v.draw("latex"))

# outcome, state = v.measure()
# print(f"Measured: {outcome}\nPost-measurement state:")
# display(state.draw("latex"))

# u = Statevector([1 / sqrt(2), 1 / sqrt(2)])
# v = Statevector([(1 + 2.0j) / 3, -2 / 3])
# w = Statevector([1 / 3, 2 / 3])

# statistics = v.sample_counts(10000)
# plot_histogram(statistics)


Y = Operator([[0, -1.0j], [1.0j, 0]])
H = Operator([[1 / sqrt(2), 1 / sqrt(2)], [1 / sqrt(2), -1 / sqrt(2)]])
S = Operator([[1, 0], [0, 1.0j]])
T = Operator([[1, 0], [0, (1 + 1.0j) / sqrt(2)]])

# display(T.draw("latex"))

v = Statevector([1, 0])

v = v.evolve(H)
v = v.evolve(T)
v = v.evolve(H)
v = v.evolve(S)
v = v.evolve(Y)

# display(v.draw("latex"))

circuit = QuantumCircuit(1)

circuit.h(0)
circuit.t(0)
circuit.h(0)
circuit.s(0)
circuit.y(0)

display(circuit.draw(output="mpl"))

display(Operator.from_circuit(circuit).draw("latex"))

ket0 = Statevector([1, 0])
v = ket0.evolve(circuit)
display(v.draw("latex"))

statistics = v.sample_counts(4000)
display(plot_histogram(statistics))