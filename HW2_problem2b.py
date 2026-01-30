import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import time

# Problem 2 (b)

# PDF of desired distribution
def PDF(x):
  return x * np.exp(-1*x)

startTime = time.time()

N = 10**6 # number of samples to take
U = np.random.uniform(0,1,N)

# Generate N random numbers from distribution using newton root-finding algorithm
X = [sp.optimize.newton(lambda x: -1*np.exp(-1*x) * (1 + x) + 1 - sample, 0.5) for sample in U]

print(f"Total time taken: {time.time() - startTime} seconds")

dx = 0.1
r = np.arange(0,15+dx,dx)
fx = PDF(r)

plt.plot(r,fx,'r',label='f(x)')
plt.hist(X,bins='auto',density=True,label='Normalized hist')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Inverse Sampling Method')

plt.grid()
plt.legend()
plt.show()