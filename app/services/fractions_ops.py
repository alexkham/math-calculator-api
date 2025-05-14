from fractions import Fraction
from fastapi import HTTPException

def validate_denominator(d: int):
    if d == 0:
        raise HTTPException(status_code=400, detail="Denominator cannot be zero.")

def to_decimal(n: int, d: int) -> float:
    validate_denominator(d)
    return float(Fraction(n, d))

def from_decimal(decimal: float) -> str:
    return str(Fraction(decimal).limit_denominator())

def add_fractions(n1: int, d1: int, n2: int, d2: int) -> str:
    validate_denominator(d1)
    validate_denominator(d2)
    return str(Fraction(n1, d1) + Fraction(n2, d2))

def subtract_fractions(n1: int, d1: int, n2: int, d2: int) -> str:
    validate_denominator(d1)
    validate_denominator(d2)
    return str(Fraction(n1, d1) - Fraction(n2, d2))

def multiply_fractions(n1: int, d1: int, n2: int, d2: int) -> str:
    validate_denominator(d1)
    validate_denominator(d2)
    return str(Fraction(n1, d1) * Fraction(n2, d2))

def divide_fractions(n1: int, d1: int, n2: int, d2: int) -> str:
    validate_denominator(d1)
    validate_denominator(d2)
    if n2 == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero fraction.")
    return str(Fraction(n1, d1) / Fraction(n2, d2))

def simplify_fraction(n: int, d: int) -> str:
    validate_denominator(d)
    return str(Fraction(n, d))

def improper_to_mixed(n: int, d: int) -> dict:
    validate_denominator(d)
    frac = Fraction(n, d)
    sign = -1 if frac < 0 else 1
    whole = abs(frac.numerator) // frac.denominator
    remainder = abs(frac.numerator) % frac.denominator
    return {
        "whole": sign * whole,
        "numerator": remainder,
        "denominator": frac.denominator
    }

def mixed_to_improper(whole: int, n: int, d: int) -> str:
    validate_denominator(d)
    sign = -1 if whole < 0 else 1
    numerator = abs(whole) * d + n
    return str(Fraction(sign * numerator, d))
