import numpy as np
import matplotlib.pyplot as plt

samples = 10**5
lambduh = 3
t = 48
N = np.random.poisson(2*lambduh*t, size=samples)
A_cond = np.random.binomial(N, 0.5)
B_cond = N - A_cond


# compute outcomes
D = 2*(A_cond - B_cond)
expected = np.sum(D) / samples
variance = np.sum((D - expected)**2) / samples
prob0 = (D==0).sum() / samples

print(f'Expection: {expected} \nVariance: {variance} \n P(D(t) = 0): {prob0}')