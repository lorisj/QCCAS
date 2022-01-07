import sympy as sp
# Diagonalizes matrix mat_in into a list of eigenvectors/eigenvalues that are orthoganal to each other.
# arguments: 
#               mat_in: matrix input (must be hermitian)
#
#
# returns:      List diag
#                    diag = [ [a_i, |i>] ]_i  where for all i:  a_i is a complex number, |i> is a vector in C^n
#                           each entry in diag = [eigenvalue_i, eigenvector_i]
#               Note that repeated eigenvalues are okay

def spectral_decomp(mat_in):
    assert(mat_in.H == mat_in)
    
    return diag