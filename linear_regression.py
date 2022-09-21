import numpy as np

def design_matrix(X, degree=2):
    """
    Returns a design matrix.
    Args:
        X: Array of shape (m,1) with 'm' independent data.
        degree: Integer with the degree of the polynomial. 
                  Note that a degree-n polynomial has n+1 coefficients.     
    Returns:
        X_d: Design matrix of shape (m, order+1).
    """
    m = len(X)
    n = degree + 1 
    X_d = np.zeros((m, n))
    
    for j in range(n):
        for i in range(m):
            X_d[i,j] = X[i]**j

    return X_d


def solve_normal_equation(X, y, degree=2):
    """
    Solve the normal equation: theta_best = (X^T * X)^-1 * X^T * y
    
    Args:
             X: Array of shape (m,1) with 'm' independent data.
        degree: Integer with the degree of the polynomial. 
             y: Dependent data of shape (m,1).
                  
    Returns:
        theta_best: Best parameters, array of shape (n,).
    """
    
    X_d = design_matrix(X, degree) 
    X = X_d
    X_trans = np.transpose(X)
    transformation_matrix = np.matmul( np.linalg.inv( np.matmul(X_trans, X) ), X_trans) # (X^T * X)^-1 * X^T

    theta_best = np.matmul(transformation_matrix, y)
    theta_best = np.ndarray.flatten(theta_best)
          
    return theta_best


def linear_regression(X, y, degree=2):
    return solve_normal_equation(X, y, degree)