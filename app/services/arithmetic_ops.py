from fastapi import HTTPException
import math

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    return a / b

def modulo(a: int, b: int) -> int:
    if b == 0:
        raise HTTPException(status_code=400, detail="Modulo by zero is not allowed.")
    return a % b

def floor_divide(a: int, b: int) -> int:
    if b == 0:
        raise HTTPException(status_code=400, detail="Floor division by zero is not allowed.")
    return a // b

def gcd(a: int, b: int) -> int:
    return math.gcd(a, b)

def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)
