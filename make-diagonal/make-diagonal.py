import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    v = np.asarray(v)
    n = len(v)

    matrix_zero = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i == j:
                matrix_zero[i][j] = v[i]
    
    # matrix_diag = np.diag(v)
    
    return matrix_zero
