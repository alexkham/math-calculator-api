from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.vector_ops import (
    add_vectors, subtract_vectors, dot_product, cross_product
)

router = APIRouter()

class VectorPair(BaseModel):
    v1: list[float]
    v2: list[float]

@router.post("/add")
def add(pair: VectorPair):
    try:
        result = add_vectors(pair.v1, pair.v2)
        return {"operation": "add", "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/subtract")
def subtract(pair: VectorPair):
    try:
        result = subtract_vectors(pair.v1, pair.v2)
        return {"operation": "subtract", "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/dot")
def dot(pair: VectorPair):
    try:
        result = dot_product(pair.v1, pair.v2)
        return {"operation": "dot", "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/cross")
def cross(pair: VectorPair):
    try:
        result = cross_product(pair.v1, pair.v2)
        return {"operation": "cross", "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
