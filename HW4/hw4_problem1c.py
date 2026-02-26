import numpy as np

# utilizes discrete inverse sampling to determine next state
def stepInto(curr, rand):
    if rand <= p[0]:    # has probability q
        return curr - 1
    elif rand <= p[1] + p[0]:  # has probability p
        return curr + 1
    else:               # has probability s
        return -1

# transition probability matrix
p = np.array([0.4, 0.35, 0.25]) # q, p, s in order

sims = 100_000 # number of simulations to perform
results = [] # list to store results of each simulation

for sim in range(sims):
    
    currState = 10 # start with 10 dollars
    finished = False # flag to stop current simulation
    
    while finished == False:
        
        U = np.random.uniform(0,1) # generate random uniformly distributed num
        nextStep = stepInto(currState, U) # step into next state

        if nextStep == 0: # if state is 0 (out of money) then retire
            results.append(0)
            finished = True
        elif nextStep == -1:
            results.append(currState)
            finished = True
        else:
            currState = nextStep

avgEnd = np.average(results)
print(f'Average retired state: {avgEnd}')