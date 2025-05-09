def to_complex(real: float, imag: float) -> complex:
    return complex(real, imag)

def add_complex(a_real: float, a_imag: float, b_real: float, b_imag: float):
    return to_complex(a_real, a_imag) + to_complex(b_real, b_imag)

def subtract_complex(a_real: float, a_imag: float, b_real: float, b_imag: float):
    return to_complex(a_real, a_imag) - to_complex(b_real, b_imag)

def multiply_complex(a_real: float, a_imag: float, b_real: float, b_imag: float):
    return to_complex(a_real, a_imag) * to_complex(b_real, b_imag)

def divide_complex(a_real: float, a_imag: float, b_real: float, b_imag: float):
    denominator = to_complex(b_real, b_imag)
    if denominator == 0:
        raise ValueError("Division by zero is not allowed.")
    return to_complex(a_real, a_imag) / denominator
