# Weird result for a sum of sin series as ground acceleration with random noise also added:

import numpy as np
import matplotlib.pyplot as plt

def richter_to_amplitude(M):
   return 10 ** (0.5 * M - 2.4)

def generate_ground_motion(T, dt, M, N):
   w = 2 * np.pi / T
   A = richter_to_amplitude(M)
   G = np.zeros(N)
   for n in range(1, N+1):
       G += A * np.sin(n * w * np.arange(N) * dt) / n
   G += np.random.normal(0, 0.01, N)
   return G

T = 10  # period of ground motion (s)
dt = 0.01  # time step (s)
M = 6.0  # Richter scale magnitude
N = int(T / dt)  # number of time steps

G = generate_ground_motion(T, dt, M, N)

t = np.arange(N) * dt

plt.plot(t, G)
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (g)')
plt.show()
