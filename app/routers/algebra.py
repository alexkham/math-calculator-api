from fastapi import APIRouter, Query
from app.services.algebra_ops import solve_quadratic

router = APIRouter()

@router.get("/solve_quadratic")
def solve_quadratic_route(a: float = Query(...), b: float = Query(...), c: float = Query(...)):
    return {"operation": "solve_quadratic", "roots": solve_quadratic(a, b, c)}
