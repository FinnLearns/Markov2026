import numpy as np
import matplotlib.pyplot as plt
import concurrent.futures

# utilizes discrete inverse sampling to determine next state
def stepInto(curr, rand):
	total = 0
	
	for e in range(size):
		if p[curr,e] == 0:
			pass
		else:
			total += p[curr,e]
			if rand <= total:
				return e
			
# markov chain function
def markovChain(initState):
    stateList = np.array([]) # list to store results of each step
    currState = initState
    U = np.random.uniform(0,1,numSteps) # uniform random numbers for determing next state
    stateList = np.append(stateList, currState+1)

    for step in range(numSteps):
        currState = stepInto(currState, U[step])
        stateList = np.append(stateList, currState+1)
    return stateList

# concurrently run markov processes
def run(sims):
    initList = [0 for i in range(sims)]
    with concurrent.futures.ProcessPoolExecutor(max_workers=sims) as ex:
            res = list(ex.map(markovChain, initList))
	
    return res

# function to determine ratio of chains that are in state 1 at given time
def getRatios(r,sims):
    ratios = np.array([])
    for i in range(numSteps):
        n = np.count_nonzero(r[:,i] == 1)
        ratios = np.append(ratios, n/sims)

    return ratios


# number of chains to run at once
N = [100, 1000, 10000]

# transition probability matrix
a = 0.99
p = np.matrix([[1-a,a,0],
			   [a,0,1-a],
			   [0,1-a,a]])

initState = 0
size = len(p)
numSteps = 300 # number of simulations to perform
		
if __name__=='__main__':
    results = []
    for i in N:
        
        # split large number of chains into groups
        if i > 100:
            subs = i / 100
            res_total = np.array([])
            for s in range(int(subs)):
                res = run(100)
                res = np.array(res)
                
                if s == 0:
                    res_total = res
                else:
                      res_total = np.concatenate((res_total,res),axis=0)
            
            thing = getRatios(res_total, i)
            results.append(thing)

        # if number of chains is small, run all at once
        else:
            res = run(i)
            res = np.array(res)

            thing = getRatios(res,i)
            results.append(thing)

    # ------PLOTTING---------
    x = np.arange(0,300,1)
    def q1(x):
          q1 = (0.58**2) + (0.71**2)*((-0.98)**x) + (0.41**2)*(0.99**x)
          return q1
    
    plt.figure(figsize=(10,7))
    plt.tight_layout()
    
    plt.subplot(1,3,1)
    plt.plot(x, results[0], label='f(n)')
    plt.plot(x, q1(x), label='$q_n(1)$', alpha=0.3)
    plt.title('N=100')
    plt.xlabel('n')
    plt.ylabel('f(n)')
    plt.legend()

    plt.subplot(1,3,2)
    plt.plot(x, results[1], label='f(n)')
    plt.plot(x, q1(x), label='$q_n(1)$', alpha=0.3)
    plt.title('N=1,000')
    plt.xlabel('n')
    plt.ylabel('f(n)')
    plt.legend()

    plt.subplot(1,3,3)
    plt.plot(x, results[2], label='f(n)')
    plt.plot(x, q1(x), label='$q_n(1)$', alpha=0.3)
    plt.title('N=10,000')
    plt.xlabel('n')
    plt.ylabel('f(n)')
    plt.legend()

    plt.show()
