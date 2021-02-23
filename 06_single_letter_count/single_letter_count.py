def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    letter_count = 0
    word_list = []
    word_list[:0] = word #converting string to list
    i = 0
    while i < len(word_list):
        if word_list[i] == letter or word_list[i].lower() == letter:
            letter_count += 1
        i += 1
    return letter_count