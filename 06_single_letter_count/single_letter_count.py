def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    return word.upper().count(letter.upper())

print(f"single_letter_count('Hello World', 'h') should return 1, result: {single_letter_count('Hello World', 'h')}")
print(f"single_letter_count('Hello World', 'z') should return 0, result: {single_letter_count('Hello World', 'z')}")
print(f"single_letter_count('Hello World', 'l') should return 3, result: {single_letter_count('Hello World', 'l')}")