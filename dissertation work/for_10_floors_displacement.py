# Python Program to work out the natural frequencies for any number of floors:

import numpy as np
from scipy.linalg import eigh

N = int(input("How many floors: "))

# Initialize empty lists for the masses and spring constants
m = []
k = []

# Loop through each floor and ask for the mass and spring constant
for i in range(1, N+1):
   a = float(input(f"m{i} value: "))
   b = float(input(f"k{i} value: "))
   m.append(a)
   k.append(b)

# Create diagonal matrices for the masses and spring constants
M = np.diag(m)
K = np.diag(k)

# Create an identity matrix for the off-diagonal terms
I = np.identity(N-1)

# Add the off-diagonal terms to the stiffness matrix
for i in range(N-1):
   K[i][i+1] = -k[i+1]
   K[i+1][i] = -k[i+1]

# Solve for the natural frequencies and mode shapes with respect to M
eigvals, eigvecs = eigh(K, M)

# Print the natural frequencies and mode shapes
print("Natural Frequencies:")
print(eigvals)
print("Mode Shapes:")
print(eigvecs)
