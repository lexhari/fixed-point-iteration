import numpy as np
import warnings

def fixpoint(g, x, maxit=100, tol=1e-15):
    error = tol + 1
    k = 0 # number of iterations
    roots = []
    errors = []
    while error > tol and k < maxit:
        xold = x
        x = g(x)
        error = abs(x - xold)
        roots.append(x)
        errors.append(error)
        k += 1
    if error > tol and k == maxit:
        warnings.warn("Error in Fixed-Point: Maximum iteration is achieved but not tolerance")
    return [roots, errors, k]

# Initial iterates 
x0_1 = -2  
x0_2 = 1 

#main function
f = lambda x: np.exp(x) + x**2 - 4
#candidate functions
g1 = lambda x: np.sqrt(4 - np.exp(x))*(-1)
g2 = lambda x: np.log(4 - x**2)




# Find roots using g1
roots1, errors1, iter1 = fixpoint(g1, x0_1)
print("Solving for a Root using g_1 (x):")
print("n\tEstimate Root\t\tAbsolute Error")

for n in range(1, iter1 + 1):
    print(f"{n}\t{roots1[n-1]:.15f}\t\t{errors1[n-1]:.15f}")


# Find roots using g2
roots2, errors2, iter2 = fixpoint(g2, x0_2)
print("\nSolving for a Root using g_2 (x):")
print("n\tEstimate Root\t\tAbsolute Error")

for n in range(1, iter2 + 1):
    print(f"{n}\t{roots2[n-1]:.15f}\t\t{errors2[n-1]:.15f}")
