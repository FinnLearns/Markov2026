import numpy as np
import sympy as sp
sp.init_printing()

a = sp.symbols('a',real=True, positive=True)
c1, c2, c3, n = sp.symbols('c1 c2 c3 n')
u0 = sp.Matrix([1,0,0])

p = sp.Matrix([[1-a, a, 0],
               [a, 0, 1-a],
               [0, 1-a, a]])

# get evecs, evals of p transpose
e1, v1 = p.T.eigenvects()[0][0], p.T.eigenvects()[0][2][0]
e2, v2 = p.T.eigenvects()[1][0], p.T.eigenvects()[1][2][0]
e3, v3 = p.T.eigenvects()[2][0], p.T.eigenvects()[2][2][0]

# create orthonormal basis
n1 = v1.normalized()
n2 = v2.normalized()
n3 = v3.normalized()

# find coefficients to express initial condition as linear combo of basis vectors
c1 = sp.simplify(u0.dot(n1))
c2 = sp.simplify(u0.dot(n2))
c3 = sp.simplify(u0.dot(n3))

print('---SYMBOLIC RESULTS---\n')
print(f'Coefficients:\nc1: {sp.latex(c1)} \nc2: {sp.latex(c2)} \nc3: {sp.latex(c3)}')
print(f'\n\nEvalues:\ne1: {sp.latex(e1**n)} \ne2: {sp.latex(e2**n)} \ne3: {sp.latex(e3**n)}')
print(f'\n\nUnit Vectors: \n n1: {sp.latex(n1)} \n n2: {sp.latex(n2)} \n n3: {sp.latex(n3)}')

print('\n---NUMERICAL RESULTS---\n')
print(f'Coefficients:\nc1: {sp.latex(c1.subs(a,0.99))} \nc2: {sp.latex(c2.subs(a,0.99))} \nc3: {sp.latex(c3.subs(a,0.99))}')
print(f'\n\nEvalues:\ne1: {sp.latex(e1**n)} \ne2: {sp.latex(e2.subs(a,0.99)**n)} \ne3: {sp.latex(e3.subs(a,0.99)**n)}')
print(f'\n\nUnit Vectors: \n n1: {sp.latex(n1.subs(a,0.99))} \n n2: {sp.latex(n2.subs(a,0.99))} \n n3: {sp.latex(n3.subs(a,0.99))}')