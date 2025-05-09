from fastapi import APIRouter, Query
from app.services.complex_ops import (
    add_complex,
    subtract_complex,
    multiply_complex,
    divide_complex
)

router = APIRouter()

@router.get("/add")
def complex_add(
    a_real: float = Query(...), a_imag: float = Query(...),
    b_real: float = Query(...), b_imag: float = Query(...)
):
    result = add_complex(a_real, a_imag, b_real, b_imag)
    return {
        "operation": "add",
        "real": result.real,
        "imag": result.imag
    }

@router.get("/subtract")
def complex_subtract(
    a_real: float = Query(...), a_imag: float = Query(...),
    b_real: float = Query(...), b_imag: float = Query(...)
):
    result = subtract_complex(a_real, a_imag, b_real, b_imag)
    return {
        "operation": "subtract",
        "real": result.real,
        "imag": result.imag
    }

@router.get("/multiply")
def complex_multiply(
    a_real: float = Query(...), a_imag: float = Query(...),
    b_real: float = Query(...), b_imag: float = Query(...)
):
    result = multiply_complex(a_real, a_imag, b_real, b_imag)
    return {
        "operation": "multiply",
        "real": result.real,
        "imag": result.imag
    }

@router.get("/divide")
def complex_divide(
    a_real: float = Query(...), a_imag: float = Query(...),
    b_real: float = Query(...), b_imag: float = Query(...)
):
    try:
        result = divide_complex(a_real, a_imag, b_real, b_imag)
        return {
            "operation": "divide",
            "real": result.real,
            "imag": result.imag
        }
    except ValueError as e:
        return {"error": str(e)}
