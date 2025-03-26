import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

# Paramètres
E = 3300e6  # Module d'Young (N/m²)
l = 0.5  # Largeur de la plaque (m)
e = 0.003  # Épaisseur (m)
L = 3  # Longueur de la plaque (m)
I = (L * e**3) / 12  # Moment d'inertie
z = 0.005
A = 0.05
Po = 101300
Rho = 1000
g = 9.1v8
ho = 0.55
Lambda = 3.52
k = 2*np.pi/Lambda
w = 4.16
t=20

# Fonction de charge q(x)
def q(x):
    return Po + Rho*g*(ho + A*np.cos(k*x-w*t) - z) - 106131.42544336956
# Équation différentielle pour solve_bvp
def beam_eq(x, y):
    w, dw, d2w, d3w = y
    d4w = q(x) / (E * I)  # Équation de la flexion EI w'''' = q(x)
    return np.array([dw, d2w, d3w, d4w])

# Conditions aux limites : w(0) = w(L) = w'(0) = w'(L) = 0
def bc(ya, yb):
    return np.array([ya[0], ya[1], yb[0], yb[1]])

# Discrétisation
x = np.linspace(0, L, 100)
y_init = np.zeros((4, x.size))  # Devine une solution initiale (0 partout)

# Résolution numérique
sol = solve_bvp(beam_eq, bc, x, y_init)

# Extraction de la solution
w_sol = sol.sol(x)[0]  # Déplacement de la plaque

# Affichage
plt.plot(x, w_sol * 1000, label="Déformation de la plaque (mm)")
plt.xlabel("Position x (m)")
plt.ylabel("Déplacement w (mm)")
plt.legend()
plt.grid()
plt.show()
