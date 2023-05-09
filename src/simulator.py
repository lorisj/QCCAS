import sympy as sp
import math
from sympy.physics.quantum.matrixutils import matrix_tensor_product #TODO: Check if works if removed
from quant_util import *
from list_util import swap_list_positions


class State: # State, i.e a set of quantum systems 

    def __init__(self, matrix, system_digits, base):
        self.matrix = matrix # Total matrix representing current state.
        self.system_digits = system_digits # array that at index i says how many qudits are in system i
        self.base = base # What base (2 -> qubit, 3 -> qutrit, etc.)

    def process(self, operation):
        match operation.type:
            
            case "unitary": # self.parameter has type Matrix (unitary matrix used for evolution)
                self.matrix = operation.parameter * self.state * operation.parameter.H


            case "measurement": 
                # If target is given then output it otherwise do a measure channel
                pass
            
            case "discard":
                for index, traced_system_index in enumerate(operation.system_index_list):
                    self.matrix = partial_trace(self.matrix, self.system_digits, traced_system_index,self.base) 
                    self.system_digits[index] = 0
                

        return self
    

class Operation: # Quantum operation
    type_list = ["unitary", "measurement", "discard", "purify"]   
    def __init__(self, type, system_index_list, parameter= [], label=""):
        assert type in Operation.type_list, "Invalid operation type"
        self.type = type
        # parameter: Unitary matrix for unitary evolution, observable for measurement, not used (can be empty) for discard
        self.parameter = parameter 
        self.system_index_list = system_index_list # List that says which systems the operation will work on.  
        self.label = "" # Label for name of operation


    


class Circuit: # Chain of Operations, can change size, but has to be linked together somehow
    
       
    def __init__(self, dimension_list, base_list=[]):
        self.system_list = dimension_list
        self.operation_list = []
        if base_list:
            self.base_list = base_list
        else:
            base_list = [2] * len(dimension_list) # By default we are dealing with qubits
        


        


    def discard(self, system_index):
        pass

    

    def unitary(self, unitary_matrix, system_index_list, label=""):
        
        # Assert checks:
        systems_dim = 1
        for s in system_index_list:
            systems_dim *= self.base_list[s] ** self.dimension_list[s] # TODO: Check this
        assert unitary_matrix.shape()[0] == unitary_matrix.shape()[1] == systems_dim  , 0 # Checks that the dimension of the target system(s) is the same as the unitary
        assert unitary_matrix * unitary_matrix.H ==  unitary_matrix.H * unitary_matrix  == sp.eye(systems_dim) # Checks input matrix is really unitary 
    


    def process(self, state_in):
        state_out = state_in
        for operation in self.operation_list:
            state_out.process(operation)
        
        return state_out






        





def main():
    print("Running main:")
    





main()


