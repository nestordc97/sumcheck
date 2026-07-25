import galois

# Field parameters
CHAR = 97  # Characteristic of the field
DEGREE = 2  # Degree of the field
FIELD_SIZE = CHAR ** DEGREE  # Cache computed field size

# Polynomial definition: each monomial as [coefficient, deg_var1, deg_var2, ...]
# Example: 3X₁(X₂)³X₃ is represented as [3, 1, 3, 1]
POLY = [[0], [2, 3, 0, 0], [1, 1, 0, 1], [1, 0, 1, 1]]
DIMENSION = 3  # Maximal degree of each variable

# Precompute field
GF = galois.GF(FIELD_SIZE)
