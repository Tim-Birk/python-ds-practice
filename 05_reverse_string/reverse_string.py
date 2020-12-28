def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    if not type(phrase) == str:
        return "Input is not a string"

    return phrase[::-1]

print(f"reverse_string('awesome') should return 'emosewa', result: {reverse_string('awesome')}")
print(f"reverse_string('sauce') should return 'ecuas', result: {reverse_string('sauce')}")
        


