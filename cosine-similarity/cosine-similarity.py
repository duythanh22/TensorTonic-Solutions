import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """

    # step 1
    a = np.asarray(a)
    b = np.asarray(b)

    dot_ab = np.dot(a, b)

    # step 2
    norm2_a = np.linalg.norm(a, ord=2)
    norm2_b = np.linalg.norm(b, ord=2)
    
    if norm2_a == 0 or norm2_b == 0:
        return 0.0
    # step 3
    return (dot_ab / (norm2_a*norm2_b)).astype(np.float32)