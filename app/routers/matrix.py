from fastapi import APIRouter
from app.models.schemas import MatrixInput, TwoMatricesInput
from app.services.matrix_ops import (
    matrix_add,
    matrix_multiply,
    matrix_transpose,
    matrix_determinant,
    matrix_inverse
)

router = APIRouter()

@router.post("/add")
def add_matrices(data: TwoMatricesInput):
    return {"result": matrix_add(data.matrix1, data.matrix2)}

@router.post("/multiply")
def multiply_matrices(data: TwoMatricesInput):
    return {"result": matrix_multiply(data.matrix1, data.matrix2)}

@router.post("/transpose")
def transpose_matrix(data: MatrixInput):
    return {"result": matrix_transpose(data.matrix)}

@router.post("/determinant")
def determinant_matrix(data: MatrixInput):
    return {"result": matrix_determinant(data.matrix)}

@router.post("/inverse")
def inverse_matrix(data: MatrixInput):
    return {"result": matrix_inverse(data.matrix)}
