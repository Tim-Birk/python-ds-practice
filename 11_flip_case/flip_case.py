def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    final_string = []
    for char in phrase:
        if char.upper() == to_swap.upper():
            if char.isupper():
                final_string.append(char.lower())
            else:
                final_string.append(char.upper())
        else:
            final_string.append(char)

    return "".join(final_string)