import math
from fastapi import HTTPException

def factorial(n: int) -> int:
    return math.factorial(n)

def permutations(n: int, r: int) -> int:
    if r > n:
        raise HTTPException(status_code=400, detail="r must be ≤ n")
    return math.perm(n, r)

def combinations(n: int, r: int) -> int:
    if r > n:
        raise HTTPException(status_code=400, detail="r must be ≤ n")
    return math.comb(n, r)

def multichoose(n: int, r: int) -> int:
    return math.comb(n + r - 1, r)
