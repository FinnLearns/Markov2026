import numpy as np
import matplotlib.pyplot as plt

def sampledTime():
    U = np.random.uniform(0,1)
    return -(1/rate)*np.log(U)

t = 0 # starting time
rate = 3 # rate of event
A_pts = [] # keep track of events
B_pts = []


# seperately model arrival times of events
while t <= 48:
    score = sampledTime()
    A_pts.append(t)
    t += score

t = 0
while t <= 48:
    score = sampledTime()
    B_pts.append(t)
    t += score

plt.figure(figsize=(10,7))
plt.vlines(x=A_pts, ymin=-0.5, ymax=0.5, color='r', label='A Scores')
plt.vlines(x=B_pts, ymin=-0.5, ymax=0.5, color='b', label='B Scores')

plt.xlim(0,48)
plt.xlabel('t')
plt.xticks([0,10,20,30,40,48])
plt.title('Times where A & B Scored')
plt.legend()
plt.show()