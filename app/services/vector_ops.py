def add_vectors(v1: list[float], v2: list[float]) -> list[float]:
    if len(v1) != len(v2):
        raise ValueError("Vectors must be the same length")
    return [a + b for a, b in zip(v1, v2)]

def subtract_vectors(v1: list[float], v2: list[float]) -> list[float]:
    if len(v1) != len(v2):
        raise ValueError("Vectors must be the same length")
    return [a - b for a, b in zip(v1, v2)]

def dot_product(v1: list[float], v2: list[float]) -> float:
    if len(v1) != len(v2):
        raise ValueError("Vectors must be the same length")
    return sum(a * b for a, b in zip(v1, v2))

def cross_product(v1: list[float], v2: list[float]) -> list[float]:
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Cross product requires 3D vectors")
    return [
        v1[1]*v2[2] - v1[2]*v2[1],
        v1[2]*v2[0] - v1[0]*v2[2],
        v1[0]*v2[1] - v1[1]*v2[0]
    ]
