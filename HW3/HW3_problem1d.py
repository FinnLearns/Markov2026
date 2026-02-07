import numpy as np
import matplotlib.pyplot as plt

coeff = [1,2,-2]
roots = np.roots(coeff)
print(roots) # find a*

def f_x(X): # pdf to sample
	return (1/3) * X * (1 + X) * np.exp(-1*X)

def g_a(X, a): # pdf with known method to sample from
	return (a**2) * X * np.exp(-1 * a * X)

def c_a(X, a): # c is supremum of f(x)/g(x)
	return np.max(f_x(X) / g_a(X,a))


# generate domain
dx = 0.1
x = np.arange(0,15,dx)
X = x + dx

a_star = 0.732 # from calculated roots


# confirm that our theoretical result matches
c = c_a(X,a_star)
print(1/c)

plt.plot(X,f_x(X), 'red', label='$f(x)$')
plt.plot(X,c*g_a(X,a_star), 'green', label='$c(a^*)g_{a^*}(x)$')
plt.title('$f(x) \, and \, g_a(x)$')
plt.xlabel('$x$')
plt.ylabel('$y$')

plt.grid()
plt.legend()
plt.show()