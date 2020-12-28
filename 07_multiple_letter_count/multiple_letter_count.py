def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    phraseDict = {}
    for char in set(phrase.replace(" ","")):
        phraseDict[char] = phrase.count(char)

    return phraseDict

print(f"multiple_letter_count('yay') should return dict('y': 2, 'a': 1), result: {multiple_letter_count('yay')}")
print(f"multiple_letter_count('Yay') should return dict('Y': 1, 'a': 1, 'y': 1), result: {multiple_letter_count('Yay')}")