def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if not type(lst) == list:
        return None
    elif len(lst) == 0:
        return None

    return lst[-1]

print(f"last_element([1, 2, 3]) should return 3, result: {last_element([1, 2, 3])}")
print(f"last_element([]) should return None, result: {last_element([])}")