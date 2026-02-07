import numpy as np

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
p = np.matrix([[1/2, 1/2, 0, 0, 0, 0],
				[0, 1/2, 1/2, 0, 0, 0],  
				[1/3, 0, 1/3, 1/3, 0, 0],
				[0, 0, 0, 1/2, 1/2, 0],
				[0, 0, 0, 0, 0, 1],
				[0, 0, 0, 0, 1, 0]])

size = len(p)
steps = 5
sims = 10_000
finished = 0

for sim in range(sims):
	U = np.random.uniform(0,1,steps)

	currState = 0 # start in state 1
	stateList = [currState]
	for step in range(steps):
		currState = stepInto(currState, step)
		stateList.append(currState)

	if stateList[-1] == 3: # ending in 4th state, 3rd row
		finished += 1

print(finished / sims)