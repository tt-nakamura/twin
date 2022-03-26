# reference: P. Jones and L. F. Wanex
#   Foundations of Physics Letters 19 (2006) 75

import numpy as np
import matplotlib.pyplot as plt

D = 4 # distance to destination

# t = inertial time of stationary twin
# tau = proper time of accelerating twin
t2 = np.sqrt((D+4)*D) # time at destination
tau1 = np.arccosh(1 + D/2) # time at reversing acceleration
t4 = 2*t2 # time at returning home
tau2 = 2*tau1 # time at destination
tau3 = 3*tau1 # time at reversing acceleration again
tau4 = 4*tau1 # time at returning home

# proper time of accelerating twin
tau01 = np.linspace(0,tau1,20) # positive acceleration
tau13 = np.linspace(tau1,tau3, 40) # negative acceleration
tau34 = np.linspace(tau3,tau4, 20) # positive acceleration

# hyperbolic motion in inertial coordinate
z01 = np.cosh(tau01)-1 # positive acceleration
z13 = D - np.cosh(tau13 - tau2) + 1 # negative acceleration
z34 = np.cosh(tau34 - tau4) - 1 # positive acceleration

# inertial time of stationary twin
t01 = np.sinh(tau01) # positive acceleration
t13 = t2 + np.sinh(tau13 - tau2) # negative acceleration
t34 = t4 + np.sinh(tau34 - tau4) # positive acceleration

plt.figure(figsize=(6.4,8))
plt.subplot(2,1,1)
plt.plot(tau01,z01,label=r'$0\leq\tau\leq\tau_1$')
plt.plot(tau13,z13,label=r'$\tau_1\leq\tau\leq\tau_3$')
plt.plot(tau34,z34,label=r'$\tau_3\leq\tau\leq\tau_4$')
plt.ylabel(r'$gz/c^2$', fontsize=14)
plt.text(5.8,2.5,r'$gD/c^2=%d$' % D, fontsize=14)
plt.legend(fontsize=12)

plt.subplot(2,1,2)
plt.plot(tau01,t01,label=r'$0\leq\tau\leq\tau_1$')
plt.plot(tau13,t13,label=r'$\tau_1\leq t\leq\tau_3$')
plt.plot(tau34,t34,label=r'$\tau_3\leq t\leq\tau_4$')
plt.xlabel(r'$g\tau/c$', fontsize=14)
plt.ylabel(r'$gt/c$', fontsize=14)
plt.text(0,7,r'$gD/c^2=%d$' % D, fontsize=14)
plt.legend(fontsize=12)

plt.tight_layout()
plt.savefig('fig2.eps')
plt.show()
