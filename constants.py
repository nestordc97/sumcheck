import math

import galois

char = 97 #Characteristic of the field.

degree = 2 #Degree of the field
poly=[[0],[2,3,0,0],[1,1,0,1],[1,0,1,1]] #This is the polynomial. Every vector is a monomial: The first value is the coefficient and the other values are the degree of each variable. For example, the monomial 3X_1(x_2)^3x_3 is represented by (3,1,3,1). 
#The elements of the field have to be expressed as integers from 0 to char^degree-1

dimension = 3 #maximal degree of each variable
