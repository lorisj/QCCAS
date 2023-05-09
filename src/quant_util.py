import sympy as sp
from sympy.physics.quantum.matrixutils import matrix_tensor_product
from list_util import bring_to_front
from linalg_util import *




"""
    Purify a density operator given its eigenvalues and eigenvectors.

    Args:
        eigenvalues (list or tuple): List or tuple of eigenvalues of the density operator.
        eigenvectors (list or tuple): List or tuple of eigenvectors of the density operator.

    Returns:
        sympy.Matrix: Purified state as a matrix object.
"""
def purify_density_operator(rho_in):
    eigenvalues = []
    eigenvectors = []
    eigentuples = rho_in.eigenvects()

    for eigen_tuple in eigentuples:
        # (value, multiplicity, vector)
        value = eigen_tuple[0]
        for i in range(eigen_tuple[1]): # For each natural below multiplicity
            eigenvectors.append(eigen_tuple[2][i]) # Add the ith eigenvector
            eigenvalues.append(value) # Add the ith eigenvalue


    n = len(eigenvalues) # Number of eigenvalues/eigenvectors
    psi = sp.Matrix([[0] * n**2]).T # Initialize purified state as an empty matrix

    for i in range(n):
        eigenvalue = eigenvalues[i]
        eigenvector = eigenvectors[i]
        
        psi_i = sp.sqrt(eigenvalue) * sp.Matrix(matrix_tensor_product(eigenvector, eigenvector)) # Tensor product of eigenvector with itself
        psi = psi + psi_i # Add to the purified state
    return psi



def swap(rho_in, list_in, system_digits):
    M = change_tensor_order_matrix(list_in, system_digits)
    return M * rho_in * M.T




def partial_trace(rho_in, system_digits, traced_system_index, base=2):
    # TODO: Figure out how to transfer base
    num_systems = len(system_digits)
    rho_in = swap(rho_in, bring_to_front(list(range(num_systems)), traced_system_index), system_digits)
    
   
    n = sum(system_digits) # Current total number of digits
    while(system_digits[0] != 0): # While there is something to trace out
        new_size = base ** (n-1) # Size of the new matrix after the partial trace
        rho_out = sp.Matrix([([0] * new_size)]*new_size)
        for row in range(new_size):
            for col in range(new_size):
                rho_out[row, col] = rho_in[row, col] + rho_in[row + new_size, col + new_size]
        

        system_digits[0] = system_digits[0] - 1 # Take one less digit
        n = n-1 # One less digit
        rho_in = rho_out # If loop happens we want the new rho_in to be 

    return sp.Matrix(rho_out)





def tests():
    #rho_in = sp.eye(4)/4
    rho_in = sp.Matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    sp.pprint(rho_in)
    sp.pprint(partial_trace(rho_in, [1,1],0))




tests()