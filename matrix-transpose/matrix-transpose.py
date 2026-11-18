import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    m = len(A)
    n = len(A[0])

    ans = np.zeros((n, m), dtype=int)

    for i in range(m):
        for j in range(n):
            ans[j][i] = A[i][j];
    return ans
    
    pass
