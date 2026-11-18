import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    x_arr = np.asarray(x, dtype=float)
    result = 1.0/(1.0 + np.exp(-x_arr))

    if isinstance(x, (int, float)):
        return float(result);
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    return result
    
    pass