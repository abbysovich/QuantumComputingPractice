from qiskit import *
from qiskit.tools.visualization import plot_histogram

qr = QuantumRegister(2)
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)
print(circuit.draw())

circuit.h(qr[0])
print(circuit.draw())
circuit.cx(qr[0], qr[1])
print(circuit.draw())
circuit.measure(qr, cr)
print(circuit.draw())

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator).result()
plot_histogram(result.get_counts(circuit))

IBMQ.load_account()
provider = IBMQ.get_provider('ibm-q')
qcomp = provider.get_backend('ibmq_16_melbourne')
job = execute(circuit, backend=qcomp)
from qiskit.tools.monitor import job_monitor
job_monitor(job)
result = job.result()
plot_histogram(result.get_counts(circuit)).show()