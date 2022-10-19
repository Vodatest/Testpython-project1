"""
high level support for doing this and that.
"""
def quadratic(a, b, c, x):
    """
    high level support for doing this and that.
    """
    # Calculate solution to a quadratic equation using the quadratic
    # formula.
    #
    # A quadratic equation always has 2 solutions x_1 and x_2.
    x_1 = (- b+(b**2-4*a*c)**(1/2)) / (2*a)
    x_2 = (- b-(b**2-4*a*c)**(1/2)) / (2*a)
    return x_1, x_2
