import numpy as np
import matplotlib.pyplot as plt
import math

# Problem 3 (b)

def function(pts): # evaluates integral
	func = 1 / ((pts**2) + (1 / pts**4))
	return func

def evalPts(pts): # determine which points are under the integrand f
	# seperate uniformly sampled list into x and y coordinates
	x = pts[:,0]
	y = pts[:,1]

	outputs = function(x) # evaluate f(x)

	result = y <= outputs # number of True indicates how many random points
	# are below f(x)

	return result

# Define given range of exponents and declare lists
X = np.arange(1,5.1,0.1)
samples = []
vals = []

for n in X:
 N = math.floor(10**n) # compute given expression
 pts = np.random.uniform(0,1, (N,2)) # sample N points
 inIntegral = evalPts(pts) # get boolean list were True indicates points is under f
 fraction = (sum(inIntegral) / N).item() # compute fraction

 # record results
 vals.append(fraction)
 samples.append(N)


# numerically compute integral
dx = 0.1
d = np.arange(0,1+dx,dx)
numInt = np.trapezoid(function(d),dx=dx)

plt.plot(samples, vals, label="Sampled 'Integral'")
plt.hlines(numInt, xmin=samples[0], xmax=samples[-1], color='red',linestyles='--',label="True Value")
plt.xscale('log')
plt.xlabel('N')
plt.ylabel('E[N]')
plt.grid()

plt.legend()
plt.show()