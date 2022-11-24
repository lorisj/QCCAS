import sympy as sp

# Given a list of the new orientation of bits, calculate the new index version of index_in.
# Requires: list_in to be complete!
# Ex: L=[1,0]: this means essentially we switch the order of bits 0 and 1: (assume leftmost is MSB)
# 0 = 00 -> 0 = 00, 
# 1 = 01 -> 2 = 10,
# 2 = 10 -> 1 = 01,
# 3 = 11 -> 3 = 11

def change_tensor_order_helper(index_in, list_in):
    out = 0
    n = len(list_in)
    for old_power in range(len(list_in)):
        # if the ath bit of index_in is 1, i.e bool(index_in >> old_power & 1)
        #  add 2**(new_power)
        
        new_power = n-list_in.index(old_power)-1
        out = out + 2**(new_power)*(index_in >> old_power & 1)
    return out


# Given a list of the new orientation of qubits, calculate the change of basis matrix.
# Ex: L=[1,0]: this means essentially that we switch the order of qubits 0 and 1:
#   change_tensor_order_matrix(two_qubit_identitiy, L) should return:
#       1   0   0   0
#       0   0   1   0
#       0   1   0   0
#       0   0   0   1

def change_tensor_order_matrix(list_in):
    complete_permutation_list(list_in)
    out = []
    numStates = 2** NQ
    for i in range(numStates):
        tmp = [0] * numStates
        tmp[change_tensor_order_helper(i,list_in)]
        out.append(tmp)
    return sp.Matrix(out)


# Given a partial permutation list of the integers from 0,...NQ, add the missing numbers to the end of the list.
# Ex: Let NQ = 4, L = [0,3]:
# complete_permutation_list(L) should return [0,3,1,2]

def complete_permutation_list(list_in):
    for i in range(NQ):
        if(i not in list_in):
            list_in.append(i)
    return list_in



def complete_operator(self, op_in, list_in): #done
        # 1) U = U\otimes I^{\otimes |list^C|}
        size_of_list_comp = self.num_qubits - len(list_in)
        op_in = sp.TensorProduct(op_in, sp.eye(2**size_of_list_comp))
        #print(op_in)
        # 2) Calculate cob matrix M = cob(list)
        m = self.change_tensor_order_matrix(list_in)
        #print(m)
        # 3) output = MUM^\dagger
        return (m * op_in * sp.Dagger(m))
        