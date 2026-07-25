import random
import galois
from constants import CHAR, DEGREE, FIELD_SIZE, POLY, DIMENSION, GF
from functions_optimized import boolean_matrix, evaluate_polynomial


def validate_polynomial():
    """Ensure all monomials have the same number of variables."""
    variables = len(POLY[1]) - 1
    for term in POLY[2:]:
        if len(term) - 1 != variables:
            raise ValueError("All monomials must have the same number of variables!")
    return variables


def one_dimensional_polynomial(coeffs: list, val):
    """Evaluate univariate polynomial: result = coeffs[0] + coeffs[1]*val + ..."""
    result = GF(coeffs[0])
    val_power = GF(val)
    
    for i in range(1, len(coeffs)):
        result += GF(coeffs[i]) * (val_power ** i)
    
    return result


def format_polynomial(coeffs: list) -> str:
    """Format polynomial coefficients as readable string."""
    terms = [str(coeffs[0])]
    for i in range(1, len(coeffs)):
        if coeffs[i] != 0:
            terms.append(f"+{coeffs[i]}X^{i}")
    return "".join(terms)


def sum_check_protocol(p: list, dim: int):
    """Execute sum-check protocol for polynomial verification."""
    
    # Validate polynomial
    num_variables = validate_polynomial()
    
    # Compute H: sum of polynomial over all boolean inputs
    H = GF(0)
    bool_matrix = boolean_matrix(num_variables)
    
    for bool_point in bool_matrix:
        H += evaluate_polynomial(p, bool_point)
    
    if len(p) < 2:
        raise ValueError("Polynomial must have variables, not just constant term")
    
    # START OF PROTOCOL
    print(f"Polynomial dimension: {dim}")
    print(f"Send first univariate polynomial g(X) = a_0 + a_1*X + ... + a_{dim}*X^{dim}")
    print(f"Provide {dim + 1} coefficients (a_0, ..., a_{dim}):")
    
    randoms = []
    g = []
    
    # Round 1
    for i in range(dim + 1):
        try:
            coeff = GF(int(input()))
        except ValueError:
            print(f"Invalid input. Use integers 0 to {FIELD_SIZE - 1}")
            return
        g.append(coeff)
    
    # Verify: g(0) + g(1) should equal H
    c1 = g[0] + sum(g)  # Equivalent to g(0) + g(1)
    
    print(f"Polynomial received: {format_polynomial(g)}")
    
    if H != c1:
        print("❌ Verification failed at round 1")
        return
    
    # Subsequent rounds
    for r in range(1, num_variables):
        r1 = random.randint(0, FIELD_SIZE - 1)
        randoms.append(GF(r1))
        
        print(f"\nRound {r + 1}: Random element = {r1}")
        
        gh = one_dimensional_polynomial(g, r1)
        
        print(f"Send univariate polynomial g(X):")
        
        g = []
        for i in range(dim + 1):
            try:
                coeff = GF(int(input()))
            except ValueError:
                print(f"Invalid input. Use integers 0 to {FIELD_SIZE - 1}")
                return
            g.append(coeff)
        
        c1 = g[0] + sum(g)
        print(f"Polynomial received: {format_polynomial(g)}")
        
        if gh != c1:
            print(f"❌ Verification failed at round {r + 1}")
            return
    
    # Final round verification
    r1 = random.randint(0, FIELD_SIZE - 1)
    randoms.append(GF(r1))
    
    gh = one_dimensional_polynomial(g, r1)
    
    if gh == evaluate_polynomial(p, randoms):
        print("✓ Protocol accepted!")
    else:
        print("❌ Final verification failed")


if __name__ == "__main__":
    sum_check_protocol(POLY, DIMENSION)
