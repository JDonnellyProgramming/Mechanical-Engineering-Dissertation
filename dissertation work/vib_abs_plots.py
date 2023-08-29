# Vibration absorber plots for with or without one on two floors as simplified models:

import numpy as np
import matplotlib.pyplot as plt

# SDOF parameters
m = 1.0      # mass in kg
k = 10.0     # stiffness in N/m
c = 0.1      # damping coefficient in Ns/m

# Natural frequency and damping ratio of the SDOF system
wn = np.sqrt(k / m)
zeta = c / (2 * np.sqrt(k * m))

# Tuned vibration absorber parameters
m1 = 0.2     # mass in kg
k1 = k       # stiffness in N/m
c1 = 2 * zeta * np.sqrt(m1 * k1)    # damping coefficient in Ns/m
r = 0.5      # tuning ratio

# Natural frequency and damping ratio of the absorber
wn1 = np.sqrt(k1 / m1)
zeta1 = c1 / (2 * np.sqrt(k1 * m1))

# Transfer function of the SDOF system
def H(w):
   return 1 / (-w**2 * m + 1j * w * c + k)

# Transfer function of the absorber
def Ha(w):
   return r * H(w) * m / (m1 * (w**2 - wn1**2 + 1j * 2 * zeta1 * wn1 * w))

# Frequency range
w = np.logspace(-1, 2, num=1000)

# Magnitude and phase of the transfer functions
H_mag = abs(H(w))
H_phase = np.angle(H(w), deg=True)
Ha_mag = abs(Ha(w))
Ha_phase = np.angle(Ha(w), deg=True)

# Plotting
plt.subplot(211)
plt.semilogx(w, H_mag, label='SDOF system')
plt.semilogx(w, Ha_mag, label='Absorber')
plt.ylabel('Magnitude')
plt.grid()
plt.legend()

plt.subplot(212)
plt.semilogx(w, H_phase, label='SDOF system')
plt.semilogx(w, Ha_phase, label='Absorber')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Phase [deg]')
plt.grid()
plt.legend()

plt.show()

