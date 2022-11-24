import linalg_util as linalg
import quant_util as quant

class QCCAS:
    




    def __init__(self, num_qreg, num_creg):
        qreg = QRV(quant.init_quant_regs(num_qreg) , 1)
        