import sympy as sp
from sympy.physics.quantum.matrixutils import matrix_tensor_product
from list_util import dict_to_vector
from quant_util import purify_density_operator, partial_trace, swap

def classical_entropy(prob_vector, base=2):
    """
    Calculates the entropy of a probability vector.

    Parameters:
        - prob_vector (list or tuple): A probability vector.

    Returns:
        - sympy expression: The entropy value.
    """
    # Check if the probabilities sum to 1
    
    #assert sum(prob_vector) == 1, "Input probabilities do not sum to 1"

    # Convert the input to a list of sympy.Rational objects
    prob_vector = [sp.sympify(p) for p in prob_vector]

    # Calculate the entropy using the entropy formula
    entropy = -sum(p * sp.log(p, base) for p in prob_vector if p != 0)

    return entropy#.evalf(n=5) # if you need to round




def quantum_entropy(matrix_in, base=2):
    """
    Compute the quantum entropy of a density matrix.

    Args:
        matrix_in (sp.Matrix): Input density matrix.

    Returns:
        float: Quantum entropy.
    """
    return classical_entropy(dict_to_vector(matrix_in.eigenvals()),base)




def main():
    rho_in = sp.eye(2)/2

    pure = purify_density_operator(rho_in)
    pure = pure * pure.H

    a = sp.Symbol("a", complex=True)
    b = sp.Symbol("b", complex=True) 
    #b = sp.sqrt(1-a*sp.conjugate(a))
    varphi = sp.Matrix([[a, b]]).T
    #varphi = sp.Matrix([[1/sp.sqrt(2), 1/sp.sqrt(2)]]).T
    #varphi = sp.Matrix([[0, 1]]).T
    varphi = varphi * varphi.H

    #d = sp.Symbol("d") 
    #sp.pprint(sp.solve("1-a * conjugate(a) + d * conjugate(d)",d))
    # sp.pprint(sp.sympify( (sp.conjugate(a) * a / 2) + (sp.conjugate(b) * b / 2 )) )
    # sp.pprint(b.assumptions0)


    rho_ApsiAr = swap(matrix_tensor_product(varphi, pure),[1,0,2],[1,1,1]) # before cnot stage
    sp.pprint("rho_ApsiAr (before cnot):")
    sp.pprint(rho_ApsiAr)

    cnot = sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    total_cnot = matrix_tensor_product(cnot, sp.eye(2))

    rho_ApsiAr = total_cnot * rho_ApsiAr * total_cnot.T


    sp.pprint("rho_ApsiAr: (after cnot")
    sp.pprint(rho_ApsiAr)


    rho_BAr = partial_trace(rho_ApsiAr,[1,1,1],0)

    rho_B = partial_trace(rho_BAr, [1,1], 1)

    sp.pprint(f"rho_in: {sp.sympify(quantum_entropy(rho_in))} ")
    sp.pprint("(Without reference)")
    sp.pprint(rho_in)
    sp.pprint("(With reference)")
    sp.pprint(pure)


    sp.pprint(f"rho_B: (channel output)")
    sp.pprint(sp.sympify(quantum_entropy(rho_B)))
    sp.pprint(rho_B)

    sp.pprint(f"rho_BAr:")
    sp.pprint(sp.sympify(quantum_entropy(rho_BAr)))
    sp.pprint(rho_BAr)

    print(f"Mutual information:")
    sp.pprint(sp.sympify(quantum_entropy(rho_in) + quantum_entropy(rho_B) - quantum_entropy(rho_BAr)))

    #sp.pprint(sp.sympify(quantum_entropy(varphi)))






def tests():
    assert classical_entropy([1,0]) == 0
    assert classical_entropy([0,1]) == 0
    assert classical_entropy([sp.Rational(1,2), sp.Rational(1,2)]) == 1
    
    assert quantum_entropy()

tests()
