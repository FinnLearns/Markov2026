import numpy as np
import matplotlib.pyplot as plt

# Problem 1 (d)

# define constants
x0 = 10
gamma = 4

# inverse CDF function
def transformation(u):
  rv = x0*(u**(1 / (-1*gamma + 1)))

  return rv

# PDF of X
def PDF(x):
  p = (gamma - 1) * (x0**(gamma - 1)) * (x**(-1*gamma))

  return p

N1,N2,N3 = 100,1000,10000 # input number of samples to be taken

# Find N uniformly distributed random numbers
U1 = np.random.uniform(0,1,N1)
U2 = np.random.uniform(0,1,N2)
U3 = np.random.uniform(0,1,N3)

# Generate numbers according to X's distribution
fromDist1 = transformation(U1)
fromDist2 = transformation(U2)
fromDist3 = transformation(U3)

# Generate prescribed range to evaluate
dx = 0.5
r = np.arange(0,60+dx,dx)
fx = np.piecewise(r,[r<x0,r>=x0],[lambda r: 0, lambda r: PDF(r)]) # evaluate PDF

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

datasets = [fromDist1, fromDist2, fromDist3]
numSamples = [N1,N2,N3]

for i, ax in enumerate(axes):
    ax.hist(datasets[i], bins='auto', density=True, label='Normalized Hist')
    ax.plot(r, fx, 'r', label='f(x)')

    ax.set_title(f'N={numSamples[i]} Samples')
    ax.set_xlim(0, 60)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.grid(True)
    ax.legend()

plt.show()