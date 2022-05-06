#problema 2 hewel.ochoa@utp.ac.pa
from scipy.sparse import csr_matrix
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree

rutas = np.array([[0,6,6,6,0,0,0,0,0,0,0],
                    [6,0,1,0,2,0,0,0,0,0,0],
                    [6,1,0,2,7,0,2,0,0,0,0],
                    [6,0,2,0,0,0,0,0,0,0,0],
                    [0,2,7,0,0,4,0,0,0,0,0],
                    [0,0,0,0,4,0,11,10,0,0,0,0],
                    [0,0,0,0,0,11,0,22,2,0,0,0],
                    [0,0,0,0,0,10,22,0,12,0,25,0],
                    [0,0,0,0,0,0,2,12,0,1,16,0],
                    [0,0,0,18,0,0,0,0,1,0,0,8],
                    [0,0,0,0,0,0,0,25,16,0,0,3],
                    [0,0,0,0,0,0,0,0,0,8,3,0]])
r = np.array(rutas, dtype=int)
ru = csr_matrix(r)
recorridos = minimum_spanning_tree(ru)
print(recorridos)
print(recorridos.toArray().astype(int))