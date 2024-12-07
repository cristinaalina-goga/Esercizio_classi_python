# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:17:50 2024

@author: bosca
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors



nomefile='COME HAI NOMINATO IL FILE AD ES:Nemo_6670.dat'


class readdf:
    
    def __init__(self,nomefile):
        
        self.nome=nomefile
        self.data = None
    
    
    def read_file(self):
        try:
            self.data=pd.read_csv(self.nome, sep=' ')
        except FileNotFoundError:
            print(f"Errore: Il file '{self.file_path}' non è stato trovato.")
        except pd.errors.EmptyDataError:
            print("Errore: Il file è vuoto.")
        except pd.errors.EmptyDataError:
            print("Errore: C'è un problema di formattazione con il file.")
    
    def show_head(self, n=5):
       """Mostra le prime n righe del DataFrame."""
       if self.data is not None:
           print(self.data.head(n))
       else:
           print("Errore: Il file non è stato ancora caricato.")
    
    

what=readdf(nomefile)
what.read_file()
    
dati=what.data

    




dati.groupby('età')['M_ass'].hist(alpha=0.5)

