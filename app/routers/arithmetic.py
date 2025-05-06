from fastapi import APIRouter, Query
from app.services.arithmetic_ops import add, subtract, multiply, divide

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
