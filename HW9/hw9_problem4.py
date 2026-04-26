import numpy as np
import matplotlib.pyplot as plt

def approx(m):
    tally = 0
    for s in range(1,m):
        tally += 1/s

    return tally

def exact(m):
    
    return np.log(m)

m = 100
beta = 1

m_range = np.arange(1,m+1,1)

my_exact = exact(m_range) / beta

my_approx = []
for i in m_range:
    my_approx.append(approx(i) / beta)

plt.plot(m_range, my_approx, label='Expected')
plt.plot(m_range, my_exact, label='Deterministic')
plt.xlabel('m')
plt.ylabel(r'$\tau_m$')

plt.legend()
plt.show()