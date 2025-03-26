import numpy as np
import matplotlib.pyplot as plt


Po = 101300 # P atmosphérique
Rho = 1000 # Rho de l'eau
g = 9.81 # pesenteur
ho = 0.55 # hauteur d'eau au repos
A = 0.05 # amplitude des vagues (en m)
Lambda = 3.52 # longueur d'onde des vagues
k = 2*np.pi/Lambda # nombre d'onde
w = 4.16 # pulsation des vagues
L = 3 # longueur d'une plaque de PMMA
l = 0.5 # Largeur d'une plaque de PMMA
e = 0.003 # Epaisseur d'une plaque de pMMA
I = l*(e**3)/12 # Moment d'inertie de la plaque
z = 0.05 # Hauteur de la plaque par rapport au fond
Nbr_P = 5000 # Nombre de points utilisés pour la résolution
E=3300e6 # Module d'Young de la plaque
t=20 # t auquel on effectue les calculs
Phmin=106131.42544336956 # Pression minimale subie pour le haut
Pbmin=106180.47544336955 # Pression minimale subie pour le bas
P_z=l*(Rho*g*e) # constante régulière


def a(x):
    return P_z * (x**3)/6

def b(x):
    return -(l*g*Rho*A/(k**3)) * np.sin(k*x-w*t)

def a2(x):
    return P_z * (x**4)/24

def b2(x):
    return (l*g*Rho*A/(k**4)) * np.cos(k*x-w*t)

C3 = -(l*g*Rho*A/(k**3)) * np.sin(w*t)
C4 = - b2(0)
C1 = (12/(L**3)) * (C4 + C3*L + a2(L) + b2(L) + (L/2) * (-C3 - a(L) - b(L)))
C2 = (1/L) * (-C3 - a(L) - b(L) - ((L**2)/2) * C1)


def P(x,z,t):
    return Po + Rho*g*(ho + A*np.cos(k*x-w*t) - z)

def u(x,t):
    return (-l/(E*I)) *(a2(x) + b2(x) + C1*((x**3)/6) + C2*((x**2)/2) + C3*x + C4)



X=[i*L/Nbr_P for i in range(Nbr_P)]
Preh = []
Preb = []
Pred = []
U = []
zh = z + e/2
zb = z - e/2

for i in range(Nbr_P):
    Preh.append(P(i*L/Nbr_P,zh,t)-Phmin)
    Preb.append(P(i*L/Nbr_P,zb,t)-Pbmin)
    U.append(u(i*L/Nbr_P,t))

print(u(0,t),u(L,t))
print(E*I)
print(C1,C2,C3,C4)


##plt.plot(X,Preh,"red")
##plt.plot(X,Preb,"blue")
##plt.plot(X,Pred,"orange")
plt.plot(X,U)
plt.xlabel('x in m')
plt.ylabel('Déplacement U en m')
plt.show()



