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
X1_0 = 9.793
X2_0 = 9.992
X3_0 = 10.192
X4_0 = 10.391

X1_1 = 10.590
X2_1 = 10.789
X3_1 = 10.986
X4_1 = 11.184

X1_2 = 11.350
X2_2 = 11.549
X3_2 = 11.746
X4_2 = 11.944

# Columns numbers
C1 = 3
C2 = 1
C3 = 4
C4 = 2


# Getting the files names
f05_A03_x9793_run1 = r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x9793\f05\f05_A03_x9793_run1.csv"
f05_A03_x10590_run1 = r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10590\f05\f05_A03_x10590_run1.csv"
f05_A03_x10590_run1 = r"C:\Maxime\ECM\Stages\SSE\Recherche\19032025\x10286\f05\f05_A03_x10286_run1.csv"


## Getting the csv to a good format for reading values
# Reading the csv
df_0 = pd.read_csv(f05_A03_x9793_run1, header=None)
df_1 = pd.read_csv(f05_A03_x10590_run1, header=None)
df_2 = pd.read_csv(f05_A03_x10286_run1, header=None)

#Getting average of values up to line 20
AV1_0 = df_0.iloc[:,C1].mean()
AV2_0 = df_0.iloc[:,C2].mean()
AV3_0 = df_0.iloc[:,C3].mean()
AV4_0 = df_0.iloc[:,C4].mean()

AV1_1 = df_1.iloc[:,C1].mean()
AV2_1 = df_1.iloc[:,C2].mean()
AV3_1 = df_1.iloc[:,C3].mean()
AV4_1 = df_1.iloc[:,C4].mean()

AV1_2 = df_2.iloc[:,C1].mean()
AV2_2 = df_2.iloc[:,C2].mean()
AV3_2 = df_2.iloc[:,C3].mean()
AV4_2 = df_2.iloc[:,C4].mean()


# Plotting the Averages
X = [X1_1,X1_2,X2_0,X2_1,X2_2,X3_0,X3_1,X3_2,X4_0,X4_1,X4_2]
AVG = [AV1_0,AV2_0,AV3_0,AV4_0,AV1_1,AV2_1,AV3_1,AV4_1,AV1_2,AV2_2,AV3_2,AV4_2]
plt.plot(X,AVG,"red")
plt.title("Average height depending on the position")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

