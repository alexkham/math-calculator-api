from fastapi import APIRouter, Query
from app.services.trigo_ops import (
    sin_deg, cos_deg, tan_deg, to_radians, to_degrees,
    asin_func, acos_func, atan_func, sinh_func, cosh_func, tanh_func
)

router = APIRouter()

@router.get("/sin")
def sine(x: float = Query(..., description="Angle in radians")):
    return {"operation": "sin", "result": sin_deg(x)}

@router.get("/cos")
def cosine(x: float = Query(..., description="Angle in radians")):
    return {"operation": "cos", "result": cos_deg(x)}

@router.get("/tan")
def tangent(x: float = Query(..., description="Angle in radians")):
    return {"operation": "tan", "result": tan_deg(x)}

@router.get("/radians")
def radians(deg: float = Query(..., description="Degrees to convert")):
    return {"operation": "to_radians", "result": to_radians(deg)}

@router.get("/degrees")
def degrees(rad: float = Query(..., description="Radians to convert")):
    return {"operation": "to_degrees", "result": to_degrees(rad)}


@router.get("/asin")
def arcsin(x: float = Query(..., description="Value between -1 and 1")):
    return {"operation": "asin", "result": asin_func(x)}

@router.get("/acos")
def arccos(x: float = Query(..., description="Value between -1 and 1")):
    return {"operation": "acos", "result": acos_func(x)}

@router.get("/atan")
def arctan(x: float = Query(...)):
    return {"operation": "atan", "result": atan_func(x)}

@router.get("/sinh")
def sinh(x: float = Query(...)):
    return {"operation": "sinh", "result": sinh_func(x)}

@router.get("/cosh")
def cosh(x: float = Query(...)):
    return {"operation": "cosh", "result": cosh_func(x)}

@router.get("/tanh")
def tanh(x: float = Query(...)):
    return {"operation": "tanh", "result": tanh_func(x)}