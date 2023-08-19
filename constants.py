import math

char = 7 #Characteristic of the field.
poly=[[0],[2,3,0,0],[1,1,0,1],[1,0,1,1]] #This is the polynomial. Every vector is a monomial: The first value is the coefficient and the other values are the degree of each variable. For example, the monomial 3X_1(x_2)^3x_3 is represented by (3,1,3,1). 
dimension = 4 #maximal degree of each variable


def boolean_matrix(n):#This gives a matrix of n rows and 2^n columns with all the boolean possibilities
    if n <= 0:
        raise ValueError("n should be greater than 0")

    num_rows = int(math.pow(2,n))
    boolean_matrix = []

    for i in range(num_rows):
        boolean_row = []
        for j in range(n):
            bit = (i >> (n - j - 1)) & 1
            boolean_row.append(bit)
        boolean_matrix.append(boolean_row)

    return boolean_matrix

def evaluate_polynomial(p:list, val:list):#This function can also be done in a recursive way. But I think that it is clearer to do it directly.
    #p is a vector of vectors. Every list describes a term. For example, if we have 3 variables, 4xyz^2 is expressed as [4,1,1,2] and 3xz = [3,1,0,1]
    #The first of this terms is just a list with one number, the constant coefficient.

    n = len(p)

    result = p[0][0]    
    
    for t in range(1,len(p)):#Each t is a term

        if len(val)+1 != len(p[t]):
            raise ValueError("There is a dimension problem")
            
        term = 1
        
        for i in range (1,len(p[t])):#Each var is a variable in the term. In 4xyz^2, the number 4 "counts" as a variable.
            #print(p[t][i])
            if p[t][i] != 0:
                term = term*math.pow(val[i-1],p[t][i])           

        term = term*p[t][0]

        result = result+term
    return(result%char)
