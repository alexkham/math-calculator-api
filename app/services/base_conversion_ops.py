from fastapi import HTTPException

def binary_to_decimal(value: str) -> int:
    try:
        return int(value, 2)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid binary input.")

def binary_to_octal(value: str) -> str:
    return oct(binary_to_decimal(value))[2:]

def binary_to_hex(value: str) -> str:
    return hex(binary_to_decimal(value))[2:]

def decimal_to_binary(value: int) -> str:
    return bin(value)[2:]

def decimal_to_octal(value: int) -> str:
    return oct(value)[2:]

def decimal_to_hex(value: int) -> str:
    return hex(value)[2:]

def octal_to_decimal(value: str) -> int:
    try:
        return int(value, 8)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid octal input.")

def octal_to_binary(value: str) -> str:
    return bin(octal_to_decimal(value))[2:]

def octal_to_hex(value: str) -> str:
    return hex(octal_to_decimal(value))[2:]

def hex_to_decimal(value: str) -> int:
    try:
        return int(value, 16)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid hex input.")

def hex_to_binary(value: str) -> str:
    return bin(hex_to_decimal(value))[2:]

def hex_to_octal(value: str) -> str:
    return oct(hex_to_decimal(value))[2:]
