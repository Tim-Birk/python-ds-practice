def product(a, b):
    """Return product of a and b.

        >>> product(2, 2)
        4

        >>> product(2, -2)
        -4
    """
    return a * b

print(f"product(2, 2) should return 4, result: {product(2, 2)}")
print(f"product(2, 2) should return -4, result: {product(2, -2)}")