import numpy as np

# uses discrete inverse sampling to determine next state
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


# transition matrix
p = np.matrix([[9/10, 1/10, 0], #G
				[0, 7/8, 1/8],  #S
				[2/5, 0, 3/5]]) #D
				  #G  #S  #D

size = len(p)
steps = 10_000
U = np.random.uniform(0,1,steps)

currState = 0 # start in row G
stateList = [currState]
for step in range(steps):
	currState = stepInto(currState, step)
	stateList.append(currState)

# find fraction of states that were G 
occursG = stateList.count(0)
fraction = occursG / len(stateList)

print(fraction)