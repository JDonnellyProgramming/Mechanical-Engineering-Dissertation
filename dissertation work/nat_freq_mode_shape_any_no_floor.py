# The Vibraton Absorber Tuning frequency for 2 floors:

import numpy as np

# Input values for k, m, and c
k = float(input("Enter value of k: "))
m = float(input("Enter value of m: "))
c = float(input("Enter value of c: "))

# Calculate natural frequency
omega_n = np.sqrt(k / m)

# Calculate damping ratio
zeta = c / (2 * np.sqrt(k * m))

# Calculate tuning frequency
f_tune = omega_n / (2 * np.pi * np.sqrt(1 - zeta**2))

# Print result
print(f"The tuning frequency is: {f_tune:.2f} Hz")
