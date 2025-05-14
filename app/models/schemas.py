from pydantic import BaseModel
from typing import List

class ValuesList(BaseModel):
    values: List[float]


class MatrixInput(BaseModel):
    matrix: List[List[float]]

class TwoMatricesInput(BaseModel):
    matrix1: List[List[float]]
    matrix2: List[List[float]]