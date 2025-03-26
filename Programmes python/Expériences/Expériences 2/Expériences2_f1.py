import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv


## Parameters
g = 9.81 #m.s-2
H = 0.4 #m Height of the water
v = np.sqrt(g*H) #Speed of waves
f = 1 #Hz frequency
Ttot = 30 #s periode time of experiment
P = Ttot*f #Number of periods
L=7500

#Position of probe 1 _ Position of tray (0,1,2)
X1_1 = 10.186 
X2_1 = 10.691
X3_1 = 11.111
X4_1 = 11.564

X1_0 = X1_1 - 0.1
X2_0 = X2_1 - 0.1
X3_0 = X3_1 - 0.1
X4_0 = X4_1 - 0.1

X1_2 = X1_1 + 0.1
X2_2 = X2_1 + 0.1
X3_2 = X3_1 + 0.1
X4_2 = X4_1 + 0.1


# Column in sheets
C1 = 2
C2 = 1
C3 = 4
C4 = 3

def temps_ligne(T):
    return int((T*7500)/30)

# Calculating times of arrival and departure of wave x for each probe
V10tp1e_0 = temps_ligne(X1_0/v + 10 * 1/f)
V10tp1s_0 = temps_ligne(X1_0/v + 11 * 1/f)

V10tp2e_0 = temps_ligne(X2_0/v + 10 * 1/f)
V10tp2s_0 = temps_ligne(X2_0/v + 11 * 1/f)

V10tp3e_0 = temps_ligne(X3_0/v + 10 * 1/f)
V10tp3s_0 = temps_ligne(X3_0/v + 11 * 1/f)

V10tp4e_0 = temps_ligne(X4_0/v + 10 * 1/f)
V10tp4s_0 = temps_ligne(X4_0/v + 11 * 1/f)


V10tp1e_1 = temps_ligne(X1_1/v + 10 * 1/f)
V10tp1s_1 = temps_ligne(X1_1/v + 11 * 1/f)

V10tp2e_1 = temps_ligne(X2_1/v + 10 * 1/f)
V10tp2s_1 = temps_ligne(X2_1/v + 11 * 1/f)

V10tp3e_1 = temps_ligne(X3_1/v + 10 * 1/f)
V10tp3s_1 = temps_ligne(X3_1/v + 11 * 1/f)

V10tp4e_1 = temps_ligne(X4_1/v + 10 * 1/f)
V10tp4s_1 = temps_ligne(X4_1/v + 11 * 1/f)


V10tp1e_2 = temps_ligne(X1_2/v + 10 * 1/f)
V10tp1s_2 = temps_ligne(X1_2/v + 11 * 1/f)

V10tp2e_2 = temps_ligne(X2_2/v + 10 * 1/f)
V10tp2s_2 = temps_ligne(X2_2/v + 11 * 1/f)

V10tp3e_2 = temps_ligne(X3_2/v + 10 * 1/f)
V10tp3s_2 = temps_ligne(X3_2/v + 11 * 1/f)

V10tp4e_2 = temps_ligne(X4_2/v + 10 * 1/f)
V10tp4s_2 = temps_ligne(X4_2/v + 11 * 1/f)

# Getting the files names
f1_A03_x10086_run1 = r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10086\f1\f1_A03_x10086_run1.csv"
f1_A03_x10186_run1 = r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10186\f1\f1_A03_x10186_run1.csv"
f1_A03_x10286_run1 = r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10286\f1\f1_A03_x10286_run1.csv"
f07_A03_x10086_run1 = r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10086\f07\f07_A03_x10086_run1.csv"
f07_A03_x10186_run1 = r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10186\f07\f07_A03_x10186_run1.csv"
f07_A03_x10286_run1 = r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10286\f07\f07_A03_x10286_run1.csv"
f05_A03_x10086_run1 = r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10086\f05\f05_A03_x10086_run1.csv"
f05_A03_x10186_run1 = r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10186\f05\f05_A03_x10186_run1.csv"
f05_A03_x10286_run1 = r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10286\f05\f05_A03_x10286_run1.csv"


## Getting the csv to a good format for reading values
# Reading the csv
df_0 = pd.read_csv(f1_A03_x10086_run1, header=None)
df_1 = pd.read_csv(f1_A03_x10186_run1, header=None)
df_2 = pd.read_csv(f1_A03_x10286_run1, header=None)

#Getting average of values up to line 20
line_limit = 200

AV1_0 = df_0.iloc[:line_limit,C1].mean()
AV2_0 = df_0.iloc[:line_limit,C2].mean()
AV3_0 = df_0.iloc[:line_limit,C3].mean()
AV4_0 = df_0.iloc[:line_limit,C4].mean()

