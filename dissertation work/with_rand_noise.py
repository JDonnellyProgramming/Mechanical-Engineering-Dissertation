# Now  am looking at two floors with tuning for a vibration absorber where I will find the mode shapes an natural frequencies with damping or ground acceleration for now:

import numpy as np
import scipy.linalg as la

# system parameters
m1 = 10  # mass of floor 1
m2 = 20  # mass of floor 2
k1 = 500  # spring constant between floor 1 and ground
k2 = 1000  # spring constant between floor 1 and floor 2
k3 = 800  # spring constant between floor 2 and ground

# create mass matrix
M = np.diag([m1, m2])

# create stiffness matrix
K = np.array([[k1+k2, -k2], [-k2, k2+k3]])

# find natural frequencies and mode shapes
evals, evecs = la.eig(K, M)

# sort natural frequencies and mode shapes
idx = np.argsort(evals)
evals = evals[idx]
evecs = evecs[:, idx]

# print natural frequencies and mode shapes
print("Natural frequencies:", np.sqrt(evals))
print("Mode shapes:\n", evecs)

# vibration absorber parameters
ma = 5  # mass of absorber
ka = 10000  # spring constant of absorber
xa = 0.5  # position of absorber on floor 2

# calculate effective stiffness and mass of system with absorber
keff = k1 + k2 * (1 - evecs[0, 1]**2) + k3 * evecs[0, 1]**2 + ka * evecs[0, 1]**2
meff = m1 + m2 * evecs[0, 1]**2 + ma * evecs[0, 1]**2

# calculate natural frequency and mode shape of system with absorber
omega = np.sqrt(keff / meff)
psi1 = evecs[:, 0]
psi2 = np.concatenate(([xa], evecs[:, 1]))

# print natural frequency and mode shape of system with absorber
print("Natural frequency with absorber:", omega)
print("Mode shape with absorber on floor 2:\n", psi2)

