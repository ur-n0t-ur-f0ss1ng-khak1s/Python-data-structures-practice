def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    first_freq_dict = {}
    second_freq_dict = {}
    phrase_list = []
    phrase_list_two = []
    phrase_list[:0] = str(num1)
    phrase_list_two[:0] = str(num2)
    for letter in phrase_list:
        if letter in first_freq_dict:
            first_freq_dict[letter] += 1
        else:
            first_freq_dict[letter] = 1
    for letter in phrase_list_two:
        if letter in second_freq_dict:
            second_freq_dict[letter] += 1
        else:
            second_freq_dict[letter] = 1
    for key in first_freq_dict:
        if first_freq_dict[key] != second_freq_dict[key]:
            return False
    return True