import galois
from constants import CHAR, DEGREE, FIELD_SIZE, GF


def boolean_matrix(n: int) -> list:
    """Generate matrix of n rows with all 2^n boolean possibilities."""
    if n <= 0:
        raise ValueError("n must be greater than 0")
    
    matrix = []
    for i in range(1 << n):  # Use bit shift instead of 2^n
        row = [(i >> (n - j - 1)) & 1 for j in range(n)]
        matrix.append(row)
    return matrix


def evaluate_polynomial(p: list, val: list):
    """
    Evaluate polynomial at given values.
    p: list of terms, each [coefficient, deg_var1, deg_var2, ...]
    val: list of variable values
    """
    if len(val) + 1 != len(p[0]):
        raise ValueError(f"Dimension mismatch: expected {len(p[0]) - 1} variables, got {len(val)}")
    
    result = GF(p[0][0])
    
    for term in p[1:]:
        term_value = GF(term[0])  # Start with coefficient
        
        for idx, degree in enumerate(term[1:]):
            if degree != 0:
                var_value = pow(val[idx], degree, FIELD_SIZE)  # Use modular exponentiation
                term_value *= GF(var_value)
        
        result += term_value
    
    return result
