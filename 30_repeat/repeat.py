def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    list_of_phrases = []
    if type(num) is int and num >= 0:
        while num > 0:
            list_of_phrases.append(phrase)
            num -= 1
        return ''.join(list_of_phrases)
    return None
