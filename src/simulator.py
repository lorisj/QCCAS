import sympy as sp
import math
from sympy.physics.quantum.matrixutils import matrix_tensor_product #TODO: Check if works if removed
from quant_util import *
from list_util import swap_list_positions

def num_dimensions(system_digit_list : list[int], system_base_list : list[int])-> int:
    dimensions = 1
    for digit_index, num_digits in enumerate(system_digit_list):
        dimensions *= (system_base_list[digit_index] ** num_digits)
    return dimensions


class Operation: # Quantum operation
    type_list = ["unitary", "measurement", "discard", "purify"]   

    # self.input_digit_list
    # self.input_base_list: Base for input_digit_list
    # self.parameter: 
    #   Unitary matrix for unitary evolution, 
    #   Observable for measurement, 
    #   Not used (i.e. empty) for discard, purify, split
    # self.label: for name of operation
    # self.type: type of operation, i.e. something in type_list


    def __init__(self, type, input_system_list : list[int], system_base_list = [], parameter = [], label : str =""):
        
        self.type = type
        self.parameter = parameter 
        self.label = label 
        self.input_digit_list = input_system_list

        if system_base_list: # If there is a base list, overwrite it.
            self.system_base_list = system_base_list # What base (2 -> qubit, 3 -> qutrit, etc.)


        self.assert_valid_operation() # Make sure the parameter and type are valid.


        

    def assert_valid_operation(self):
        assert self.type in Operation.type_list, f"Invalid operation type '{self.type}' '{Operation.type_list}'"
        match self.type:     
            case "unitary":
                assert_unitary(self.parameter)    
            
            case "measurement":
                assert_hermitian(self.parameter)


class State: # State, i.e a set of quantum systems 

    def __init__(self, matrix, system_digit_list : list[int], system_base_list : list[int] = []):
        assert len(system_base_list) == len(system_digit_list) or len(system_base_list) == 0, f"conflicting number of digits between base_list ({system_base_list}) and system_digits {system_digit_list}"
        
        self.matrix = matrix # Density matrix representing current state.
        self.system_digit_list = system_digit_list # Array that at index i says how many qudits are in system i
        self.system_base_list = [2] * len(system_digit_list) # By default, base is 2.

        if system_base_list: # If there is a base list, overwrite it.
            self.system_base_list = system_base_list # What base (2 -> qubit, 3 -> qutrit, etc.)


    def is_pure(self):
        return self.matrix == self.matrix * self.matrix

    def is_separable(self, digit_list : list[int] =[]):
        # digit_list: if the given digits together are separable
        if not digit_list:
            digit_list = self.system_digit_list
        
        # check_matrix = partial_trace(self.matrix, some_function_that_subtracts(list(range(len(system_digits))), digit_list)) # partial trace out everything but digit_list
        return 0 # maybe partial trace out every qudit, then see if it is the product? 


    def clear_empty_systems(self):
        for index, value in enumerate(self.system_digit_list):
            if value == 0:
                self.system_base_list.pop(index)
                self.system_digit_list.pop(index)
    


    def process(self, operation : Operation):
        match operation.type:
            case "unitary": # self.parameter has type Matrix (unitary matrix used for evolution)
                
                # Complete operation.parameter to act on the current state. 


                Note that you need to store the current system information (digits, base) at each step. Maybe make a class for systems?
        
                # 1) U = U\otimes I^{\otimes |list^C|}
                size_of_list_comp = self.num_qubits - len(list_in)
                big_unitary = matrix_tensor_product(operation.parameter, sp.eye(2**size_of_list_comp))
                #print(op_in)
                # 2) Calculate cob matrix M = cob(list)
                m = self.change_tensor_order_matrix(list_in)
                #print(m)
                # 3) output = MUM^\dagger
                m.H * op_in * m


                self.matrix = operation.parameter * self.matrix * operation.parameter.H

            case "measurement": 
                pass

            case "discard":
                for traced_system_index in operation.input_system_list:
                    num_systems = len(self.system_digit_list) 
                    rho_in = swap_digits(rho_in, bring_to_front(list(range(num_systems)), traced_system_index), self.system_digit_list) # Swap system traced_system_index to the front
        
                
                    new_size = num_dimensions(self.system_digit_list[1:], self.system_base_list[1:]) # Calculate the size of the new matrix after the partial trace


                    rho_out = partial_trace_front(self.matrix, new_size) # Partial trace to new_size

                    # removes system from digit and base list
                    self.system_digit_list[traced_system_index] = 0 
                    self.system_base_list[traced_system_index] = 0

                    rho_in = rho_out # restart the process
                self.clear_empty_systems()
                return sp.Matrix(rho_out)

            case "purify":
                pass

            case "initialize":
                pass 