AV1_1 = df_1.iloc[:line_limit,C1].mean()
AV2_1 = df_1.iloc[:line_limit,C2].mean()
AV3_1 = df_1.iloc[:line_limit,C3].mean()
AV4_1 = df_1.iloc[:line_limit,C4].mean()

AV1_2 = df_2.iloc[:line_limit,C1].mean()
AV2_2 = df_2.iloc[:line_limit,C2].mean()
AV3_2 = df_2.iloc[:line_limit,C3].mean()
AV4_2 = df_2.iloc[:line_limit,C4].mean()

# Getting the real amplitude of waves
df_0.iloc[:, C1] = AV1_0 - df_0.iloc[:, C1]
df_0.iloc[:, C2] = AV2_0 - df_0.iloc[:, C2]
df_0.iloc[:, C3] = AV3_0 - df_0.iloc[:, C3]
df_0.iloc[:, C4] = AV4_0 - df_0.iloc[:, C4]

df_1.iloc[:, C1] = - AV1_1 + df_1.iloc[:, C1]
df_1.iloc[:, C2] = - AV2_1 + df_1.iloc[:, C2]
df_1.iloc[:, C3] = - AV3_1 + df_1.iloc[:, C3]
df_1.iloc[:, C4] = - AV4_1 + df_1.iloc[:, C4]

df_2.iloc[:, C1] = AV1_2 - df_2.iloc[:, C1]
df_2.iloc[:, C2] = AV2_2 - df_2.iloc[:, C2]
df_2.iloc[:, C3] = AV3_2 - df_2.iloc[:, C3]
df_2.iloc[:, C4] = AV4_2 - df_2.iloc[:, C4]

