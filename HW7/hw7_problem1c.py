import matplotlib.pyplot as plt
import numpy as np

#---Part c: Otis' Demise---

t = np.linspace(0,90,100) # create time domain

rules = [ # create piecewise defined function that changes when score is made
    (lambda x : np.exp(-3.5*(1 - x/90)), t < 60),
    (lambda x : 1.5 * (1-x/90) * np.exp(-3.5*(1 - x/90)), t >= 60)
]

evals, conds = zip(*rules)

probs = np.piecewise(t, conds, evals)
plt.plot(t, probs)
plt.xlabel(r'$t$')
plt.ylabel(r'$P(Tie)$')
plt.title('Probability that match ends in a tie')

plt.show()