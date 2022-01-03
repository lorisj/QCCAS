# QCCAS
QCCAS (Quantum computing computer algebra system) is a gate based quantum computing simulator written in python that uses density matrices, and can give outputs in exact form rather than just approximations. The simulator is inherently deterministic and simulates every possiblity unless otherwise instructed.


## State
The state of the system at a given time is represented by a random variable, Q. The random variable Q has a pmf, and Q takes values in the set of possible system states. 

A system state consists of the state of the given quantum and classical registers, where each quantum register is represented by a density matrix, and each classical register is represented by it's own random variable taking values in the complex numbers. Each quantum register represents a qbit, while each classical register represents a classical bit. In reality, the system will be in only one of these system states, while 

Generally when using the simulator, Q will have only one entry with probability = 1, and the system state is simply the density operator of the system with pmfs of it's measurement results. This changes when you have a unitary operation that depends on a measurement result. This case is explained under the measurement section.

## Measurement
Where QCCAS differs from most other simulators is its approach to measurement.

QCCAS uses a PVMs to measure the states. Recall a PVM is characterized by an observable A, and gives a quantum output and a classical output. A is diagonalized into a set of projectors for each eigenvalue a_i, and the quantum state collapses to it's normalized projection onto the eigensubspace for a_i, and the classical output is just a_i.
QCCAS instead collapses the quantum state to the expected quantum output for the observalble, and the classical output is a pmf of eigenvalues. This means the density operator after the measurment would encompass all of the possible states that could have occured after the measurement. 

## Unitary evolution
