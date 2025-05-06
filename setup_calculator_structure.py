import os

# Base dir (now math-calculator-api)
BASE_DIR = "."

structure = {
    f"{BASE_DIR}/app/__init__.py": "",
    f"{BASE_DIR}/app/main.py": "",
    f"{BASE_DIR}/app/routers/__init__.py": "",
    f"{BASE_DIR}/app/routers/arithmetic.py": "",
    f"{BASE_DIR}/app/routers/algebra.py": "",
    f"{BASE_DIR}/app/services/__init__.py": "",
    f"{BASE_DIR}/app/services/arithmetic_ops.py": "",
    f"{BASE_DIR}/app/services/algebra_ops.py": "",
    f"{BASE_DIR}/app/models/__init__.py": "",
    f"{BASE_DIR}/app/models/schemas.py": "",
    f"{BASE_DIR}/requirements.txt": "fastapi\nuvicorn\n"
}

content = {
    f"{BASE_DIR}/app/main.py": '''from fastapi import FastAPI
from app.routers import arithmetic, algebra

app = FastAPI(title="Math Calculator API")

@app.get("/")
def root():
    return {"message": "Math calculator is online!"}

app.include_router(arithmetic.router, prefix="/arithmetic", tags=["Arithmetic"])
app.include_router(algebra.router, prefix="/algebra", tags=["Algebra"])
''',

    f"{BASE_DIR}/app/routers/arithmetic.py": '''from fastapi import APIRouter, Query
from app.services.arithmetic_ops import add, subtract, multiply, divide

router = APIRouter()

@router.get("/add")
def add_route(a: float = Query(...), b: float = Query(...)):
    return {"operation": "add", "result": add(a, b)}

@router.get("/subtract")
def subtract_route(a: float = Query(...), b: float = Query(...)):
    return {"operation": "subtract", "result": subtract(a, b)}

@router.get("/multiply")
def multiply_route(a: float = Query(...), b: float = Query(...)):
    return {"operation": "multiply", "result": multiply(a, b)}

@router.get("/divide")
def divide_route(a: float = Query(...), b: float = Query(...)):
    return {"operation": "divide", "result": divide(a, b)}
''',

    f"{BASE_DIR}/app/services/arithmetic_ops.py": '''def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
''',

    f"{BASE_DIR}/app/routers/algebra.py": '''from fastapi import APIRouter, Query
from app.services.algebra_ops import solve_quadratic

router = APIRouter()

@router.get("/solve_quadratic")
def solve_quadratic_route(a: float = Query(...), b: float = Query(...), c: float = Query(...)):
    return {"operation": "solve_quadratic", "roots": solve_quadratic(a, b, c)}
''',

    f"{BASE_DIR}/app/services/algebra_ops.py": '''import math

def solve_quadratic(a: float, b: float, c: float):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return [root1, root2]
    elif discriminant == 0:
        root = -b / (2 * a)
        return [root]
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-discriminant) / (2 * a)
        return [f"{real}+{imag}i", f"{real}-{imag}i"]
''',

    f"{BASE_DIR}/app/models/schemas.py": '''from pydantic import BaseModel
from typing import List

class ValuesList(BaseModel):
    values: List[float]
'''
}

# Create everything
for path, default_content in structure.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.get(path, default_content))

print("✅ math-calculator-api project scaffold complete!")