# Saving the modifications
df_0.to_csv(r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10086\f1\f1_A03_x10086_run1_modified.csv", index=False)
df_1.to_csv(r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10186\f1\f1_A03_x10186_run1_modified.csv", index=False)
df_2.to_csv(r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10286\f1\f1_A03_x10286_run1_modified.csv", index=False)


# Getting the new file name
f1_A03_x10086_run1_modified = r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10086\f1\f1_A03_x10086_run1_modified.csv"
f1_A03_x10186_run1_modified = r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10186\f1\f1_A03_x10186_run1_modified.csv"
f1_A03_x10286_run1_modified = r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10286\f1\f1_A03_x10286_run1_modified.csv"


# Getting wave x for each probe
df1_0 = pd.read_csv(f1_A03_x10086_run1_modified, skiprows=V10tp1e_0, nrows=V10tp1s_0-V10tp1e_0)
P1_0 = df1_0.iloc[:, C1].tolist()

df2_0 = pd.read_csv(f1_A03_x10086_run1_modified, skiprows=V10tp2e_0, nrows=V10tp2s_0-V10tp2e_0)
P2_0 = df2_0.iloc[:, C2].tolist()

df3_0 = pd.read_csv(f1_A03_x10086_run1_modified, skiprows=V10tp3e_0, nrows=V10tp3s_0-V10tp3e_0)
P3_0 = df3_0.iloc[:, C3].tolist()

df4_0 = pd.read_csv(f1_A03_x10086_run1_modified, skiprows=V10tp4e_0, nrows=V10tp4s_0-V10tp4e_0)
P4_0 = df4_0.iloc[:, C4].tolist()


df1_1 = pd.read_csv(f1_A03_x10186_run1_modified, skiprows=V10tp1e_1, nrows=V10tp1s_1-V10tp1e_1)
P1_1 = df1_1.iloc[:, C1].tolist()

df2_1 = pd.read_csv(f1_A03_x10186_run1_modified, skiprows=V10tp2e_1, nrows=V10tp2s_1-V10tp2e_1)
P2_1 = df2_1.iloc[:, C2].tolist()

df3_1 = pd.read_csv(f1_A03_x10186_run1_modified, skiprows=V10tp3e_1, nrows=V10tp3s_1-V10tp3e_1)
P3_1 = df3_1.iloc[:, C3].tolist()

df4_1 = pd.read_csv(f1_A03_x10186_run1_modified, skiprows=V10tp4e_1, nrows=V10tp4s_1-V10tp4e_1)
P4_1 = df4_1.iloc[:, C4].tolist()


df1_2 = pd.read_csv(f1_A03_x10286_run1_modified, skiprows=V10tp1e_2, nrows=V10tp1s_2-V10tp1e_2)
P1_2 = df1_2.iloc[:, C1].tolist()

df2_2 = pd.read_csv(f1_A03_x10286_run1_modified, skiprows=V10tp2e_2, nrows=V10tp2s_2-V10tp2e_2)
P2_2 = df2_2.iloc[:, C2].tolist()

df3_2 = pd.read_csv(f1_A03_x10286_run1_modified, skiprows=V10tp3e_2, nrows=V10tp3s_2-V10tp3e_2)
P3_2 = df3_2.iloc[:, C3].tolist()

df4_2 = pd.read_csv(f1_A03_x10286_run1_modified, skiprows=V10tp4e_2, nrows=V10tp4s_2-V10tp4e_2)
P4_2 = df4_2.iloc[:, C4].tolist()

# Calculating Alpha
MAP1_0 = max(abs(x) for x in P1_0)
MAP2_0 = max(abs(x) for x in P2_0)
MAP3_0 = max(abs(x) for x in P3_0)
MAP4_0 = max(abs(x) for x in P4_0)

MAP1_1 = max(abs(x) for x in P1_1)
MAP2_1 = max(abs(x) for x in P2_1)
MAP3_1 = max(abs(x) for x in P3_1)
MAP4_1 = max(abs(x) for x in P4_1)

MAP1_2 = max(abs(x) for x in P1_2)
MAP2_2 = max(abs(x) for x in P2_2)
MAP3_2 = max(abs(x) for x in P3_2)
MAP4_2 = max(abs(x) for x in P4_2)

AlphaP2_0=(np.log(MAP1_0)-np.log(MAP2_0))/(X2_0-X1_0)
AlphaP3_0=(np.log(MAP1_0)-np.log(MAP3_0))/(X3_0-X1_0)
AlphaP4_0=(np.log(MAP1_0)-np.log(MAP4_0))/(X4_0-X1_0)

AlphaP1_1=(np.log(MAP1_0)-np.log(MAP1_1))/(X1_1-X1_0)
AlphaP2_1=(np.log(MAP1_0)-np.log(MAP2_1))/(X2_1-X1_0)
AlphaP3_1=(np.log(MAP1_0)-np.log(MAP3_1))/(X3_1-X1_0)
AlphaP4_1=(np.log(MAP1_0)-np.log(MAP4_1))/(X4_1-X1_0)

AlphaP1_2=(np.log(MAP1_0)-np.log(MAP1_2))/(X1_2-X1_0)
AlphaP2_2=(np.log(MAP1_0)-np.log(MAP2_2))/(X2_2-X1_0)
AlphaP3_2=(np.log(MAP1_0)-np.log(MAP3_2))/(X3_2-X1_0)
AlphaP4_2=(np.log(MAP1_0)-np.log(MAP4_2))/(X4_2-X1_0)

Alpha=[AlphaP1_1,AlphaP1_2,AlphaP2_0,AlphaP2_1,AlphaP2_2,AlphaP3_0,AlphaP3_1,AlphaP3_2,AlphaP4_0,AlphaP4_1,AlphaP4_2]

# Plotting the waves
T=np.linspace(0,30,len(P1_0))
plt.plot(T,P1_0,"mediumblue")
plt.plot(T,P1_1,"darkslateblue")
plt.plot(T,P1_2,"blueviolet")
plt.plot(T,P2_0,"mediumorchid")
plt.plot(T,P2_1,"purple")
plt.plot(T,P2_2,"magenta")
plt.plot(T,P3_0,"hotpink")
plt.plot(T,P3_1,"pink")
plt.plot(T,P3_2,"blanchedalmond")
plt.plot(T,P4_0,"burlywood")
plt.plot(T,P4_1,"peru")
plt.plot(T,P4_2,"chocolate")
plt.title("Wave 10 at different postions")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Plotting Alpha
X=[X1_1,X1_2,X2_0,X2_1,X2_2,X3_0,X3_1,X3_2,X4_0,X4_1,X4_2]
plt.plot(X,Alpha,"red")
plt.title("Alpha in fonction of the postion")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Plotting Amplitudes max
X=[X1_0,X1_1,X1_2,X2_0,X2_1,X2_2,X3_0,X3_1,X3_2,X4_0,X4_1,X4_2]
MaxAmp = [MAP1_0, MAP1_1, MAP1_1, MAP2_0, MAP2_1, MAP2_2, MAP3_0, MAP3_1, MAP3_2, MAP4_0, MAP4_1, MAP4_2]
plt.plot(X,MaxAmp,"red")
plt.title("Max amplitude in fonction of the postion")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Plotting Amplitudes max in percentage
X=[X1_0,X1_1,X1_2,X2_0,X2_1,X2_2,X3_0,X3_1,X3_2,X4_0,X4_1,X4_2]
MaxAmp = [MAP1_0, MAP1_1, MAP1_1, MAP2_0, MAP2_1, MAP2_2, MAP3_0, MAP3_1, MAP3_2, MAP4_0, MAP4_1, MAP4_2]
MaxAmpP = [MaxAmp[x]/MAP1_0 for x in range(len(MaxAmp))]
plt.plot(X,MaxAmpP,"red")
plt.title("Max amplitude in fonction of the postion")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
