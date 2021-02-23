def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    phrase_list = []
    phrase_list[:0] = phrase #converting string to list
    phrase_list[0] = phrase_list[0].upper()
    return ''.join(phrase_list)