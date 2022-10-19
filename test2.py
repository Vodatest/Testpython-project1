"""
high level support for doing this and that.
"""
def quadratic(a1, b1, c1, x1):
    
    """
    high level support for doing this and that.
    """
    
    # Calculate solution to a quadratic equation using the quadratic
    # formula.
    #
    # A quadratic equation always has 2 solutions x_1 and x_2.
    x_1 = (- b1+(b1**2-4*a1*c1)**(1/2)) / (2*a1)
    x_2 = (- b1-(b1**2-4*a1*c1)**(1/2)) / (2*a1)
    return x_1, x_2
