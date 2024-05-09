# Example: Simulate spacecraft orbit around Europa
import numpy as np
import matplotlib.pyplot as plt

# Define gravitational constant (m^3/kg/s^2)
G = 6.67430e-11

# Define Europa's semi-major axis (m) and eccentricity
a_europa = 671100000  # semi-major axis of Europa's orbit around Jupiter (m)
e_europa = 0.0094      # eccentricity of Europa's orbit

# Define time array (seconds)
t = np.linspace(0, 2*np.pi*np.sqrt(a_europa**3 / G), 1000)

# Calculate spacecraft position in orbit using Kepler's equation
r = a_europa * (1 - e_europa**2) / (1 + e_europa * np.cos(t))

# Plot spacecraft orbit around Europa
plt.figure(figsize=(8, 6))
plt.plot(r * np.cos(t), r * np.sin(t), label='Spacecraft Orbit')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Spacecraft Orbit around Europa')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.show()
