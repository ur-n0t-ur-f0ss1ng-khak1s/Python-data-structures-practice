def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase = phrase.lower()
    phrase = ' '.join(phrase)
    phrase_list = []
    phrase_list[:0] = phrase #converting string to list
    i = 0
    while i < len(phrase_list):
        if phrase_list.pop() != phrase_list.pop(0):
            return False
        i += 1
    return True
