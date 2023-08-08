def sum(a, b = 2):
    """This is a function that returns sum of  two numbers
    >>> sum(1, 2)
    3
    >>> sum(1.5, 2.5)
    4.0
    >>> sum(1.5)
    3.5

    """
    return a + b
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
print(sum(1.5))