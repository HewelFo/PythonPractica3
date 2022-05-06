
import numpy as np
from scipy.sparse import csgraph

X = np.array([[0, 1, 0, 0, 0, 0],
             [1, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 1, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0]])

print( X )
n_components, labels = csgraph.connected_components(X, directed=True,connection='strong')
print (n_components)
print (labels)

Y = np.array([[0, 2, 7, 0, 0],
             [0, 0, 3, 8, 5],
             [0, 2, 0, 1, 0],
             [0, 0, 0, 0, 4],
             [0, 0, 0, 5, 0]])

print( Y )
n_components, labels = csgraph.connected_components(Y, directed=True,connection='strong')
print (n_components)
print (labels)

