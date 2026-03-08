import numpy as np
import matplotlib.pyplot as plt

# utilizes discrete inverse sampling to determine next state
def stepInto(curr, step):
	rand = U[step]
	total = 0
	
	for e in range(size):
		if p[curr,e] == 0:
			pass
		else:
			total += p[curr,e]
			if rand <= total:
				return e

# transition probability matrix
p = np.matrix([[0.8959, 0.1041, 0, 0, 0],
              [0.1174, 0.7743, 0.1083, 0, 0],
              [0, 0.1377, 0.7496, 0.1127, 0],
              [0, 0, 0.1616, 0.7210, 0.1174],
              [0, 0, 0, 0.1896, 0.8104]])

numSteps = int(10**6) # number of simulations to perform
size = len(p)
stateList = np.array([]) # list to store results of each step

U = np.random.uniform(0,1,numSteps)

currState = np.random.randint(0, 5) # start in random state
stateList = np.append(stateList, currState+1)
for step in range(numSteps):
	currState = stepInto(currState, step)
	stateList = np.append(stateList, currState+1)

#---------Plotting---------

def detailed_balance(a, b):
    sd = []
    sum = 0
    denom = 1 + np.exp(a-b) + np.exp(3*(a-b)) + np.exp(6*(a-b)) + np.exp(10*(a-b))
    for i in range(0, 5):
        sum += i
        entry = np.exp((sum)*(a-b)) / denom
        sd.append(entry)

    return sd

evec = [0.2966, 0.2630, 0.2068, 0.1443, 0.0893]

plt.figure(figsize=(10,7))
plt.tight_layout()

plt.subplot(1,3,1)
plt.hist(stateList, density=True, bins=np.arange(0.5, 6.5, 1), rwidth=0.8, label="Simulation")
plt.xlabel('State')
plt.ylabel('P(State)')
plt.legend()

plt.subplot(1,3,2)
plt.bar(range(1,6), evec, width=0.8, align='center', label='Eigenvector Dist.', color='r')
plt.legend()

plt.subplot(1,3,3)
plt.bar(range(1,6), detailed_balance(0.04,0.16), width=0.8, align='center', label='Detailed Balance Dist.', color='g')
plt.legend()

plt.show()