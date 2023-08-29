For two floor in both the y and x directions and just simple with Mx’’+kx=0 and My’’+ky=0:

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the system of differential equations
def equations(state, t, m1, m2, k1, k2, k3):
   x1, x1_dot, x2, x2_dot, x3, x3_dot, y1, y1_dot, y2, y2_dot, y3, y3_dot = state
   x1_dotdot = (-k1 * x1 + k2 * (x2 - x1)) / m1
   x2_dotdot = (-k2 * (x2 - x1) + k3 * (x3 - x2)) / m2
   y1_dotdot = (-k1 * y1 + k2 * (y2 - y1)) / m1
   y2_dotdot = (-k2 * (y2 - y1) + k3 * (y3 - y2)) / m2
   return [x1_dot, x1_dotdot, x2_dot, x2_dotdot, x3_dot, 0, y1_dot, y1_dotdot, y2_dot, y2_dotdot, y3_dot, 0]

# Define initial conditions and parameters
initial_state = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0]  # x1, x1', x2, x2', x3, x3', y1, y1', y2, y2', y3, y3'
t = np.linspace(0, 10, 1000)
m1 = 1
m2 = 2
k1 = 1
k2 = 2
k3 = 3

# Solve the system of differential equations
sol = odeint(equations, initial_state, t, args=(m1, m2, k1, k2, k3))

# Extract the solutions for x(t) and y(t) from the state vector
x1_sol = sol[:, 0]
x2_sol = sol[:, 2]
x3_sol = sol[:, 4]
y1_sol = sol[:, 6]
y2_sol = sol[:, 8]
y3_sol = sol[:, 10]

# Plot the solutions for x(t) and y(t)
plt.plot(t, x1_sol, label='x1')
plt.plot(t, x2_sol, label='x2')
plt.plot(t, x3_sol, label='x3')
plt.plot(t, y1_sol, label='y1')
plt.plot(t, y2_sol, label='y2')
plt.plot(t, y3_sol, label='y3')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Position')
plt.show()
