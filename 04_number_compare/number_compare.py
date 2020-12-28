def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if not type(a) == int or not type(b) == int:
        return "Input is not a number"

    if a == b:
        return "Numbers are equal"
    elif b > a:
        return "Second is greater"
    else:
        return "First is greater"

print(f"number_compare(1, 1) should return 'Numbers are equal', result: {number_compare(1, 1)}")
print(f"number_compare(-1, 1) should return 'Second is greater', result: {number_compare(-1, 1)}")
print(f"number_compare(1, -2) should return 'First is greater', result: {number_compare(1, -2)}")