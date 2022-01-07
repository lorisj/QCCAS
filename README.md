# QCCAS
QCCAS (Quantum computing computer algebra system) is a gate based quantum computing simulator written in python that uses density matrices, and can give outputs in exact form rather than just approximations. The simulator is inherently deterministic and simulates every possibility unless otherwise instructed.


## State
The state of the system at a given time is represented by a random variable, **Q**. The random variable **Q** has a pmf, and **Q** takes values in the set of possible system states. 

Here, a system state consists of the state of the given quantum and classical registers, where each quantum register is represented by a density matrix, and each classical register is represented by its own random variable taking values in the complex numbers. 

Each quantum register represents a qbit, while each classical register represents a classical bit. In reality, the system will be in only one of these system states, but after a measurement result, it sometimes (see measurement section) makes sense to split up the simulation into mulitple branches, one for each measurement result, so that you can view what the algorithm does in every possible case. These multiple branches that arise from measurement results are what **Q** represents.

## Measurement
Where QCCAS differs from most other simulators is its approach to measurement.

QCCAS uses a PVM to measure the states. 

---
<details open>
<summary>PVM theory</summary>
<br>

> Recall that a PVM is characterized by an observable (hermitian operator) A, and gives a quantum output and a classical output.
> A is diagonalized into a set of projectors for each eigenvalue a_i, and the quantum state collapses to it's normalized projection onto the eigensubspace corresponding to a_i, and the classical output is just a_i.

  
</details>

---

In order to save time, QCCAS considers two cases with respect to simulating measurements. 
### Case 1: No split on measurement
This case covers when you have no unitary operations that depend on a specific measurement result.

Instead of picking one possible measurement outcome, QCCAS instead collapses the quantum state to the expected quantum output for the observable, and the classical output is a random variable representing each of eigenvalues. This means the density operator after the measurement would be the average of all possible states that could have occured after the measurement (think of this as the output density operator representing the state after measurement when you forgot which output value you got). 

So in case 1, **Q** will have only one entry with probability = 1, and the system state is simply the density operator of the system, (for the quantum registers) combined with pmfs of its measurement results (for the classical registers). 

We claim that the output of the entire algorithm will yield the same density operator as branching off into seperate cases for each measurement result and then combining them at the end.

See QCCAS/analysis/no_split.ipynb for more information and proofs of stated claims.
### Case 2: Split on measurement
This case covers when you have a unitary operator that depends on a measurement result, or if the user specified that they wanted to split
## Unitary evolution


