# reference: P. Jones and L. F. Wanex
#   Foundations of Physics Letters 19 (2006) 75

import numpy as np
import matplotlib.pyplot as plt

D = 4 # distance to destination

# t = proper time of freely-falling twin
# tau = coordinate time of stationary twin in Rindler metric
tau1 = np.arccosh(1 + D/2) # time at reversing gravitional field
tau2 = 2*tau1 # time at destination
tau3 = 3*tau1 # time at reversing gravinational field again
tau4 = 4*tau1 # time at returning home
t2 = np.sqrt((D+4)*D) # time at destination
t4 = 2*t2 # time at returning home

# coordinate time of stationary twin in Rindler metric
tau01 = np.linspace(0,tau1,20) # downward gravitational field
tau13 = np.linspace(tau1,tau3,40) # upward
tau34 = np.linspace(tau3,tau4,20) # downward

# geodesic motion in Rindler metric
zeta01 = 1/np.cosh(tau01) - 1 # downward gravitational field
zeta13 = 1 - (1+D)/np.cosh(tau13 - tau2) # upward
zeta34 = 1/np.cosh(tau34 - tau4) - 1 # downward

# proper time of freely-falling twin
t01 = np.tanh(tau01) # downward gravitational field
t13 = t2 + (1+D)*np.tanh(tau13 - tau2) # upward
t34 = t4 + np.tanh(tau34 - tau4) # downward

plt.figure(figsize=(6.4,8))
plt.subplot(2,1,1)
plt.plot(t01,zeta01,label=r'$0\leq t\leq t_1$')
plt.plot(t13,zeta13,label=r'$t_1\leq t\leq t_3$')
plt.plot(t34,zeta34,label=r'$t_3\leq t\leq t_4$')
plt.ylabel(r'$g\zeta/c^2$', fontsize=14)
plt.text(7.6,-0.2,r'$gD/c^2=%d$' % D, fontsize=14)
plt.legend(fontsize=12)

plt.subplot(2,1,2)
plt.plot(t01,tau01,label=r'$0\leq t\leq t_1$')
plt.plot(t13,tau13,label=r'$t_1\leq t\leq t_3$')
plt.plot(t34,tau34,label=r'$t_3\leq t\leq t_4$')
plt.xlabel(r'$gt/c$', fontsize=14)
plt.ylabel(r'$g\tau/c$', fontsize=14)
plt.text(0,4.5,r'$gD/c^2=%d$' % D, fontsize=14)
plt.legend(fontsize=12)

plt.tight_layout()
plt.savefig('fig4.eps')
plt.show()
