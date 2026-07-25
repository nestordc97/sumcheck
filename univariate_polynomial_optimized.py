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


def round_summatory(p: list, round_num: int, subvals: list):
    """
    Compute univariate polynomial for a given round.
    
    Args:
        p: Polynomial terms
        round_num: Current round number (1-indexed, 0 < r <= n)
        subvals: Vector of random elements from previous rounds (length: round_num - 1)
    """
    num_variables = validate_polynomial()
    
    # Prepare substitution vector with X_r = 1 as variable
    sub_vals = subvals + [1]
    
    n_remaining = num_variables - round_num
    power = 1 << n_remaining  # 2^n_remaining
    
    # Initialize univariate polynomial coefficients
    univariate = [GF(0)] * (DIMENSION + 1)
    
    # Sum over all boolean assignments to remaining variables
    bool_matrix = boolean_matrix(n_remaining) if n_remaining > 0 else [[]]
    
    for i in range(power):
        # Create complete variable assignment
        if n_remaining > 0:
            val = GF(sub_vals + bool_matrix[i])
        else:
            val = GF(sub_vals)
        
        # Accumulate contributions
        for term in p[1:]:
            degree = term[round_num]
            # Evaluate monomial with substituted variables
            monomial = [[0]] + [term]
            univariate[degree] += GF(evaluate_polynomial(monomial, val))
        
        # Add constant term
        univariate[0] += GF(p[0][0])
    
    # Display the univariate polynomial
    print(f"Univariate polynomial: {GF(univariate)}")
    
    # Compute g(0) + g(1)
    c = univariate[0] + sum(univariate)
    return c


def main():
    """Interactive univariate polynomial evaluation for sum-check protocol."""
    try:
        round_num = int(input("Enter the round number: "))
        
        if round_num > 1:
            print(f"Enter {round_num - 1} random values:")
            randoms = [int(input()) for _ in range(round_num - 1)]
        else:
            randoms = []
        
        result = round_summatory(POLY, round_num, randoms)
        print(f"Result g(0) + g(1) = {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nInterrupted by user")


if __name__ == "__main__":
    main()
