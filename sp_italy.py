# problema 1 hewel.ochoa@utp.ac.pa
import numpy as np
import pandas as pd
from time import time
import networkx as nx
from scipy.sparse import csgraph

data = pd.read_csv('italia.csv', header=0, index_col=0)
print(data)
# toma el timepo de ejecucion para luego calcularlo
timeS = time()
# calula la ruta mas corta por el algoritmo de dijkta
sloveD = csgraph.shortest_path(np.array(data), method='D')
timeD = time()
# calcula la ruta mas corta por el algoritmo de floid warshall
sloveFW = csgraph.shortest_path(np.array(data), method='FW')
timeFW = time()
# se sacan los tiempos de ejecucion de cada algoritmo
Tpas_warshall = timeS - timeFW
Tpas_Dijkta = timeS - timeD
# se evalua cual es el menor tiempo de ejecucion
if Tpas_Dijkta < Tpas_warshall:
    print("el algoritmo de warshall tiene mayor tiempo de ejecucion")
else:
    print("el algoritmo de dijkta tiene mayor tiempo de ejecucion")


print(sloveD)
print(sloveFW)
#creacion de lo grafos con networkx
ge = nx.Graph(np.array(data))
gdi = nx.DiGraph(np.array(data))
#dibuja el grafo utilizando networkx
nx.draw(ge)

 
