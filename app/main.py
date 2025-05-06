from fastapi import FastAPI
from app.routers import arithmetic, algebra ,trigo ,roots ,exponents

app = FastAPI(title="Math Calculator API")

@app.get("/")
def root():
    return {"message": "Math calculator is online!"}

app.include_router(arithmetic.router, prefix="/arithmetic", tags=["Arithmetic"])
app.include_router(algebra.router, prefix="/algebra", tags=["Algebra"])
app.include_router(trigo.router, prefix="/trigo", tags=["Trigonometry"]) 
app.include_router(roots.router, prefix="/roots", tags=["Roots"])
app.include_router(exponents.router, prefix="/exponents", tags=["Exponents"])
