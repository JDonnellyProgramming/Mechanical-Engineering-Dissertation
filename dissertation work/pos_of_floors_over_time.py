# For 10 floors:

import numpy as np
from scipy.integrate import odeint

def equation_of_motion(x, t, m, c, k, N, A, B):
   dxdt = np.zeros_like(x)
   for i in range(N - 1):
       dxdt[2 * i] = x[2 * i + 1]
       dxdt[2 * i + 1] += (-c[i] * (x[2 * i + 1] - x[2 * i]) + c[i + 1] * (x[2 * (i + 1)] - x[2 * i])) / m[i]
       dxdt[2 * i + 1] += (-k[i] * (x[2 * i] - A * np.sin(B * t)) + k[i + 1] * (x[2 * (i + 1)] - x[2 * i])) / m[i]

   dxdt[2 * (N - 1)] = x[2 * (N - 1) + 1]
   dxdt[2 * (N - 1) + 1] = -k[N - 1] * (x[2 * (N - 1)] - A * np.sin(B * t)) / m[N - 1]
   return dxdt

N = 10 # number of floors
m = np.ones(N) * 1000 # mass of each floor
c = np.ones(N) * 10 # damping coefficient of each floor
k = np.ones(N) * 10000 # spring constant of each floor
A = 0.1 # amplitude of the external force
B = 2*np.pi/10 # frequency of the external force
x0 = np.zeros(2 * N) # initial conditions
x0[0] = 0.01 # initial displacement of the first floor

t = np.linspace(0, 10, 1000)
sol = odeint(equation_of_motion, x0, t, args=(m, c, k, N, A, B))

# extract x values
x = sol[:, range(0, 2*N, 2)]

# plot results
import matplotlib.pyplot as plt
for i in range(N):
   plt.plot(t, x[:, i], label=f"floor {i+1}")
plt.xlabel('Displacement (m)')
plt.ylabel('Time (s)')
plt.legend()
plt.show()
