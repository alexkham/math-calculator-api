from fastapi import APIRouter, Query
from app.services.sequences_ops import (
    arithmetic_sequence,
    geometric_sequence,
    fibonacci_sequence,
    factorial_number,
    prime_sequence,
    triangular_sequence,
    is_prime
)

router = APIRouter()

@router.get("/arithmetic")
def get_arithmetic_sequence(
    start: float = Query(...),
    step: float = Query(...),
    count: int = Query(..., gt=0)
):
    return {"sequence": arithmetic_sequence(start, step, count)}

@router.get("/geometric")
def get_geometric_sequence(
    start: float = Query(...),
    ratio: float = Query(...),
    count: int = Query(..., gt=0)
):
    return {"sequence": geometric_sequence(start, ratio, count)}

@router.get("/fibonacci")
def get_fibonacci_sequence(count: int = Query(..., gt=0)):
    return {"sequence": fibonacci_sequence(count)}

@router.get("/factorial")
def get_factorial(n: int = Query(..., ge=0)):
    return {"result": factorial_number(n)}

@router.get("/primes")
def get_prime_sequence(count: int = Query(..., gt=0)):
    return {"sequence": prime_sequence(count)}


@router.get("/triangular")
def get_triangular_sequence(count: int = Query(..., gt=0)):
    return {"sequence": triangular_sequence(count)}

@router.get("/is-prime")
def check_is_prime(n: int = Query(..., gt=1)):
    return {"number": n, "is_prime": is_prime(n)}