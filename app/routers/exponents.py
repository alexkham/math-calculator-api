from fastapi import APIRouter, Query
from app.services.exponent_ops import (
    square,
    cube,
    power,
    rational_power,
    inverse,
    negative_power
)

router = APIRouter()

@router.get("/square")
def square_endpoint(x: float = Query(...)):
    return {"operation": "square", "result": square(x)}

@router.get("/cube")
def cube_endpoint(x: float = Query(...)):
    return {"operation": "cube", "result": cube(x)}

@router.get("/power")
def power_endpoint(
    x: float = Query(...),
    n: float = Query(...)
):
    return {"operation": f"{x}^{n}", "result": power(x, n)}

@router.get("/fractional")
def fractional_power_endpoint(
    x: float = Query(...),
    m: float = Query(...),
    n: float = Query(...)
):
    return {"operation": f"{x}^({m}/{n})", "result": rational_power(x, m, n)}

@router.get("/inverse")
def inverse_endpoint(x: float = Query(...)):
    return {"operation": "x^-1", "result": inverse(x)}

@router.get("/negative")
def negative_power_endpoint(
    x: float = Query(...),
    n: float = Query(...)
):
    return {"operation": f"{x}^-{n}", "result": negative_power(x, n)}
