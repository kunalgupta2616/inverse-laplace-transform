import sympy.polys.partfrac
from sympy.integrals.transforms import inverse_laplace_transform
from sympy.abc import s

""" Function to return the partial fraction decomposition
    of the equation in frequency domain(s)
""" 
def partialFrac(f):
    return sympy.polys.partfrac.apart(f)
    
"""main function to call that will output the partial frac
   as well as the final inverse laplace transform 
"""      
def invLaplace(f=(3*s + 2)/(s**2 -(3*s) +2)):
    part = partialFrac(f)
    print("Partial Fraction Decomposition: ",part)
    t = sympy.symbols('t',positive=True)
    ans = sympy.inverse_laplace_transform(part,s,t)
    return "Inverse Laplace Transform is: ",ans

Eq = input("Enter a Equation:")
invLaplace(eval(Eq))