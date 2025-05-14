import numpy as np
from fastapi import HTTPException

def to_numpy(matrix):
    try:
        return np.array(matrix, dtype=float)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid matrix format.")

def matrix_add(m1, m2):
    a = to_numpy(m1)
    b = to_numpy(m2)
    if a.shape != b.shape:
        raise HTTPException(status_code=400, detail="Matrix shapes must match for addition.")
    return (a + b).tolist()

def matrix_multiply(m1, m2):
    a = to_numpy(m1)
    b = to_numpy(m2)
    try:
        return (a @ b).tolist()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid matrix dimensions for multiplication.")

def matrix_transpose(matrix):
    a = to_numpy(matrix)
    return a.T.tolist()

def matrix_determinant(matrix):
    a = to_numpy(matrix)
    if a.shape[0] != a.shape[1]:
        raise HTTPException(status_code=400, detail="Matrix must be square for determinant.")
    return float(np.linalg.det(a))

def matrix_inverse(matrix):
    a = to_numpy(matrix)
    if a.shape[0] != a.shape[1]:
        raise HTTPException(status_code=400, detail="Matrix must be square for inversion.")
    try:
        return np.linalg.inv(a).tolist()
    except np.linalg.LinAlgError:
        raise HTTPException(status_code=400, detail="Matrix is not invertible.")
