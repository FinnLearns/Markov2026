import sympy as sp

# Problem 7 (d)

# perform series expansion utilizing SymPy library

s,n = sp.symbols('s n') # define symbols

mgf = sp.exp((n * sp.exp(s / sp.sqrt(n))) - n - (s*n/sp.sqrt(n))) # define mgf

expanded = mgf.series(s,0,4) # generate series expansion

print(expanded)

