import math

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
