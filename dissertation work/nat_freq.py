# Now getting tuned values for the vibration absorber:

import numpy as np
import sympy as sp

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

A = np.linalg.inv(M) @ K

# Find the eigenvalues and eigenvectors of the matrix A
eigvals, eigvecs = np.linalg.eig(A)

print("The natural frequencies are:", eigvals)

for i in range(N):
   omega = np.sqrt(eigvals[i])
   mt = m[0] * eigvecs[0][i] ** 2 / eigvecs[i][i] ** 2
   kt = omega ** 2 * mt
   print(f"\nMode {i+1} Tuning:")
   print(f"Tuned Mass: {mt:.2f} kg")
   print(f"Tuned Stiffness: {kt:.2f} N/m")