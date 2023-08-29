# Now I have the position of two floors in the x direction of the x position, where both equations of motion are of the form mi*xi’’+ci*xi’+ki*xi=Asin(x)+Bcos(x):

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the system of differential equations
def model(y, t, m1, m2, k1, k2, k3, c1, c2, c3, A, B):
   x1, x1_dot, x2, x2_dot = y

   # Define the external force as Asin(x) + Bcos(x)
   G = A * np.sin(x1) + B * np.cos(x1)

   # Define the system of differential equations
   f = [x1_dot,
        (-k1 * x1 + k2 * (x2 - x1) - c1 * x1_dot + c2 * (x2_dot - x1_dot) - m1 * G) / m1,
        x2_dot,
        (-k2 * (x2 - x1) + k3 * (0 - x2) - c2 * (x2_dot - x1_dot) + c3 * (-x2_dot)) / m2]

   return f

# Define the initial conditions and time range
y0 = [0, 0, 0, 0]  # initial conditions
t = np.linspace(0, 100, 1000)  # time range

# Define the parameters for the system
m1 = 1  # mass of the first floor
m2 = 1  # mass of the second floor
k1 = 2  # spring constant between the first floor and the ground
k2 = 3  # spring constant between the first and second floor
k3 = 2  # spring constant between the second floor and the ground
c1 = 0.1  # damping coefficient for the first floor
c2 = 0.2  # damping coefficient for the first and second floor
c3 = 0.1  # damping coefficient for the second floor
A = 1  # amplitude of the external force's sine term
B = 2  # amplitude of the external force's cosine term

# Solve the system of differential equations
sol = odeint(model, y0, t, args=(m1, m2, k1, k2, k3, c1, c2, c3, A, B))

# Plot the results
plt.plot(t, sol[:, 0], label='x1')
plt.plot(t, sol[:, 2], label='x2')
plt.legend(loc='best')
plt.xlabel('time')
plt.ylabel('position')
plt.title('Positions of floors over time')
plt.show()
