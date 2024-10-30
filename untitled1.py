# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:44:56 2024

@author: bosca
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors


bins=10

binsarr=np.linspace(0,bins-1,bins)

dati=pd.read_csv('HRdati.dat', sep=' ')



plt.scatter(dati['b-y'],dati['M_ass'],s=1)
plt.gca().invert_yaxis()

numero=np.linspace(0,1,bins)

distanza=(dati['age_parent'].max()-dati['age_parent'].min())/bins

dati['età']=pd.cut(dati['age_parent'],bins=bins,labels=numero)

norm = mcolors.Normalize(vmin=dati['age_parent'].min(), vmax=dati['age_parent'].max())

plt.scatter(dati['b-y'],dati['M_ass'],s=1,c=dati['età'],cmap='plasma')

plt.legend( [f'{i}-{i+np.round(distanza,3)}' for i in np.round(binsarr*distanza,1)], title="Gruppi di Età",loc='upper right')


plt.show()


dati.groupby('età')['M_ass'].hist(alpha=0.5)

plt.legend( [f'{i}-{i+np.round(distanza,3)}' for i in np.round(binsarr*distanza,1)], title="Gruppi di Età",loc='upper right')



print(dati['età'])
