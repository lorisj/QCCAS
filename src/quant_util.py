import sympy as sp
import math
from sympy.physics.quantum.matrixutils import matrix_tensor_product
from list_util import bring_to_front
from linalg_util import *

# Quantutil should only work on single digits!!!! Leave multiple systems to the simulator.


"""
    Purify a density matrix.

    Args:
        rho_in (sympy.Matrix): Density matrix to be purified.

    Returns:
        sympy.Matrix: Purified state (vector) as a matrix object.
"""
def purify_density_operator(rho_in : sp.Matrix)-> sp.Matrix:
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
    return psi * psi.H # Return |\psi><\psi|, the pure state density matrix.



def swap_digits(rho_in : sp.Matrix, list_in : list[int]) -> sp.Matrix:
    M = change_tensor_order_matrix(list_in)
    return M * rho_in * M.T




def partial_trace_front(rho_in : sp.Matrix, new_size : int) -> sp.Matrix:
    digits_traced = rho_in.shape[0]/new_size
    assert digits_traced.is_integer() , "new_size is inconsistent (i.e. not a divisor of size) with rho_in"
    digits_traced = int(digits_traced)

    rho_out = sp.Matrix([([0] * new_size)]*new_size)
    for row in range(new_size):
        for col in range(new_size):
            for i in range(digits_traced):
                rho_out[row, col] += rho_in[row + new_size * i, col + new_size * i]
    
    return sp.Matrix(rho_out)





def assert_unitary(matrix_in : sp.Matrix):
    assert matrix_in * matrix_in.H ==  matrix_in.H * matrix_in  == sp.eye(matrix_in.shape [0]), f"Input matrix {matrix_in} not unitary" # Checks input matrix is really unitary


def assert_density_matrix(matrix_in : sp.Matrix):
    assert matrix_in.shape[0] == matrix_in.shape[1], "initial state not a matrix (must be a density matrix, do outer product for pure state)"
    assert matrix_in.H == matrix_in ,"initial state matrix not hermitian"
    assert sp.Trace(matrix_in) == 1, "initial state matrix not trace 1"
    assert matrix_in.is_positive_semidefinite(), "initial state matrix not PSD"

def assert_hermitian(matrix_in : sp.Matrix):
    assert matrix_in == matrix_in.H, "observable not hermitian"


def tests():
    #rho_in = sp.eye(4)/4
    rho_in = sp.Matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    sp.pprint(rho_in)
    sp.pprint(partial_trace_front(rho_in, 2))




tests()