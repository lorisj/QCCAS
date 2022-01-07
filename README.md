# QCCAS
QCCAS (Quantum computing computer algebra system) is a gate based quantum circuit simulator written in python that uses density matrices, and can give outputs in exact form rather than just approximations. The simulator is inherently deterministic and simulates every possibility unless otherwise instructed.

The goal of this project is to create a simulator that can give a complete description of a quantum circuit, and to do so as efficiently as possible while being as easy to use as possible.


# Table of Contents
**Basic concepts:** (Theory side)
1. [State](#state-loc)
2. [Measurement](#measurement-loc)
3. [Quantum evolution](#evolution-loc)


**Code/implementation:** (Programming side)
1. [Third Example](#third-example-loc)
2. [Fourth Example](#fourth-examplehttpwwwfourthexamplecom)


<a name="state-loc"/>


# Basic concepts
## State
The state of the system at a given time is represented by a random variable, **Q**. The random variable **Q** has a pmf, and **Q** takes values in the set of possible system states. 

Here, a system state is defined as the state of the given quantum and classical registers, where each quantum register is represented by a density matrix, and each classical register is represented by its own random variable taking values in the complex numbers. 

Each quantum register represents a qbit, while each classical register represents a classical bit. In reality, the system will be in only one of these system states, but after a measurement result, it sometimes (see measurement section) makes sense to split up the simulation into mulitple branches, one for each measurement result, so that you can view what the algorithm does in every possible case. These multiple branches that arise from measurement results are what **Q** represents.

<a name="measurement-loc"/>

## Measurement
Where QCCAS differs from most other simulators is its approach to measurement.

QCCAS uses a PVM to measure the states. 


<details>
<summary>PVM theory recap</summary>
<br>

> Recall that a PVM is characterized by an observable (hermitian operator) A, and gives a quantum output and a classical output.
> A is diagonalized into a set of projectors for each eigenvalue $a_i$, and the quantum state collapses to it's normalized projection onto the eigensubspace corresponding to $a_i$, and the classical output is just $a_i$.

  
</details>



In order to save time, QCCAS considers two cases with respect to simulating a given measurement. 
### Case 1: No split on measurement
This case occurs when you have no unitary operations that depend on a specific measurement result.

Instead of picking one possible measurement outcome, QCCAS instead collapses the quantum state to the expected quantum output for the observable, and the classical output is a random variable representing each of eigenvalues. This means the density operator after the measurement would be the average of all possible states that could have occured after the measurement (think of this as the output density operator representing the state after measurement when you forgot which output value you got). 

So in case 1, **Q** will have only one entry with probability = 1, and the system state is simply the density operator of the system (for the quantum registers), combined with pmfs of its measurement results (for the classical registers). 

We claim that if there are no unitary operations that depend on a specific measurement result, averaging out the measurement will yield the same density operator as branching off into seperate cases for each measurement result and then combining them at the end.

See QCCAS/analysis/measure_no_split.ipynb for more information and proofs of stated claims.
### Case 2: Split on measurement
This case occurs when you have a unitary operator that depends on a measurement result, or if the user specified that they wanted to split after a certain measurement. 

In this case, we claim the solution of collapsing to the average quantum state would not work, and simulating the rest of the algorithm after the measurement for each outcome is necissary, and so this is what QCCAS does.
If you have multiple of these measurements, then each branch is then split again for each measurement.

Each sequence of measurement outcomes is exactly what Q represents. At the end of the algorithm, Q then yields a complete description of the output of a quantum algorithm.

See QCCAS/analysis/measure_split.ipynb for more information and proofs of stated claims.

<a name="evolution-loc"/>

## Quantum evolution


# Code/implementation

<a name="third-example-loc"/>

## Third-example
