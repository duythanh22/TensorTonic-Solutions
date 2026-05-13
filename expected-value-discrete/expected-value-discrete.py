import numpy as np


def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.asarray(x)
    p = np.asarray(p)
    if x.shape != p.shape:
        raise ValueError('Shape mismatch: expected {}, got {}'.format(x.shape, p.shape))
    sum_p = np.sum(p)
    if not np.allclose(sum_p, 1):
        raise ValueError('Sum of probabilities does not equal 1')
    return float(np.sum(x * p))
