import numpy as np


def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # step 1: cal dot a, b
    a = np.asarray(a)
    b = np.asarray(b)
    dot_ab = np.dot(a, b)
    
    # step 2: cal L2
    norm2_a = np.linalg.norm(a)
    norm2_b = np.linalg.norm(b)
    
    # step 3: cal sim (validate when norm = 0)
    if norm2_a == 0 or norm2_b == 0:
        return 0.0
    
    return float(dot_ab / (norm2_a*norm2_b))

print(cosine_similarity([1,2,3], [2,4,6]))