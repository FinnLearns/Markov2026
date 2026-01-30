import numpy as np
import matplotlib.pyplot as plt
import math
import time

# Problem 2 (c)

# PDF of desired distribution
def PDF(x):
  return x * np.exp(-1*x)

startTime = time.time()


def criteria(nums):
  Y1 = -2 * np.log(nums[:,0]) # generate sample Exp(1/2)
  Y2 = nums[:,1] # uniform random variables
  denom = c*0.5*np.exp(-0.5*Y1) # compute cg(Y1)
  numer = Y1 * np.exp(-1*Y1) # compute f(Y1)

  criteria = numer/denom
  mask = Y2 <= criteria # generate a mask
  met = Y1[mask] # apply mask to pick out Y2 samples

  return met

c = 4 / np.exp(1) # acceptance rate
N = 10**6

# number of generated samples is number of wanted samples times acceptance rate
# plus a little extra
U = np.random.uniform(0,1,(math.ceil(1.001*c*N),2))

randNums = criteria(U) # returns samples that meet condition
randNums = randNums[:N] # cut off any extra beyond N samples

print(f"Total time taken: {time.time() - startTime}")

dx = 0.1
r = np.arange(0,15+dx,dx)
fx = PDF(r)

plt.plot(r,fx,'r',label='f(x)')
plt.hist(randNums,bins='auto',density=True,label='Normalized hist')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Acceptance-Rejection Method')

plt.grid()
plt.legend()
plt.show()