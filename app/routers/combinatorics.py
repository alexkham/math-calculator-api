from fastapi import APIRouter, Query
from app.services.combinatorics_ops import (
    factorial,
    permutations,
    combinations,
    multichoose
)

router = APIRouter()

@router.get("/factorial")
def get_factorial(n: int = Query(..., ge=0)):
    return {"operation": f"{n}!", "result": factorial(n)}

@router.get("/permutations")
def get_permutations(n: int = Query(..., ge=0), r: int = Query(..., ge=0)):
    return {"operation": f"P({n},{r})", "result": permutations(n, r)}

@router.get("/combinations")
def get_combinations(n: int = Query(..., ge=0), r: int = Query(..., ge=0)):
    return {"operation": f"C({n},{r})", "result": combinations(n, r)}

@router.get("/multichoose")
def get_multichoose(n: int = Query(..., ge=0), r: int = Query(..., ge=0)):
    return {"operation": f"MC({n},{r})", "result": multichoose(n, r)}
