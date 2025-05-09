from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services import statistics_ops as ops

router = APIRouter()

class DataInput(BaseModel):
    values: List[float]

@router.post("/analyze")
def analyze(data: DataInput):
    try:
        result = {
            "sample_size": ops.sample_size(data.values),
            "sum": ops.total_sum(data.values),
            "mean": ops.mean(data.values),
            "median": ops.median(data.values),
            "mode": ops.mode(data.values),
            "min": ops.minimum(data.values),
            "max": ops.maximum(data.values),
            "range": ops.value_range(data.values),
            "variance": ops.variance(data.values),
            "std_dev": ops.std_dev(data.values),
            "q1": ops.quartiles(data.values)["q1"],
            "q3": ops.quartiles(data.values)["q3"],
            "iqr": ops.quartiles(data.values)["iqr"],
            "skewness": ops.skewness(data.values),
            "kurtosis": ops.kurtosis(data.values),
            "coefficient_of_variation": ops.coef_variation(data.values),
            "geometric_mean": ops.geometric_mean(data.values),
            "harmonic_mean": ops.harmonic_mean(data.values),
            "root_mean_square": ops.root_mean_square(data.values),
        }
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
