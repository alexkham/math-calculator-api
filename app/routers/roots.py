from fastapi import APIRouter, Query
from app.services.roots_ops import (
    square_root,
    cube_root,
    nth_root,
    rational_power
)

router = APIRouter()

@router.get("/square")
# @router.get(
#     "/square",
#     summary="Calculate Square Root",
#     description="Returns the positive square root of a non-negative number using math.sqrt()."
# )
def get_square_root(x: float = Query(..., description="Number to square root")):
    return {"operation": "square_root", "result": square_root(x)}

@router.get("/cube")
def get_cube_root(x: float = Query(..., description="Number to cube root")):
    return {"operation": "cube_root", "result": cube_root(x)}

@router.get("/nth")
def get_nth_root(
    x: float = Query(..., description="Value to extract root from"),
    n: int = Query(..., description="Root degree (e.g. 4 for 4th root)")
):
    return {"operation": f"{n}th_root", "result": nth_root(x, n)}

@router.get("/rational")
def rational_exponent(
    x: float = Query(..., description="Base number"),
    m: float = Query(..., description="Numerator of exponent"),
    n: float = Query(..., description="Denominator of exponent")
):
    return {
        "operation": f"{x}^({m}/{n})",
        "result": rational_power(x, m, n)
    }
