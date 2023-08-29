# Now for some earthquake plotting:

import numpy as np
from scipy.integrate import quad

# Define the Boore-Atkinson PSD function
def S(omega):
   C1 = 2.5
   C2 = 4.5
   C3 = 1.25
   return C1/(1 + (omega/C2)**2) * np.exp(-C3*omega)

# Define the inverse Fourier transform integrand
def integrand(omega, x):
   return S(omega) * np.exp(1j*omega*x)/(1 + omega**2)

# Define the Fourier transform function
def G(x):
   integral = quad(integrand, -100, 100, args=(x,), epsrel=1e-6, limit=1000)
   return integral[0].real/(2*np.pi)

# Evaluate the Fourier transform at some x values
x_values = np.linspace(0, 10, 1000)
G_values = [G(x) for x in x_values]

# Plot the Fourier transform
import matplotlib.pyplot as plt
plt.plot(x_values, G_values)
plt.xlabel('x')
plt.ylabel('G(x)')
plt.show()

# The program is calculating and plotting the Fourier transform of the ground motion represented by the power spectral density (PSD) function given by the Boore-Atkinson model.
# The Fourier transform is a mathematical operation that decomposes a time-domain signal into its constituent frequencies. In the context of earthquake engineering, the Fourier transform is often used to analyze ground motion data and understand the frequency content of the motion.
# In this specific case, the program is evaluating the Fourier transform of the ground motion using the inverse Fourier transform formula, which involves integrating the PSD function over all frequencies. The Fourier transform is then plotted as a function of distance or position (x), which shows how the amplitude of the motion varies with frequency and distance.
# The plot produced by the program shows the Fourier transform of the ground motion as a function of distance or position (x) on the horizontal axis and amplitude (G(x)) on the vertical axis. The shape of the plot reveals the frequency content of the ground motion, with higher peaks indicating stronger amplitudes at those frequencies. The plot can be useful in earthquake engineering to analyze the response of structures to the ground motion, as different frequencies may excite different modes of vibration or resonance in a structure.
