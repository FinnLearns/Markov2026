import numpy as np
import matplotlib.pyplot as plt

# Problem 4 (b)

def pdf(t): # compute derived pdf function
  f = 3*t**2 / 60**3
  return f

td = np.linspace(0,60,100) # define domain to compute pdf
N = 10**5 # given number of points

# sample three friends' arrival time in minutes after 6pm
uniformTimes = np.random.uniform(0,60,(N,3))

# T must be time that last friend arrives, which is biggest time among friends
T = [np.max(event).item() for event in uniformTimes]

plt.hist(T,bins='auto',density=True,label='Normalized Histogram')
plt.plot(td,pdf(td),label="pdf")
plt.xlabel('t')
plt.ylabel('$f_{T}(t)$')
plt.grid()

plt.legend()
plt.show()