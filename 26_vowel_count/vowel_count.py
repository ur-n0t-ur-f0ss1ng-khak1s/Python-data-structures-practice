def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    freq_dict = {}
    phrase_list = []
    phrase_list[:0] = phrase #converting string to list
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for letter in phrase_list:
        if letter.lower() in freq_dict:
            freq_dict[letter.lower()] += 1
        elif letter.lower() in vowel_list:
            freq_dict[letter.lower()] = 1
    return freq_dict