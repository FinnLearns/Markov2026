import numpy as np

# write probability transition matrix
p = np.matrix([[0.8959, 0.1041, 0, 0, 0],
              [0.1174, 0.7743, 0.1083, 0, 0],
              [0, 0.1377, 0.7496, 0.1127, 0],
              [0, 0, 0.1616, 0.7210, 0.1174],
              [0, 0, 0, 0.1896, 0.8104]])

evals, evecs = np.linalg.eig(p.transpose()) # compute eigenvectors/values

print(evals) # observe which index eigenvalue 1 is at
evec = evecs[:,3] # get corresponding eigenvector
evec = evec / sum(evec) # normalize so elements sum to 1
print(evec)