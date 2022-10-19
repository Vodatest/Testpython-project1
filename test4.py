
# pylint: disable=C0103
# pylint: disable=C0114
# exceptions

def int2hex(integer):
    """Function that converts an integer to a hexadecimal string"""
    try:
        hexadecimal = hex(integer)
        return hexadecimal

    except TypeError:
        print('An integer should be provided as input')

# call the function
int2hex(5)
