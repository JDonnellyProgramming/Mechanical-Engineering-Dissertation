# Trying to solve with scipy

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

N = int(input("Number of floors: "))

xi0 = np.zeros(2*N)  # Initial values of x and x'
xi0[0] = 1  # initial displacement of the first floor
xi0[1] = 0  # initial velocity of the first floor

mi = []
ki = []

for j in range(1, N+1):
   m = input(f"m{j} value: ")
   mi.append(int(m))

for l in range(1, N+1):
   k = input(f"k{l} value: ")
   ki.append(int(k))

def equations(xi, t):
   xi = np.reshape(xi, (N, 2))
   xidot = np.zeros((N, 2))
   for i in range(1, N-1):
       xidot[i, 0] = xi[i, 1]
       xidot[i, 1] = (ki[i]*(xi[i-1, 0]-xi[i, 0])/mi[i]
                      - ki[i+1]*(xi[i, 0]-xi[i+1, 0])/mi[i]
                      - xi[i, 1]**2)
   xidot = np.reshape(xidot, 2*N)
   return xidot

t = np.linspace(0, 10, 100)
sol = odeint(equations, xi0, t)

# Plot the results
plt.figure()
for i in range(N):
   plt.plot(t, sol[:, i*2], label=f"x{i+1}")
plt.legend()
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.show()
