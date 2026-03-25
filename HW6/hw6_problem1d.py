import matplotlib.pyplot as plt
import numpy as np

# create transition probability matrix
p1 = np.array([[0,1,0,0,0],
              [1/3,0,2/3,0,0],
              [0,1/2,0,1/2,0],
              [0,0,2/3,0,1/3],
              [0,0,0,1,0]])

# p2 = np.array([[0,2/3,1/3,0,0],
#               [1/3,0,2/3,0,0],
#               [1/9,4/9,0,4/9,0],
#               [0,0,2/3,0,1/3],
#               [0,0,0,1,0]])

# calculate 50 steps
p1_50 = np.linalg.matrix_power(p1, 50)
# p2_50 = np.linalg.matrix_power(p2, 50)

# Derived theoretical stationary distribution
sd1 = np.array([1/12, 1/4, 1/3, 1/4, 1/12])
# sd2 = np.array([3/26, 3/13, 9/26, 3/13, 1/13])

# start in state 2
initState = np.array([0,0,1,0,0])

pred1 = np.matmul(initState,p1_50)
# pred2 = np.matmul(initState,p2_50)

plt.plot(pred1, label='Calculated')
plt.plot(sd1, label='Theoretical')
plt.xlabel('State')
plt.ylabel('P(State)')
plt.title('Distribution After 50 Steps')
plt.legend()
plt.show()

# plt.plot(pred2, label='Calculated')
# plt.plot(sd2, label='Theoretical')
# plt.xlabel('State')
# plt.ylabel('P(State)')
# plt.title('Distribution After 50 Steps')
# plt.legend()
# plt.show()