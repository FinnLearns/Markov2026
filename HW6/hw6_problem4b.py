import numpy as np
import matplotlib.pyplot as plt
import concurrent.futures


def avalanche(b):
    state = b # size of generation
    for gen in range(gens):
        
        # randomly choose which objects branch
        Z = np.random.binomial(state, prob)
        state = 2*Z
        if state == 0: # process dies
            return 1
    
    return 0


def run(sims):
    
    X = [1 for i in range(sims)]
    with concurrent.futures.ProcessPoolExecutor(max_workers=sims) as ex:
            res = list(ex.map(avalanche, X))
	
    return res

N = 10**3
a = 0.49 # probability 'parameter'
gens = 200
prob = 1 - a

if __name__=='__main__':
    
    # subdivide number of processes run concurrently (computer crashed trying all of them)
    sub = 100
    results = []
    batches = int(N / sub)

    for batch in range(batches):
        
        res = np.array(run(sub))
        results = np.concatenate((results,res))

    died = np.sum(results) # dead processes represented as 1, alive as 0
    deathProb = died / N

    print(f'Probability of Death: {deathProb}')