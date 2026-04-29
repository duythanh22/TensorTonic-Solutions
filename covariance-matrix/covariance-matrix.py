import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    matrix = np.asarray(X)

    if matrix.ndim != 2:
        return None

    m, n = matrix.shape
    if m < 2:
        return None

    mean_matrix  = np.mean(matrix, axis=0)
    matrix_center = matrix - mean_matrix

    cov_matrix = matrix_center.T @ matrix_center
    cov_matrix = cov_matrix / (m-1)
    return cov_matrix
    pass