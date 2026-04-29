import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    matrix = np.asarray(X)

    if matrix.ndim !=2:
        return None

    N, D = matrix.shape

    if N < 2:
        return None

    mean_matrix = np.mean(matrix, axis=0)
    center_matrix = matrix - mean_matrix
    return (center_matrix.T @ center_matrix) / (N-1)