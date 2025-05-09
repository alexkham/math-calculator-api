import math
from fastapi import HTTPException

def log_natural(x: float) -> float:
    if x <= 0:
        raise HTTPException(status_code=400, detail="ln(x): x must be > 0")
    return math.log(x)

def log_base10(x: float) -> float:
    if x <= 0:
        raise HTTPException(status_code=400, detail="log10(x): x must be > 0")
    return math.log10(x)

def log_base2(x: float) -> float:
    if x <= 0:
        raise HTTPException(status_code=400, detail="log2(x): x must be > 0")
    return math.log(x, 2)

def log_custom_base(x: float, base: float) -> float:
    if x <= 0:
        raise HTTPException(status_code=400, detail="log_a(x): x must be > 0")
    if base <= 0 or base == 1:
        raise HTTPException(status_code=400, detail="log_a(x): base must be > 0 and ≠ 1")
    return math.log(x, base)

def natural_exponent(x: float) -> float:
    return math.exp(x)
