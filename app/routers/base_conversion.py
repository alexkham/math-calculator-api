from fastapi import APIRouter, Query
from app.services.base_conversion_ops import (
    binary_to_decimal, binary_to_octal, binary_to_hex,
    decimal_to_binary, decimal_to_octal, decimal_to_hex,
    octal_to_binary, octal_to_decimal, octal_to_hex,
    hex_to_binary, hex_to_decimal, hex_to_octal
)

router = APIRouter()

# BINARY
@router.get("/binary/decimal")
def binary_to_dec(value: str = Query(...)):
    return {"result": binary_to_decimal(value)}

@router.get("/binary/octal")
def binary_to_oct(value: str = Query(...)):
    return {"result": binary_to_octal(value)}

@router.get("/binary/hex")
def binary_to_hx(value: str = Query(...)):
    return {"result": binary_to_hex(value)}

# DECIMAL
@router.get("/decimal/binary")
def decimal_to_bin(value: int = Query(...)):
    return {"result": decimal_to_binary(value)}

@router.get("/decimal/octal")
def decimal_to_oct(value: int = Query(...)):
    return {"result": decimal_to_octal(value)}

@router.get("/decimal/hex")
def decimal_to_hx(value: int = Query(...)):
    return {"result": decimal_to_hex(value)}

# OCTAL
@router.get("/octal/binary")
def octal_to_bin(value: str = Query(...)):
    return {"result": octal_to_binary(value)}

@router.get("/octal/decimal")
def octal_to_dec(value: str = Query(...)):
    return {"result": octal_to_decimal(value)}

@router.get("/octal/hex")
def octal_to_hx(value: str = Query(...)):
    return {"result": octal_to_hex(value)}

# HEX
@router.get("/hex/binary")
def hex_to_bin(value: str = Query(...)):
    return {"result": hex_to_binary(value)}

@router.get("/hex/decimal")
def hex_to_dec(value: str = Query(...)):
    return {"result": hex_to_decimal(value)}

@router.get("/hex/octal")
def hex_to_oct(value: str = Query(...)):
    return {"result": hex_to_octal(value)}
