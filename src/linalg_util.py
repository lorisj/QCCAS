import sympy as sp
from sympy.physics.quantum.matrixutils import matrix_tensor_product


# Given a list of the new orientation of bits (starting from the back), calculate the new index version of index_in.
# Requires: list_in to be complete!
# Ex: L=[0,1]: this means essentially we switch the order of bits 0 and 1: (assume leftmost is MSB)
# 0 = 00 -> 0 = 00, 
# 1 = 01 -> 2 = 10,
# 2 = 10 -> 1 = 01,
# 3 = 11 -> 3 = 11
def change_tensor_order_helper(index_in : int, list_in : list[int]) -> list[int]:
    out = 0
    power_so_far = 0 # for every input power
    for system_index in range(len(list_in)):
        
        
        # if the ath bit of index_in is 1, i.e bool(index_in >> old_power & 1)
        #  add 2**(new_power)
        new_power = list_in.index(power_so_far)
        cond_add = (index_in >> power_so_far & 1) # condition add on if the power_so_far-th bit of index_in is a 1
        out = out + (2**(new_power))*(cond_add)
        power_so_far = power_so_far + 1

        
            
    return out


# Given a list of the new orientation of qubits, calculate the change of basis matrix.
#  Requires the list_in to be complete!
    # Ex: list_in=[1,0]: this means essentially that we switch the order of qubits 0 and 1:
    #   change_tensor_order_matrix(two_qubit_identitiy, L) should return:
    #       1   0   0   0
    #       0   0   1   0
    #       0   1   0   0
    #       0   0   0   1
def change_tensor_order_matrix(list_in : list[int]) -> sp.Matrix: #done
    out = []    
    num_states = 2** len(list_in)
    for i in range(num_states):
        tmp = [0] * num_states
        new_index = change_tensor_order_helper(i,list_in) 
        tmp[new_index] = 1
        out.append(tmp)
    return sp.Matrix(out).T



# returns the ith std unit column vector in R**dim_in
def std_unit_vector(dim_in : int, i : int) -> sp.Matrix():
    list = [0]*dim_in
    list[i] = 1
    return sp.Matrix(list).T
