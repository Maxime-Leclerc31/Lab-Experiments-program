import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv


## Parameters
g = 9.81 #m.s-2
H = 0.4 #m Height of the water
v = np.sqrt(g*H) #Speed of waves
f = 0.5 #Hz frequency
Ttot = 30 #s periode time of experiment
P = Ttot*f #Number of periods
L=7500

#Position of probe 1 _ Position of tray (0,1,2)
X1 = 6.641
X2 = 10.186
X3 = 11.571
X4 = 13.418


# Column in sheets
C1 = 1
C2 = 2
C3 = 3
C4 = 4

def temps_ligne(T):
    return int((T*7500)/30)

# Calculating times of arrival and departure of wave x for each probe
V6tp1e_f05 = temps_ligne(X1/v + 6 * 1/f)
V6tp1s_f05 = temps_ligne(X1/v + 7 * 1/f)

V6tp2e_f05 = temps_ligne(X2/v + 6 * 1/f)
V6tp2s_f05 = temps_ligne(X2/v + 7 * 1/f)

V6tp3e_f05 = temps_ligne(X3/v + 6 * 1/f)
V6tp3s_f05 = temps_ligne(X3/v + 7 * 1/f)

V6tp4e_f05 = temps_ligne(X4/v + 6 * 1/f)
V6tp4s_f05 = temps_ligne(X4/v + 7 * 1/f)



# Getting the files names
f05_A03_beach_run1 = r"C:\Maxime\ECM\Stages\SSE\Recherche\17032025\beach\f05\f05_A03_beach_run1.csv"
f05_A03_run1 = r"C:\Maxime\ECM\Stages\SSE\Recherche\17032025\No_beach\f05\f05_A03_run2.csv"


## Getting the csv to a good format for reading values
# Reading the csv
df_b = pd.read_csv(f05_A03_beach_run1, header=None)
df_nb = pd.read_csv(f05_A03_run1, header=None)


#Getting average of values up to line 200
line_limit = 200

AV1_b = df_b.iloc[:line_limit,C1].mean()
AV2_b = df_b.iloc[:line_limit,C2].mean()
AV3_b = df_b.iloc[:line_limit,C3].mean()
AV4_b = df_b.iloc[:line_limit,C4].mean()

AV1_nb = df_nb.iloc[:line_limit,C1].mean()
AV2_nb = df_nb.iloc[:line_limit,C2].mean()
AV3_nb = df_nb.iloc[:line_limit,C3].mean()
AV4_nb = df_nb.iloc[:line_limit,C4].mean()

# Getting the real amplitude of waves
df_b.iloc[:, C1] = AV1_b - df_b.iloc[:, C1]
df_b.iloc[:, C2] = AV2_b - df_b.iloc[:, C2]
df_b.iloc[:, C3] = AV3_b - df_b.iloc[:, C3]
df_b.iloc[:, C4] = AV4_b - df_b.iloc[:, C4]

df_nb.iloc[:, C1] = - AV1_nb + df_nb.iloc[:, C1]
df_nb.iloc[:, C2] = - AV2_nb + df_nb.iloc[:, C2]
df_nb.iloc[:, C3] = - AV3_nb + df_nb.iloc[:, C3]
df_nb.iloc[:, C4] = - AV4_nb + df_nb.iloc[:, C4]


# Saving the modifications
df_b.to_csv(r"C:\Maxime\ECM\Stages\SSE\Recherche\17032025\beach\f05\f05_A03_beach_run1_modified.csv", index=False)
df_nb.to_csv(r"C:\Maxime\ECM\Stages\SSE\Recherche\17032025\No_beach\f05\f05_A03_run2_modified.csv", index=False)


# Getting the new file name
f05_A03_beach_run1_modified = r"C:\Maxime\ECM\Stages\SSE\Recherche\17032025\beach\f05\f05_A03_beach_run1_modified.csv"
f05_A03_No_beach_run1_modified = r"C:\Maxime\ECM\Stages\SSE\Recherche\17032025\No_beach\f05\f05_A03_run2_modified.csv"


# Getting wave x for each probe
df05_b = pd.read_csv(f05_A03_beach_run1_modified, skiprows=V6tp1e_f05, nrows=V6tp1s_f05-V6tp1e_f05)
P1_b = df05_b.iloc[:, C1].tolist()

df2_b = pd.read_csv(f05_A03_beach_run1_modified, skiprows=V6tp2e_f05, nrows=V6tp2s_f05-V6tp2e_f05)
P2_b = df2_b.iloc[:, C2].tolist()

df3_b = pd.read_csv(f05_A03_beach_run1_modified, skiprows=V6tp3e_f05, nrows=V6tp3s_f05-V6tp3e_f05)
P3_b = df3_b.iloc[:, C3].tolist()

df4_b = pd.read_csv(f05_A03_beach_run1_modified, skiprows=V6tp4e_f05, nrows=V6tp4s_f05-V6tp4e_f05)
P4_b = df4_b.iloc[:, C4].tolist()


