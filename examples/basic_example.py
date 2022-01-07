import qtilities as qti
import linalg_utilities
def main():

    #Parameters ---------------------------------------------------------------------------------------------------------------
    
    num_quant_reg = 3
    num_class_reg = 2

    #op_list[i] = [(quant_op1, class_op1), ...] where quant_op = [U_1,U_2,U_3, ...] : rho -> (U_1 \otimes U_2 \otimes ...) rho 
    #                                                 class_op = [f_1,f_2,f_3, ...] : class_reg[i] -> fi(class_reg[i]) 
    #when displaying, don't show identity operators
    op_list = []
    
    #End Parameters -----------------------------------------------------------------------------------------------------------

