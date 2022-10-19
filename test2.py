"""
high level support for doing this and that.
"""
def quadratic(A, B, C):
    """
    high level support for doing this and that.
    """
    # Calculate solution to a quadratic equation using the quadratic
    # formula.
    #
    # A quadratic equation always has 2 solutions x_1 and x_2.
    X_1 = (- B+(B**2-4*A*C)**(1/2)) / (2*A)
    X_2 = (- B-(B**2-4*A*C)**(1/2)) / (2*A)
    return X_1, X_2
