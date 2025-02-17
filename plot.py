import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

labellist = ('$ \phi $(t)',r'$ \theta $(t)','$q_1$(t)','$q_2$(t)')

df = pd.read_csv('FallA.csv',delimiter=';')

viktig_data = df.iloc[:1000,10:15]

plt.figure()
for i in range(1,5):
    plt.plot(viktig_data.iloc[:,0],
        viktig_data.iloc[:,i]-viktig_data.iloc[:,i].mean(),
        label=labellist[i-1])
plt.xlabel('Tid (s)')
plt.ylabel('Vinkel (rad)')
plt.title('Fall A')
plt.legend()
plt.savefig('plot_A.pdf',bbox_inches='tight')
plt.show()


df = pd.read_csv('FallB.csv',delimiter=';')

viktig_data = df.iloc[:1000,6:11]
viktig_data.info()


plt.figure()
for i in range(1,5):
    plt.plot(viktig_data.iloc[:,0],
        viktig_data.iloc[:,i]-viktig_data.iloc[:,i].mean(),
        label=labellist[i-1])
plt.xlabel('Tid (s)')
plt.ylabel('Vinkel (rad)')
plt.title('Fall B')
plt.legend()
plt.savefig('plot_B.pdf',bbox_inches='tight')
plt.show()

df = pd.read_csv('FallC.csv',delimiter=';')

viktig_data = df.iloc[:1000,10:15]

plt.figure()
for i in range(1,5):
    plt.plot(viktig_data.iloc[:,0],
        viktig_data.iloc[:,i]-viktig_data.iloc[:,i].mean(),
        label=labellist[i-1])
plt.xlabel('Tid (s)')
plt.ylabel('Vinkel (rad)')
plt.title('Fall C')
plt.legend()
plt.savefig('plot_C.pdf',bbox_inches='tight')

plt.show()