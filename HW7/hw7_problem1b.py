import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,90,100) # create time domain

#---Part b: Otis' Gambit---
probability = np.exp(-3.5*(1 - t/90)) # probability that game ends in tie

plt.plot(t, probability)
plt.title('Probability that match ends in tie')
plt.xlabel(r'$t$')
plt.ylabel(r'$P(Tie)$')

plt.title('Probability that match ends in a tie')

plt.show()