import sympy as sp
import math
from sympy.physics.quantum.matrixutils import matrix_tensor_product #TODO: Check if works if removed
from quant_util import *
from list_util import swap_list_positions





class State: # State, i.e a set of quantum systems 

    def __init__(self, matrix, system_digits, base_list = []):
        self.matrix = matrix # Total matrix representing current state.
        self.system_digits = system_digits # array that at index i says how many qudits are in system i
        self.base_list = [2] * len(system_digits) # By default, base is 2.
        if(base_list): # if there is a base
            self.base_list = base_list # What base (2 -> qubit, 3 -> qutrit, etc.)


    def is_pure(self):
        return self.matrix == self.matrix * self.matrix

    def is_separable(self, digit_list =[]):
        # digit_list: if the given digits together are seprable
        if not digit_list:
            digit_list = self.system_digits 
        
        # check_matrix = partial_trace(self.matrix, some_function_that_subtracts(list(range(len(system_digits))), digit_list)) # partial trace out everything but digit_list

        pass # maybe partial trace out every qubit, then see if it is the product? 
    

class Operation: # Quantum operation
    type_list = ["unitary", "measurement", "discard", "purify", "initialize", "split"]   

    # self.input_digit_list
    # self.output_digit_list
    # self.input_base_list: Base for input_digit_list
    # self.parameter: 
    #   Unitary matrix for unitary evolution, 
    #   Observable for measurement, 
    #   Not used (i.e. empty) for discard, purify, split
    #   State for 
    # self.label: for name of operation
    # self.type: type of operation, i.e. something in type_list


    def __init__(self, type, parameter= [], label=""):
        
        self.type = type
        self.parameter = parameter 
        self.label = label 

        self.assert_valid_operation() # Make sure the parameter and type are valid.

        match type:
            case "unitary": # self.parameter has type Matrix (unitary matrix used for evolution)
                pass

            case "measurement": 
                pass

            case "discard":
                pass

            case "purify":
                pass

            case "initialize":
                pass 
            case "split":
                pass

        

    def assert_valid_operation(self):
        assert type in Operation.type_list, "Invalid operation type"
        match type:     
            case "unitary":
                assert self.parameter * self.parameter.H ==  self.parameter.H * self.parameter  == sp.eye(self.parameter.shape()[0]), "Input matrix not unitary" # Checks input matrix is really unitary 
            
            case "measurement":
                assert self.parameter == self.parameter.H, "observable not hermitian"

            case "initialize":
                assert self.parameter.H == self.parameter ,"initial state not hermitian"
                assert sp.Trace(self.parameter) == 1, "initial state not trace 1"
                assert self.parameter.is_positive_semidefinite(), "initial state not PSD"


class Circuit: # Chain of Operations, can change size, but has to be linked together somehow
    
       
    def __init__(self, input_digit_list, input_base_list=[]):
        self.input_system_list = input_digit_list # Input to circuit
        self.operation_list = []
        if base_list:
            self.input_base_list = input_base_list
        else:
            base_list = [2] * len(input_digit_list) # By default we are dealing with qubits
        
        self.current_digit_list = input_digit_list
        self.current_base_list = input_base_list


        


    def operation(self, operation_in, input_system_list):
        match operation_in.type:
            case "unitary": # self.parameter has type Matrix (unitary matrix used for evolution)
                pass

            case "measurement": 
                # Add classical output system
                base = 2
                num_eigenvalues = len(operation_in.parameter.eigenvals()) # Calculate classical digits needed, = ceil(log_2(#eigenvalues))
                num_out_digits = math.ceil(math.log(num_eigenvalues,base))
                classical_digit_index = input_system_list[len(input_system_list ) - 1] 
                self.current_digit_list.insert(classical_digit_index, 1)
                self.current_base_list.insert(classical_digit_index, num_out_digits)

            case "discard":
                pass

            case "purify":
                pass

            case "initialize":
                pass 





    def process(self, state_in):
        state_out = state_in
        for operation in self.operation_list:
            state_out.process(operation)
        
        return state_out


    def swap_systems(self, swap_list):
        pass

    def get_current_system_list(self):
        return self.current_system_list




        





def main():
    print("Running main:")
    





main()


