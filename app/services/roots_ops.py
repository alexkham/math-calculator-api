from fastapi import HTTPException
import math

def square_root(x: float) -> float:
    if x < 0:
        raise HTTPException(status_code=400, detail="Cannot take square root of a negative number.")
    return math.sqrt(x)

def cube_root(x: float) -> float:
    return math.copysign(abs(x) ** (1/3), x)  # Handles negative numbers correctly

def nth_root(x: float, n: int) -> float:
    if n == 0:
        raise HTTPException(status_code=400, detail="Cannot take zeroth root.")
    if x < 0 and n % 2 == 0:
        raise HTTPException(status_code=400, detail="Even root of negative number is not real.")
    return math.copysign(abs(x) ** (1/n), x)

def rational_power(x: float, m: float, n: float) -> float:
    if n == 0:
        raise HTTPException(status_code=400, detail="Exponent denominator (n) cannot be zero.")
    exponent = m / n
    if x < 0 and not exponent.is_integer():
        raise HTTPException(status_code=400, detail="Cannot raise negative base to fractional power.")
    return x ** exponent
