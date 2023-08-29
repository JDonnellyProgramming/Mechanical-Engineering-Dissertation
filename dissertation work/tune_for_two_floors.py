# displacement for two floors including vertical motion too

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def equations(w, t, p):
   x1, x1d, y1, y1d, x2, x2d, y2, y2d = w
   m1, m2, k1, k2, c1, c2, A, B = p

   # equations for floors 1 and 2 in the x-direction
   f1x = k1 * x1 + (-k1 - k2) * x2 + A * np.sin(y1) + B * np.cos(y1)
   f2x = -k1 * x1 + (k1 + k2) * x2 + A * np.sin(y2) + B * np.cos(y2)

   # equations for floors 1 and 2 in the y-direction
   f1y = k1 * y1 + (-k1 - k2) * y2 + A * np.sin(x1) + B * np.cos(x1)
   f2y = -k1 * y1 + (k1 + k2) * y2 + A * np.sin(x2) + B * np.cos(x2)

   # derivatives
   x1dd = -c1 * x1d / m1 + f1x / m1
   x2dd = -c2 * x2d / m2 + f2x / m2
   y1dd = -c1 * y1d / m1 + f1y / m1
   y2dd = -c2 * y2d / m2 + f2y / m2

   return x1d, x1dd, y1d, y1dd, x2d, x2dd, y2d, y2dd


# initial conditions
w0 = [0, 0, 0, 0, 0, 0, 0, 0]
# time points
t = np.linspace(0, 10, 1000)

# parameters
m1 = 2
m2 = 1
k1 = 20
k2 = 10
c1 = 0.5
c2 = 0.2
A = 1
B = 1

# solve ODE system
sol = odeint(equations, w0, t, args=((m1, m2, k1, k2, c1, c2, A, B),))

# plot results
plt.plot(t, sol[:, 0], label='Floor 1 in x')
plt.plot(t, sol[:, 1], label='Floor 1 in x dot')
plt.plot(t, sol[:, 2], label='Floor 1 in y')
plt.plot(t, sol[:, 3], label='Floor 1 in y dot')
plt.plot(t, sol[:, 4], label='Floor 2 in x')
plt.plot(t, sol[:, 5], label='Floor 2 in x dot')
plt.plot(t, sol[:, 6], label='Floor 2 in y')
plt.plot(t, sol[:, 7], label='Floor 2 in y dot')
plt.xlabel('time')
plt.ylabel('displacement')
plt.legend()
plt.show()
