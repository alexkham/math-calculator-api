from fastapi import FastAPI
from app.routers import arithmetic, algebra ,trigo ,roots ,exponents,logarithms ,complex ,vectors,statistics

app = FastAPI(title="Math Calculator API",root_path="/math")

@app.get("/")
def root():
    return {"message": "Math calculator is online!"}

app.include_router(arithmetic.router, prefix="/arithmetic", tags=["Arithmetic"])
app.include_router(algebra.router, prefix="/algebra", tags=["Algebra"])
app.include_router(trigo.router, prefix="/trigo", tags=["Trigonometry"]) 
app.include_router(roots.router, prefix="/roots", tags=["Roots"])
app.include_router(exponents.router, prefix="/exponents", tags=["Exponents"])
app.include_router(logarithms.router, prefix="/logarithms", tags=["Logarithms"])
app.include_router(complex.router, prefix="/complex", tags=["Complex"])
app.include_router(vectors.router, prefix="/vectors", tags=["Vectors"])
app.include_router(statistics.router, prefix="/statistics", tags=["Statistics"])