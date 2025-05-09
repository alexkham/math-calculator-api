from fastapi import APIRouter, Query
from app.services.log_ops import (
    log_natural,
    log_base10,
    log_base2,
    log_custom_base,
    natural_exponent
)

router = APIRouter()

@router.get("/natural")
def natural_log(x: float = Query(..., description="x > 0")):
    return {"operation": "ln(x)", "result": log_natural(x)}

@router.get("/base10")
def log_base_10(x: float = Query(..., description="x > 0")):
    return {"operation": "log10(x)", "result": log_base10(x)}

@router.get("/base2")
def log_base_2(x: float = Query(..., description="x > 0")):
    return {"operation": "log2(x)", "result": log_base2(x)}

@router.get("/base")
def log_custom(
    x: float = Query(..., description="x > 0"),
    base: float = Query(..., description="base > 0 and ≠ 1")
):
    return {"operation": f"log_{base}(x)", "result": log_custom_base(x, base)}

@router.get("/natural-exponent")
def natural_exp(x: float = Query(..., description="e^x")):
    return {"operation": "e^x", "result": natural_exponent(x)}
