from qiskit import QuantumCircuit
from qiskit_aer.primitives import SamplerV2

qc = QuantumCircuit(1, 1)   # Create a quantum circuit with 1 qubit and 1 classical bit

qc.h(0)   # Apply a Hadamard gate to the qubit

qc.h(0)   # Apply another Hadamard gate to the same qubit

qc.measure(0, 0)   # Measure the qubit and store the result in the classical bit

print(qc)   # Print the quantum circuit

sampler = SamplerV2()   # Create a sampler instance

job = sampler.run([qc], shots=1024)  # Run the sampler with the quantum circuit and specify the number of shots
result = job.result()   # Get the result of the sampler job

counts = result[0].data.c.get_counts()  # Get the counts of measurement outcomes

print(counts)   # Print the counts of measurement outcomes