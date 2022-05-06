# -*- coding: utf-8 -*-

import numpy as np
from scipy.sparse import csgraph

X = np.array([[0, 2, 7, 0, 0],
             [0, 0, 3, 8, 5],
             [0, 2, 0, 1, 0],
             [0, 0, 0, 0, 4],
             [0, 0, 0, 5, 0]])

print( X )
dist_matrix,Pred=csgraph.shortest_path(X, method='auto', directed=True,return_predecessors=True)
print(dist_matrix)
print(Pred+1)