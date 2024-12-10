import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors

nomefile='Nemo_6670.dat'
Nbins=30

class readdf:

    def __init__(self,nomefile):

        self.nome=nomefile
        self.data = None


    def read_file(self):
        try:
            self.data=pd.read_csv(self.nome, sep=' ',header=0)
        except FileNotFoundError:
            print(f"Errore: Il file '{self.file_path}' non è stato trovato.")
        except pd.errors.EmptyDataError:
            print("Errore: Il file è vuoto.")
        except pd.errors.ParserError: #qui avevi rimesso l'eccezione di sopra
            print("Errore: C'è un problema di formattazione con il file.")
        except Exception:
            print("Some other exception")


    def show_head(self, n=5):
           """Mostra le prime n righe del DataFrame."""
           if self.data is not None:
               print(self.data.head(n))
           else:
               print("Errore: Il file non è stato ancora caricato.")
    

    def colormap_plot(self, x: str='b-y', y: str="M_ass",
                      z: str='age_parent',Nbins: int=30, map: str='viridis'):

        self.data['età']= pd.cut(self.data[z],bins=Nbins)#usa pd.cut e aggiungi una colonna
                                                         #che chiami 'età' con il numero di
                                                         #intervallo al dataframe 'dati'
        plt.figure(figsize=(10, 6))
        cmap = plt.cm.get_cmap(map, Nbins)               #fai grafico con colormap
        marker_size = 10
        for i, (bin_value, group) in enumerate(self.data.groupby('età')):
            color = cmap(i / (Nbins - 1))
            plt.scatter(group[x], group[y],
                label=f'Bin: {bin_value.left:.2f} to {bin_value.right:.2f}',
                color=color, s=marker_size, alpha=0.8)

        plt.ylim(9, -4) #plt.xlabel(x) plt.ylabel(y) plt.title('Scatter plot of b-y vs $M_V$')
        plt.legend(loc='best', title=z+'bins', fontsize='6')
        plt.show()

what=readdf(nomefile)
what.read_file()

dati=what.data
numero=np.linspace(0,1,Nbins)