class Circuit: # Chain of Operations, can change size, but has to be linked together
    
       
    def __init__(self, input_digit_list : list[int], input_base_list: list[int] = []):
        self.input_system_list = input_digit_list # Input to circuit
        self.operation_list = []
        if input_base_list:
            self.input_base_list = input_base_list
        else:
            self.input_base_list = [2] * len(input_digit_list) # By default we are dealing with qubits
        
        self.current_digit_list = input_digit_list
        self.current_base_list = input_base_list



    def operation(self, operation_in : Operation):

        # Updates current_digit_list, current_base_list.
        match operation_in.type:
            case "unitary": # self.parameter has type Matrix (unitary matrix used for evolution)
                pass 

            case "measurement": 
                # Add classical output system
                base = 2
                num_eigenvalues = len(operation_in.parameter.eigenvals()) # Calculate classical digits needed, = ceil(log_2(#eigenvalues))
                num_out_digits = math.ceil(math.log(num_eigenvalues,base))
                classical_digit_index = len(self.current_digit_list) # or input_system_list[len(input_system_list ) - 1] 
                self.current_digit_list.insert(classical_digit_index, 1)
                self.current_base_list.insert(classical_digit_index, num_out_digits)

    
            case "discard":
                for index, value in enumerate(operation_in.input_system_list):
                    self.current_base_list.pop(index)
                    self.current_digit_list.pop(index)


            case "purify":
                pass

            case "initialize":
                pass 
        
        # Add operation to list
        self.operation_list.append(operation_in)



    def process(self, state_in : State) -> State:
        state_out = state_in
        for index, operation in enumerate(self.operation_list):
            state_out.process(operation)
        
        return state_out


    def swap_systems(self, swap_list : list[int]):
        pass

    def get_current_system_list(self) -> list[int]:
        return self.current_system_list

    def unitary(self, input_matrix, input_system_list, label=""):
        unitary_base_list = [self.current_base_list[i] for i in input_system_list] 
        unitary_operation = Operation(type="unitary",input_system_list = input_system_list, system_base_list=unitary_base_list, parameter=input_matrix, label=label)
        self.operation(unitary_operation)

    def h(self, input_system_list):
        one_over_sqrt_2 = sp.sqrt(sp.Rational(1,2))
        hadamard_matrix = one_over_sqrt_2 * sp.Matrix([[1 , 1],[1 , -1]])
        for system_index in input_system_list: # Perform a hadamard on each index.
            self.unitary(input_matrix=hadamard_matrix, input_system_list=[system_index], label="H")

        
    def cnot(self, input_system_list):
        assert len(input_system_list) == 2, f"input_system_list for Circuit.cnot(input_system_list) must have two inputs. Given: {input_system_list}"
        cnot_matrix = sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
        self.unitary(cnot_matrix, "CNOT")



def main():
    print("Running main:")

    my_circuit = Circuit(input_digit_list=[1,1],input_base_list=[2,2])

    my_circuit.h([0])

    zero_mat = sp.Matrix([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    zeros_mat = matrix_tensor_product(zero_mat, zero_mat)
    zeros_state = State(matrix=zeros_mat,system_digit_list=[1,1])


    sp.pprint(my_circuit.process(zeros_state).matrix())
    
    

    





main()


