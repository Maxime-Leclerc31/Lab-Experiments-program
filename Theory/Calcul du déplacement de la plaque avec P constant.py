
import numpy as np
import matplotlib.pyplot as plt

## Constants
Po = 101300  # Atmospheric pressure
Rho = 1000  # Density of water
g = 9.81  # Gravity

## Dimensions
ho = 0.55  # Water height at rest
L = 3  # Length of a PMMA plate
l = 0.6  # Width of a PMMA plate
e = 0.003  # Thickness of a PMMA plate
I = l * (e**3) / 12   # Moment of inertia of the plate
z = 0.05  # Height of the plate from the bottom

## Parameters
A = 0.05  # Wave amplitude (in m)
Lambda = 3.52  # Wavelength of the waves
k = 2 * np.pi / Lambda  # Wave number
w = 4.16  # Wave pulsation
E = 3300e6  # Young's modulus of the plate

## Problem constants
A1 = l * (Rho * g * e)  # Regular constant
C1 = -A1*L/2
C2 = A1*(L**2)/12

def u(x):
    return (l/(E*I)) * (A1*(x**4)/24 + C1*(x**3)/6 + C2*(x**2)/2)

Nbr_P = 5000  # Number of points used for resolution
X=[i*L/Nbr_P for i in range(Nbr_P)]
U = []

for i in range(Nbr_P):
    U.append(u(i*L/Nbr_P))

plt.plot(X,U)
print(max(U))
plt.xlabel('x in m')
plt.ylabel('Déplacement U en m')
plt.xlim(0, 3)
plt.ylim(0, 3)
plt.show()




