from fastapi import HTTPException

def square(x: float) -> float:
    return x ** 2

def cube(x: float) -> float:
    return x ** 3

def power(x: float, n: float) -> float:
    return x ** n

def rational_power(x: float, m: float, n: float) -> float:
    if n == 0:
        raise HTTPException(status_code=400, detail="Denominator (n) cannot be zero.")
    exponent = m / n
    if x < 0 and not exponent.is_integer():
        raise HTTPException(status_code=400, detail="Cannot raise negative base to fractional power.")
    return x ** exponent

def inverse(x: float) -> float:
    if x == 0:
        raise HTTPException(status_code=400, detail="Cannot take inverse of zero.")
    return 1 / x

def negative_power(x: float, n: float) -> float:
    if x == 0:
        raise HTTPException(status_code=400, detail="Cannot raise zero to a negative power.")
    return x ** (-n)
