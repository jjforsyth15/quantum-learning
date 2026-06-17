from qiskit import __version__
import numpy as np
from qiskit.visualization import array_to_latex
from IPython.display import display
print(__version__)   # Print the version of Qiskit being used

ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

print(ket0 / 2 + ket1 / 2)  

M1 = np.array([[1, 1], [0, 0]])
M2 = np.array([[1, 0], [0, 1]])
M = M1 / 2 + M2 / 2
print(M)

print(M1 @ ket1)
print(M1 @ M2)
print(M @ M)


display(array_to_latex(M1 @ ket1))
display(array_to_latex(M1 @ M2))
display(array_to_latex(M @ M))
