from fastapi import APIRouter, Query, HTTPException
from app.services.arithmetic_ops import (
    add, subtract, multiply, divide,
    modulo, floor_divide, gcd, lcm
)

router = APIRouter()

@router.get("/add")
def add_route(a: float = Query(...), b: float = Query(...)):
    return {"operation": "add", "result": add(a, b)}

@router.get("/subtract")
def subtract_route(a: float = Query(...), b: float = Query(...)):
    return {"operation": "subtract", "result": subtract(a, b)}

@router.get("/multiply")
def multiply_route(a: float = Query(...), b: float = Query(...)):
    return {"operation": "multiply", "result": multiply(a, b)}

@router.get("/divide")
def divide_route(a: float = Query(...), b: float = Query(...)):
    return {"operation": "divide", "result": divide(a, b)}

@router.get("/modulo")
def modulo_route(a: int = Query(...), b: int = Query(...)):
    return {"operation": "modulo", "result": modulo(a, b)}

@router.get("/floor_divide")
def floor_divide_route(a: int = Query(...), b: int = Query(...)):
    return {"operation": "floor_divide", "result": floor_divide(a, b)}

@router.get("/gcd")
def gcd_route(a: int = Query(...), b: int = Query(...)):
    return {"operation": "gcd", "result": gcd(a, b)}

@router.get("/lcm")
def lcm_route(a: int = Query(...), b: int = Query(...)):
    return {"operation": "lcm", "result": lcm(a, b)}
