# For three floors with everything considered:

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parameters
m1 = float(input("Enter mass of floor 1 (kg): "))
m2 = float(input("Enter mass of floor 2 (kg): "))
m3 = float(input("Enter mass of floor 3 (kg): "))

k1 = float(input("Enter stiffness of floor 1 (N/m): "))
k2 = float(input("Enter stiffness of floor 2 (N/m): "))
k3 = float(input("Enter stiffness of floor 3 (N/m): "))

c1 = float(input("Enter damping coefficient of floor 1 (Ns/m): "))
c2 = float(input("Enter damping coefficient of floor 2 (Ns/m): "))
c3 = float(input("Enter damping coefficient of floor 3 (Ns/m): "))

A = float(input("Enter amplitude of earthquake acceleration (m/s^2): "))
omega = float(input("Enter frequency of earthquake acceleration (rad/s): "))


# System of equations
def equations(y, t):
   x1, x2, x3, x1dot, x2dot, x3dot = y

   # Accelerating earthquake matrix for each separate floor
   x1_acc = A * np.sin(omega * t)
   x2_acc = A * np.sin(omega * t)
   x3_acc = A * np.sin(omega * t)

   # Derivatives
   x1ddot = (1 / m1) * (-c1 * x1dot - k1 * x1 + k2 * (x2 - x1) + c2 * (x2dot - x1dot) + x1_acc)
   x2ddot = (1 / m2) * (-c2 * (x2dot - x1dot) - k2 * (x2 - x1) + k3 * (x3 - x2) + c3 * (x3dot - x2dot) + x2_acc)
   x3ddot = (1 / m3) * (-c3 * (x3dot - x2dot) - k3 * (x3 - x2) + x3_acc)

   return [x1dot, x2dot, x3dot, x1ddot, x2ddot, x3ddot]


# Initial conditions
y0 = [0, 0, 0, 0, 0, 0]

# Time points
t = np.linspace(0, 30, 3000)

# Solve system of equations
sol = odeint(equations, y0, t)

# Plot results
plt.plot(t, sol[:, 0], label='Floor 1')
plt.plot(t, sol[:, 1], label='Floor 2')
plt.plot(t, sol[:, 2], label='Floor 3')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.legend()
plt.show()