df05_nb = pd.read_csv(f05_A03_No_beach_run1_modified, skiprows=V6tp1e_f05, nrows=V6tp1s_f05-V6tp1e_f05)
P1_nb = df05_nb.iloc[:, C1].tolist()

df2_nb = pd.read_csv(f05_A03_No_beach_run1_modified, skiprows=V6tp2e_f05, nrows=V6tp2s_f05-V6tp2e_f05)
P2_nb = df2_nb.iloc[:, C2].tolist()

df3_nb = pd.read_csv(f05_A03_No_beach_run1_modified, skiprows=V6tp3e_f05, nrows=V6tp3s_f05-V6tp3e_f05)
P3_nb = df3_nb.iloc[:, C3].tolist()

df4_nb = pd.read_csv(f05_A03_No_beach_run1_modified, skiprows=V6tp4e_f05, nrows=V6tp4s_f05-V6tp4e_f05)
P4_nb = df4_nb.iloc[:, C4].tolist()


# Calculating Alpha
MAP1_b = max(abs(x) for x in P1_b)
MAP2_b = max(abs(x) for x in P2_b)
MAP3_b = max(abs(x) for x in P3_b)
MAP4_b = max(abs(x) for x in P4_b)

MAP1_nb = max(abs(x) for x in P1_nb)
MAP2_nb = max(abs(x) for x in P2_nb)
MAP3_nb = max(abs(x) for x in P3_nb)
MAP4_nb = max(abs(x) for x in P4_nb)

##
##AlphaP2_b=(np.log(MAP1_b)-np.log(MAP2_b))/X2
##AlphaP3_b=(np.log(MAP1_b)-np.log(MAP3_b))/X3
##AlphaP4_b=(np.log(MAP1_b)-np.log(MAP4_b))/X4
##
##AlphaP1_nb=(np.log(MAP1_b)-np.log(MAP1_nb))/X1
##AlphaP2_nb=(np.log(MAP1_b)-np.log(MAP2_nb))/X2
##AlphaP3_nb=(np.log(MAP1_b)-np.log(MAP3_nb))/X3
##AlphaP4_nb=(np.log(MAP1_b)-np.log(MAP4_nb))/X4
##
##
##Alpha=[AlphaP1_nb,AlphaP1_2,AlphaP2_b,AlphaP2_nb,AlphaP2_2,AlphaP3_b,AlphaP3_nb,AlphaP3_2,AlphaP4_b,AlphaP4_nb,AlphaP4_2]

# Plotting the waves
T=np.linspace(0,30,len(P1_b))
plt.plot(T,P1_nb,"darkslateblue")
plt.plot(T,P2_nb,"purple")
plt.plot(T,P3_nb,"pink")
plt.plot(T,P4_nb,"peru")
plt.title("Wave 6 at different postions, no beach")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim([-0.015, 0.015])
plt.show()

plt.plot(T,P1_b,"mediumblue")
plt.plot(T,P2_b,"mediumorchid")
plt.plot(T,P3_b,"hotpink")
plt.plot(T,P4_b,"burlywood")
plt.title("Wave 6 at different postions, beach")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim([-0.015, 0.015])

plt.show()

### Plotting Alpha
##X=[X1_nb,X1_2,X2_b,X2_nb,X2_2,X3_b,X3_nb,X3_2,X4_b,X4_nb,X4_2]
##plt.plot(X,Alpha,"red")
##plt.title("Alpha in fonction of the postion")
##plt.xlabel("x")
##plt.ylabel("y")
##plt.show()

# Plotting Amplitudes max
X=[X1,X2,X3,X4]
MaxAmp_b = [MAP1_b, MAP2_b, MAP3_b, MAP4_b]
MaxAmp_nb = [MAP1_nb, MAP2_nb, MAP3_nb, MAP4_nb]
plt.plot(X,MaxAmp_b,"red")
plt.title("Max amplitude in fonction of the postion with beach")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim([0, 0.015])
plt.show()

plt.plot(X,MaxAmp_nb,"red")
plt.title("Max amplitude in fonction of the postion without beach")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim([0, 0.015])
plt.show()


plt.plot(X,MaxAmp_nb,"red")
plt.plot(X,MaxAmp_b,"green")
plt.title("Max amplitude in fonction of the postion with and without beach")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim([0, 0.015])

plt.show()

# Plotting Amplitudes max in percentage
X=[X1,X2,X3,X4]
MaxAmp_b_P = [MaxAmp_b[x]/MAP1_b for x in range(len(MaxAmp_b))]
MaxAmp_nb_P = [MaxAmp_nb[x]/MAP1_nb for x in range(len(MaxAmp_b))]
plt.plot(X,MaxAmp_nb_P,"red")
plt.plot(X,MaxAmp_b_P,"green")
plt.title("Max amplitude in fonction of the postion")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim([0, 1.2])
plt.show()
