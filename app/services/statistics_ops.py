import math
import statistics
from typing import List
from scipy import stats
import numpy as np

def sample_size(data: List[float]) -> int:
    return len(data)

def total_sum(data: List[float]) -> float:
    return sum(data)

def mean(data: List[float]) -> float:
    return statistics.mean(data)

def median(data: List[float]) -> float:
    return statistics.median(data)

def mode(data: List[float]) -> float:
    return statistics.mode(data)

def minimum(data: List[float]) -> float:
    return min(data)

def maximum(data: List[float]) -> float:
    return max(data)

def value_range(data: List[float]) -> float:
    return max(data) - min(data)

def variance(data: List[float]) -> float:
    return statistics.variance(data)

def std_dev(data: List[float]) -> float:
    return statistics.stdev(data)

def quartiles(data: List[float]) -> dict:
    sorted_data = sorted(data)
    q1 = np.percentile(sorted_data, 25)
    q3 = np.percentile(sorted_data, 75)
    iqr = q3 - q1
    return {"q1": q1, "q3": q3, "iqr": iqr}

def skewness(data: List[float]) -> float:
    return stats.skew(data)

def kurtosis(data: List[float]) -> float:
    return stats.kurtosis(data)

def coef_variation(data: List[float]) -> float:
    m = mean(data)
    if m == 0:
        raise ValueError("Mean is zero, coefficient of variation undefined.")
    return std_dev(data) / m

def geometric_mean(data: List[float]) -> float:
    return stats.gmean(data)

def harmonic_mean(data: List[float]) -> float:
    return stats.hmean(data)

def root_mean_square(data: List[float]) -> float:
    return math.sqrt(sum(x**2 for x in data) / len(data))
