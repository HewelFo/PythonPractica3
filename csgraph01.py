import numpy as np
from scipy.sparse import csgraph
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import csgraph_from_dense

print(csgraph.__all__)

#
print("")

G_dense = np.array([[0, 114, 99],[114, 0, 0], [99, 0, 0]])
print(G_dense)

#G_masked = np.ma.masked_values(G_dense, 0)
#print(G_masked)

G_sparse = csr_matrix(G_dense)
print(G_sparse)
print("")

#G2_data = np.array([[np.inf, 2,      0     ],[2,      np.inf, np.inf],[0,      np.inf, np.inf]])
#print(G2_data)
#
#G2_masked = np.ma.masked_invalid(G2_data)
#print(G2_masked)
## G2_sparse = csr_matrix(G2_data) would give the wrong result
#
#G2_sparse = csgraph_from_dense(G2_data, null_value=np.inf)
#print(G2_sparse.data)
