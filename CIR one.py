from pyquil.api import WavefunctionSimulator
from pyquil import Program, get_qc
from pyquil.gates import *
import numpy as np

wf = WavefunctionSimulator()

p = Program()

p+=H(0)
p+=CNOT(0,1)
p+=H(0)
p+=CNOT(1,2)
p+=H(0)


wfn = wf.wavefunction(p)

print(wfn)


