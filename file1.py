# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:44:56 2024

@author: bosca
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors


...............
io creo la classe
...........................

#chiamerò il dataframe 'dati'  colonna 1='M_ass' ,colonna  2='b-y', colonna 3='age_parent'



............................
        Nbins = 10
        bins = pd.cut(dati['age_parent'], bins=Nbins)

        plt.figure(figsize=(10, 6))
        cmap = plt.cm.get_cmap('viridis', Nbins)  
        marker_size = 10  
        for i, (bin_value, group) in enumerate(df.groupby(bins)):
            color = cmap(i / (Nbins - 1))  # Calcola i colori dalla colormap
            plt.scatter(group['b-y'], group['M_ass'], 
                        label=f'Bin: {bin_value.left:.2f} to {bin_value.right:.2f}', 
                        color=color, s=marker_size, alpha=0.8)

        plt.ylim(9, -4)
        plt.xlabel('b-y')
        plt.ylabel('$M_V$')
        plt.title('Scatter plot of b-y vs $M_V$')
        plt.legend(loc='best', title='Age bins', fontsize='6')
        plt.show()

......................
faccio isogramma
......................
