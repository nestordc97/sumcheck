Sumcheck Protocol Implementation
This repository contains scripts for implementing the Sumcheck Protocol based on the description in Section 4.1 of the book "Proofs, Arguments, and Zero-Knowledge" by Justin Thaler. The protocol is adapted for finite fields with prime orders.

Scripts
1. Sumcheck Protocol
File: sumcheck_protocol.py
Description: This script implements the Sumcheck Protocol, a fundamental concept in interactive proof systems. The protocol's computation is based on finite fields with prime orders. It follows the methodology described in Section 4.1 of the book.
2. Univariate Polynomial
File: univariate_polynomial.py
Description: This script assists the prover in computing the univariate polynomial corresponding to each round of the Sumcheck Protocol. It plays a crucial role in the protocol's execution.
Constants
The constants.py file contains essential functions and constants that are configurable by the user.

Functions
boolean_matrix(n)

Description: Generates a matrix of size n x 2^n with all possible boolean combinations. Used within the protocol computation.
Usage: matrix = boolean_matrix(n)
univariate_polynomial(coefficients, x)

Description: Computes the value of the univariate polynomial with given coefficients at the specified value x.
Usage: result = univariate_polynomial(coefficients, x)
Constants
char: Characteristic of the finite field.
poly: Definition of the hidden polynomial in terms of coefficients and degrees of variables.
dimension: Maximal degree of each variable.
Users can modify these constants to tailor the protocol to specific scenarios or field characteristics.

Usage
Clone the repository to your local machine using git clone https://github.com/nestordc97/sumcheck-protocol.git.
Navigate to the repository directory using cd sumcheck-protocol.
Explore and modify the scripts and constants as needed.
Run the scripts using python sumcheck_protocol.py and python univariate_polynomial.py.
Acknowledgments
Justin Thaler's book "Proofs, Arguments, and Zero-Knowledge" for providing the foundation for this implementation.
