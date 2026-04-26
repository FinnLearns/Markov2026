import numpy as np
import matplotlib.pyplot as plt
import concurrent.futures

A = B = 1
L = 20
N = 1_000

def exponent(start=False):
    
    if start:
        rate = A
    else:
        rate = A+B
    
    U = np.random.uniform(0,1)
    return -(1/rate) * np.log(U)

def chain(init_state):
    
    currState = init_state
    time = 0

    while currState != L:
         
        if currState == 0:
            
            currState += 1
            time += exponent(True)
        
        else:
            
            U = np.random.uniform(0,1)
            if U <= 0.5:
                currState += 1
            else:
                currState -= 1

            time += exponent()

    return time

def run(sims):
    
    X = [0 for i in range(sims)]
    with concurrent.futures.ProcessPoolExecutor(max_workers=sims) as ex:
            res = list(ex.map(chain, X))
	
    return res

if __name__=='__main__':
    
    res = run(N)

    m_0 = np.average(res)
    var = np.var(res)

    print(f'The expected value of m_0 is {m_0}')
    print(f'The observed variance of m_0 {var}')