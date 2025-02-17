import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('FallA.csv',delimiter=';')

df.info()

viktig_data = df.iloc[:1000,10:15]
viktig_data.info()


plt.figure()
plt.plot(viktig_data.iloc[:,0],viktig_data.iloc[:,1],label='$ \phi $(t)')
plt.plot(viktig_data.iloc[:,0],viktig_data.iloc[:,2],label='$ \theta $(t)')
plt.plot(viktig_data.iloc[:,0],viktig_data.iloc[:,3],label='$q_1$(t)')
plt.plot(viktig_data.iloc[:,0],viktig_data.iloc[:,4],label='$q_2$(t)')
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.legend()
plt.show()