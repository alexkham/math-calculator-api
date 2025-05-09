structure = {
    ".gitignore": "",
    "main.py": "",
    "requirements.txt": "",
    "setup_calculator_structure.py": "",
    "summarize_app.py": "",
    "app\main.py": "",
    "app\__init__.py": "",
    "app\models\schemas.py": "",
    "app\models\__init__.py": "",
    "app\routers\algebra.py": "",
    "app\routers\arithmetic.py": "",
    "app\routers\exponents.py": "",
    "app\routers\logarithms.py": "",
    "app\routers\roots.py": "",
    "app\routers\trigo.py": "",
    "app\routers\__init__.py": "",
    "app\services\algebra_ops.py": "",
    "app\services\arithmetic_ops.py": "",
    "app\services\exponent_ops.py": "",
    "app\services\log_ops.py": "",
    "app\services\roots_ops.py": "",
    "app\services\trigo_ops.py": "",
    "app\services\__init__.py": "",
}

content = {
    ".gitignore": """math-api-venv/
__pycache__/
*.pyc""",
    "main.py": """from fastapi import FastAPI


# This is a simple FastAPI application that serves as a math calculator API.
# It includes a root endpoint that returns a welcome message.

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Math calculator is online! Congratulations!!!!!!"}""",
    "requirements.txt": """fastapi
uvicorn""",
    "setup_calculator_structure.py": """import os

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


# ...truncated...""",
    "summarize_app.py": """import os

BASE_DIR = "."
OUTPUT_FILE = "app_summary.py"

EXCLUDE_DIRS = {"__pycache__", ".git", "venv", ".venv", "env", "math-api-venv"}

structure = {}
content = {}

def should_exclude(path):
    parts = set(path.split(os.sep))
    return not parts.isdisjoint(EXCLUDE_DIRS)

for root, _, files in os.walk(BASE_DIR):
    if should_exclude(root):
        continue
    for file in files:
        full_path = os.path.join(root, file)
        rel_path = os.path.relpath(full_path, BASE_DIR)

        if should_exclude(rel_path):
            continue

        structure[rel_path] = ""
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                code = f.read().strip()
                snippet = code if len(code) <= 1000 else code[:1000] + "\n# ...truncated..."
                content[rel_path] = snippet
        except Exception as e:
            content[rel_path] = f"# Could not read file: {e}"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("structur
# ...truncated...""",
    "app\main.py": """from fastapi import FastAPI
from app.routers import arithmetic, algebra ,trigo ,roots ,exponents,logarithms

app = FastAPI(title="Math Calculator API")

@app.get("/")
def root():
    return {"message": "Math calculator is online!"}

app.include_router(arithmetic.router, prefix="/arithmetic", tags=["Arithmetic"])
app.include_router(algebra.router, prefix="/algebra", tags=["Algebra"])
app.include_router(trigo.router, prefix="/trigo", tags=["Trigonometry"]) 
app.include_router(roots.router, prefix="/roots", tags=["Roots"])
app.include_router(exponents.router, prefix="/exponents", tags=["Exponents"])
app.include_router(logarithms.router, prefix="/logarithms", tags=["Logarithms"])""",
    "app\__init__.py": """""",
    "app\models\schemas.py": """from pydantic import BaseModel
from typing import List

class ValuesList(BaseModel):
    values: List[float]""",
    "app\models\__init__.py": """""",
    "app\routers\algebra.py": """from fastapi import APIRouter, Query
from app.services.algebra_ops import solve_quadratic

router = APIRouter()

@router.get("/solve_quadratic")
def solve_quadratic_route(a: float = Query(...), b: float = Query(...), c: float = Query(...)):
    return {"operation": "solve_quadratic", "roots": solve_quadratic(a, b, c)}""",
    "app\routers\arithmetic.py": """from fastapi import APIRouter, Query
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
    return {"operation": "divide", "result": divide(a, b)}""",
    "app\routers\exponents.py": """from fastapi import APIRouter, Query
from app.services.exponent_ops import (
    square,
    cube,
    power,
    rational_power,
    inverse,
    negative_power
)

router = APIRouter()

@router.get("/square")
def square_endpoint(x: float = Query(...)):
    return {"operation": "square", "result": square(x)}

@router.get("/cube")
def cube_endpoint(x: float = Query(...)):
    return {"operation": "cube", "result": cube(x)}

@router.get("/power")
def power_endpoint(
    x: float = Query(...),
    n: float = Query(...)
):
    return {"operation": f"{x}^{n}", "result": power(x, n)}

@router.get("/fractional")
def fractional_power_endpoint(
    x: float = Query(...),
    m: float = Query(...),
    n: float = Query(...)
):
    return {"operation": f"{x}^({m}/{n})", "result": rational_power(x, m, n)}

@router.get("/inverse")
def inverse_endpoint(x: float = Query(...)):
    return {"operation": "x^-1", "result": inverse(x)}

@router.get("/negative")
def negative_power_endpoint(
    x: float = 
# ...truncated...""",
    "app\routers\logarithms.py": """from fastapi import APIRouter, Query
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
    return {"operation": "e^x", "result": natural_expone
# ...truncated...""",
    "app\routers\roots.py": """from fastapi import APIRouter, Query
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
    x: float = Query(..., descript
# ...truncated...""",
    "app\routers\trigo.py": """from fastapi import APIRouter, Query
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
def 
# ...truncated...""",
    "app\routers\__init__.py": """""",
    "app\services\algebra_ops.py": """import math

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
        return [f"{real}+{imag}i", f"{real}-{imag}i"]""",
    "app\services\arithmetic_ops.py": """from fastapi import HTTPException



def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    return a / b""",
    "app\services\exponent_ops.py": """from fastapi import HTTPException

def square(x: float) -> float:
    return x ** 2

def cube(x: float) -> float:
    return x ** 3

def power(x: float, n: float) -> float:
    return x ** n

def rational_power(x: float, m: float, n: float) -> float:
    if n == 0:
        raise HTTPException(status_code=400, detail="Denominator (n) cannot be zero.")
    exponent = m / n
    if x < 0 and not exponent.is_integer():
        raise HTTPException(status_code=400, detail="Cannot raise negative base to fractional power.")
    return x ** exponent

def inverse(x: float) -> float:
    if x == 0:
        raise HTTPException(status_code=400, detail="Cannot take inverse of zero.")
    return 1 / x

def negative_power(x: float, n: float) -> float:
    if x == 0:
        raise HTTPException(status_code=400, detail="Cannot raise zero to a negative power.")
    return x ** (-n)""",
    "app\services\log_ops.py": """import math
from fastapi import HTTPException

def log_natural(x: float) -> float:
    if x <= 0:
        raise HTTPException(status_code=400, detail="ln(x): x must be > 0")
    return math.log(x)

def log_base10(x: float) -> float:
    if x <= 0:
        raise HTTPException(status_code=400, detail="log10(x): x must be > 0")
    return math.log10(x)

def log_base2(x: float) -> float:
    if x <= 0:
        raise HTTPException(status_code=400, detail="log2(x): x must be > 0")
    return math.log(x, 2)

def log_custom_base(x: float, base: float) -> float:
    if x <= 0:
        raise HTTPException(status_code=400, detail="log_a(x): x must be > 0")
    if base <= 0 or base == 1:
        raise HTTPException(status_code=400, detail="log_a(x): base must be > 0 and ≠ 1")
    return math.log(x, base)

def natural_exponent(x: float) -> float:
    return math.exp(x)""",
    "app\services\roots_ops.py": """from fastapi import HTTPException
import math

def square_root(x: float) -> float:
    if x < 0:
        raise HTTPException(status_code=400, detail="Cannot take square root of a negative number.")
    return math.sqrt(x)

def cube_root(x: float) -> float:
    return math.copysign(abs(x) ** (1/3), x)  # Handles negative numbers correctly

def nth_root(x: float, n: int) -> float:
    if n == 0:
        raise HTTPException(status_code=400, detail="Cannot take zeroth root.")
    if x < 0 and n % 2 == 0:
        raise HTTPException(status_code=400, detail="Even root of negative number is not real.")
    return math.copysign(abs(x) ** (1/n), x)

def rational_power(x: float, m: float, n: float) -> float:
    if n == 0:
        raise HTTPException(status_code=400, detail="Exponent denominator (n) cannot be zero.")
    exponent = m / n
    if x < 0 and not exponent.is_integer():
        raise HTTPException(status_code=400, detail="Cannot raise negative base to fractional power.")
    return x 
# ...truncated...""",
    "app\services\trigo_ops.py": """import math
from fastapi import HTTPException

def sin_deg(x: float) -> float:
    try:
        return math.sin(x)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input for sin: {e}")

def cos_deg(x: float) -> float:
    try:
        return math.cos(x)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input for cos: {e}")

def tan_deg(x: float) -> float:
    try:
        return math.tan(x)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid input for tan: {e}")

def to_radians(deg: float) -> float:
    try:
        return math.radians(deg)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid degrees: {e}")

def to_degrees(rad: float) -> float:
    try:
        return math.degrees(rad)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid radians: {e}")


def asin_func(x: float) -> float:
    if not -1
# ...truncated...""",
    "app\services\__init__.py": """""",
}
