# BY CONVENTION:
# Random var = [ [value1, p1], [value2, p2], ...  ] (Value first, then probability)
# 


import sympy as sp
import linalg_util as linalg
#from sympy import Matrix
#from sympy.physics.quantum import TensorProduct
init_rand_vec = (0,1)

def unitary_evolution(density_operator, unitary_operator):
    return unitary_operator * density_operator * unitary_operator.H


    


# performs a PVM measurement on each of the density_operators in the list, and outputs a vector in the form [quantum_output_rv, classical_output_rv_rv, probability]
# arguments: 
#           quantum_input_rv: rv of density operators to perform measurements.
#           observable: Either a list of orthoganal projectors or a Hermitian operator (which can be decomposed into orthoganal projectors)
#           observed value: Eigenvalue corresponding to observed value. If not provided, then no measurement is observed then
#                               state collapses to the average quantum result
#
#
# returns: L = [quantum_output, classical_output, probability]
#           quantum_output: pmf of density operators correpsonding to the quantum state of each input density operator post measurement
#           classical_output: rv of rv of eigenvalues corresponding to which classical state has been measured for each density operator.
#                               First pmf comes from the quantum_input_pmf, second comes from the actual measurement.
#                               i.e classical_output_rv_rv[i] is a rv corresponding to the different measurement results of quantum_input_rv[i][0]
#           probability: probability of getting this measurement result. If no observed_value is given then this is just 1.
#  

def measurement(quantum_input_rv, observable, observed_value = "not"):
    
    #Observable processing:------------------------------------------------------------------------
    
    if(observable.type() == sp.Matrix):
        diag = linalg.spectral_decomp(observable)
    else:
        diag = observable
    #diag = [(a_i, |i>)]_i  where for all i:  a_i is a complex number, |i> is a vector in C^n
    
    projector_dict = {}

    #find projectors for each subspace
    for pair in diag:
        projector_dict[pair[0]] = projector_dict[pair[0]] + pair[1] * pair[1].H

    # End observable processing -------------------------------------------------------------------


    for rand_var_iterator in quantum_input_rv:
        #value first, prob second by convention
        current_density_operator = rand_var_iterator[0] 
        current_probability = rand_var_iterator[1] 
        
        
        classical_output = []
        #if measurement value is observed, density operator collapses to one option
        if(observed_value != "not"):
            cur_projector = projector_dict[observed_value]
            probability = sp.trace(cur_projector*current_density_operator)
            quantum_output = sp.Rational(1,probability) * (cur_projector * current_density_operator * cur_projector.H)
            classical_output.append([[observed_value, 1]])

        #if measurement value is not observed, density operator collapsed to average of measurement result
        else:
            probability = 1
            for eigenvalue in projector_dict:
                cur_projector = projector_dict[eigenvalue]
                quantum_output = quantum_output + (projector_dict * current_density_operator * projector_dict.H)
                classical_output.append([eigenvalue, sp.trace(cur_projector * current_density_operator)]) 
    return [quantum_output, classical_output, probability]


def init_quant_reg(quant_reg, num_quant_reg):
    #Sympy uses Matrix([row1, row2, ...]) so |0> = [[1],[0]]
    init_qubit = sp.Matrix([[1], [0]])

    # |0> \otimes |0> \otimes ... \otimes |0>
    for i in range(num_quant_reg):
        quant_reg[0] = sp.TensorProduct(quant_reg[0], init_qbit) 

def proc_op_list(op_list):
    for e in op_list:
        

        # sample quantum operation: 
        # Unitary evolution: (Ti,a )
        cur_quantum_op = op_list[0]
        



        cur_classical_op = op_list[1]





    #quant_reg[i] = density operator at step i
    quant_reg = []
    init_quant_reg(quant_reg, num_quant_reg)
 

    #class_reg[i] = r.v corresponding to classical reg i
    class_reg = [[init_rand_vec] * num_class_reg] 

   
    proc_op_list(op_list)
    for e in op_list:
        


main()
