import numpy as np
import matplotlib.pyplot as plt
import concurrent.futures

N = [100,1_000,10_000,100_000]
TIME = 5
RATE = 1

def actual_prob(t):
     prob = (1/6) * np.exp(-t) * (-2*np.sin(t) + np.cos(t) + 2*np.sinh(t) + np.cosh(t))
     return prob

def exponential():
     U_t = np.random.uniform(0,1)
     exp = -np.log(U_t)
     return round(exp, 1)

def chain(s):
    t = 0
    state_list = [1 if s == 1 else 0]
    time_list = []
    state = s
    while t <= TIME:
        tau = exponential()
        t += tau
        time_list.append(tau)

        state = (state + 1) % 4
        
        if state == 1:
            state_list.append(1)
        else:
            state_list.append(0)
    
    state_list = state_list[:-1]
    time_list = [int(10*i) for i in time_list]
    states = np.repeat(state_list, time_list)
    
    return states[:50]

def run(sims):
    U_n = np.random.uniform(0,1,size=sims)
    
    X = [1 if U_n[i] <= 1/3 else 2 for i in range(sims)]
    with concurrent.futures.ProcessPoolExecutor(max_workers=sims) as ex:
            res = list(ex.map(chain, X))
	
    return res

if __name__=='__main__':
    all_probs = []
    for n in N:
        results = np.zeros(50)
        sub = 100
        batches = int(n / sub)

        for batch in range(batches):
            
            res = np.array(run(sub))
            for r in res:
                results += r

        prob_at_1 = results / n
        all_probs.append(prob_at_1)

    fig, ax = plt.subplots(2,2,figsize=(10,10))
    
    time = np.linspace(0,5,50)
    
    ax[0,0].plot(time, all_probs[0], label='Sim')
    ax[0,0].plot(time, actual_prob(time), label='Predicted')
    ax[0,0].set_ylim(0,0.5)
    ax[0,0].set_xlabel('time')
    ax[0,0].set_ylabel(r'$P(X_t = 1)$')
    ax[0,0].set_title(f'{N[0]} Markov Chains')

    ax[0,1].plot(time, all_probs[1], label='Sim')
    ax[0,1].plot(time, actual_prob(time), label='Predicted')
    ax[0,1].set_ylim(0,0.5)
    ax[0,1].set_xlabel('time')
    ax[0,1].set_ylabel(r'$P(X_t = 1)$')
    ax[0,1].set_title(f'{N[1]} Markov Chains')

    ax[1,0].plot(time, all_probs[2], label='Sim')
    ax[1,0].plot(time, actual_prob(time), label='Predicted')
    ax[1,0].set_ylim(0,0.5)
    ax[1,0].set_xlabel('time')
    ax[1,0].set_ylabel(r'$P(X_t = 1)$')
    ax[1,0].set_title(f'{N[2]} Markov Chains')

    ax[1,1].plot(time, all_probs[3], label='Sim')
    ax[1,1].plot(time, actual_prob(time), label='Predicted')
    ax[1,1].set_ylim(0,0.5)
    ax[1,1].set_xlabel('time')
    ax[1,1].set_ylabel(r'$P(X_t = 1)$')
    ax[1,1].set_title(f'{N[3]} Markov Chains')
    
    plt.legend()
    plt.show()
