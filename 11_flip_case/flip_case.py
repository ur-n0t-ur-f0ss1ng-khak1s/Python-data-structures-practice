def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase_list = []
    phrase_list[:0] = phrase #converting string to list
    i = 0
    for letter in phrase_list:
        if letter.lower() == to_swap or letter.upper() == to_swap:
            if letter.islower():
                phrase_list[i] = letter.upper()
            else:
                phrase_list[i] = letter.lower()
        i += 1
        
    #return phrase
    return ''.join(phrase_list)
