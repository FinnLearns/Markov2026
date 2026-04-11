import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# modeling nonhomogeneous Poisson Point Process with algorithm in P3

def exponential():
    return -1/(maxRate) * np.log(np.random.uniform(0,1))

lPoint = 0
rPoint = 120

# find maximum rate
t = sp.symbols('s')
rate = 0.5*(1 + (t/30)**2)
interval = sp.Interval(lPoint,rPoint)
maxRate = sp.maximum(rate, t, interval)

arrivals = []
T = exponential()

# HPPP with maximum rate
while T <= rPoint+1:
    arrivals.append(T)
    T += exponential()

numArrivals = len(arrivals)
U = np.random.uniform(0,1,size=numArrivals)
accepted = []

# accept/reject arrivals
for n in range(numArrivals):
    prob = rate.subs(t,arrivals[n]) / maxRate
    if U[n] <= prob:
        accepted.append(arrivals[n])

accepted = [int(a) for a in accepted]
print(f'Number of infections: {len(accepted)}')
plt.hist(accepted, bins=120)
plt.xlabel('t')
plt.ylabel('Number of reports')
plt.title('Number of reports per day')
plt.show()