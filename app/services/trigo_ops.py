import math
from fastapi import HTTPException

def sin_deg(x: float) -> float:
    try:
        return math.sin(x)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input for sin: {e}")

def cos_deg(x: float) -> float:
    try:
        return math.cos(x)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input for cos: {e}")

def tan_deg(x: float) -> float:
    try:
        return math.tan(x)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input for tan: {e}")

def to_radians(deg: float) -> float:
    try:
        return math.radians(deg)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid degrees: {e}")

def to_degrees(rad: float) -> float:
    try:
        return math.degrees(rad)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid radians: {e}")


def asin_func(x: float) -> float:
    if not -1 <= x <= 1:
        raise HTTPException(status_code=400, detail="asin input must be between -1 and 1")
    return math.asin(x)

def acos_func(x: float) -> float:
    if not -1 <= x <= 1:
        raise HTTPException(status_code=400, detail="acos input must be between -1 and 1")
    return math.acos(x)

def atan_func(x: float) -> float:
    return math.atan(x)

def sinh_func(x: float) -> float:
    return math.sinh(x)

def cosh_func(x: float) -> float:
    return math.cosh(x)

def tanh_func(x: float) -> float:
    return math.tanh(x)
