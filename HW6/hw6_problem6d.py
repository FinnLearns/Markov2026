import numpy as np
import concurrent.futures


def avalanche(b):
    state = b
    size = 1 # keep track of avalanche size
    
    for _ in range(2): # only need to simulate first two generations after birth
        
        Z = np.random.binomial(state, prob)
        state = 2*Z
        size += state
  
    if size != 3:
        return 0
    else:
        return 1


def run(sims):
    
    X = [1 for i in range(sims)]
    with concurrent.futures.ProcessPoolExecutor(max_workers=sims) as ex:
            res = list(ex.map(avalanche, X))
	
    return res

N = 10**3
a = 0.5
prob = 1 - a

if __name__=='__main__':
    
    sub = 100
    results = []
    batches = int(N / sub)

    for batch in range(batches):
        
        res = np.array(run(sub))
        results = np.concatenate((results,res))

    is3 = np.sum(results) # S=3 represented as 1, S!=3 as 0
    prob = is3 / N

    print(f'Probability of S=3: {prob}')