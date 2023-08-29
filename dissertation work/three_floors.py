# Now we will add random noise and sum of cos too:

import numpy as np
import matplotlib.pyplot as plt

def generate_ground_motion(t, M, damping_ratio, dt, num_modes):
   # Constants for seismic design
   gravity = 9.81  # m/s^2
   omega_n = 2 * np.pi * np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])  # natural frequencies in Hz

   # Convert Richter scale to amplitude
   A = 10 ** (0.4 * (M - 6))

   # Generate random noise with normal distribution
   noise = np.random.normal(0, 0.1, len(t))

   # Generate Fourier series
   Tn = 2 * np.pi / omega_n  # period of each mode
   An = A * (omega_n ** 2) / np.sqrt((omega_n ** 2 - (2 * np.pi * damping_ratio * omega_n) ** 2) ** 2 + (
           2 * np.pi * damping_ratio * omega_n * omega_n) ** 2)  # amplitude of each mode
   Bn = damping_ratio * omega_n * An  # coefficient for cos term of each mode
   f = np.zeros(len(t))
   for n in range(num_modes):
       f += An[n] * np.sin(2 * np.pi * (n + 1) * t / Tn[n]) + Bn[n] * np.cos(2 * np.pi * (n + 1) * t / Tn[n])

   # Add random noise to the Fourier series
   f += noise

   # Scale the ground motion by gravity
   f *= gravity

   return f

# Example usage:
t = np.linspace(0, 10, 3000)
f = generate_ground_motion(t, 6.5, 0.05, 0.0033, 6)
plt.plot(t, f)
plt.show()
