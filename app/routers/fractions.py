from fastapi import APIRouter, Query
from app.services.fractions_ops import (
    to_decimal,
    from_decimal,
    add_fractions,
    subtract_fractions,
    multiply_fractions,
    divide_fractions,
    simplify_fraction,
    improper_to_mixed,
    mixed_to_improper
)

router = APIRouter()

@router.get("/to-decimal")
def convert_to_decimal(numerator: int = Query(...), denominator: int = Query(...)):
    return {"result": to_decimal(numerator, denominator)}

@router.get("/from-decimal")
def convert_from_decimal(decimal: float = Query(...)):
    return {"result": from_decimal(decimal)}

@router.get("/add")
def add(n1: int = Query(...), d1: int = Query(...), n2: int = Query(...), d2: int = Query(...)):
    return {"result": add_fractions(n1, d1, n2, d2)}

@router.get("/subtract")
def subtract(n1: int = Query(...), d1: int = Query(...), n2: int = Query(...), d2: int = Query(...)):
    return {"result": subtract_fractions(n1, d1, n2, d2)}

@router.get("/multiply")
def multiply(n1: int = Query(...), d1: int = Query(...), n2: int = Query(...), d2: int = Query(...)):
    return {"result": multiply_fractions(n1, d1, n2, d2)}

@router.get("/divide")
def divide(n1: int = Query(...), d1: int = Query(...), n2: int = Query(...), d2: int = Query(...)):
    return {"result": divide_fractions(n1, d1, n2, d2)}

@router.get("/simplify")
def simplify(numerator: int = Query(...), denominator: int = Query(...)):
    return {"result": simplify_fraction(numerator, denominator)}

@router.get("/to-mixed")
def to_mixed(numerator: int = Query(...), denominator: int = Query(...)):
    return {"result": improper_to_mixed(numerator, denominator)}

@router.get("/from-mixed")
def from_mixed(whole: int = Query(...), numerator: int = Query(...), denominator: int = Query(...)):
    return {"result": mixed_to_improper(whole, numerator, denominator)}
