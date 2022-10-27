# pylint: disable=C0114
# keyword and default arguments

# function that calculates cylinder volume
def cylinder_volume(height, radius=5.0):
    """Volume of a cylinder
    Parameters:
    height (float): Height of the cylinder
    radius (float): Radius of the cylinder (default 5.0)
    Returns:
    float:Volume of the cylinder
    """
    return height * 3.14159 * radius**2

# calling the function using positional arguments
cylinder_volume(10.3, 7.2)

# calling the function using keyword arguments
cylinder_volume(height=10.3, radius=7.2)






