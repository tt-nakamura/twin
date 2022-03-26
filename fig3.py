# reference: P. Jones and L. F. Wanex
#   Foundations of Physics Letters 19 (2006) 75

import numpy as np
import matplotlib.pyplot as plt

D = np.geomspace(1e-2,5,100) # distance to destination
t = 2*np.sqrt((D+4)*D) # age of intertial twin
tau = 4*np.arccosh(1 + D/2) # age of accelerating twin

plt.plot(D,t,label=r'$gt_4/c$ (twin A)')
plt.plot(D,tau,label=r'$g\tau_4/c$ (twin B)')
plt.xlabel(r'$gD/c^2$', fontsize=14)
plt.ylabel(r'$gt_4/c$, $g\tau_4/c$', fontsize=14)
plt.legend(fontsize=14)
plt.tight_layout()
plt.savefig('fig3.eps')
plt.show()

