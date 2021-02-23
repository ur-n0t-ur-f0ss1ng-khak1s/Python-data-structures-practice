def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    half_length = len(phrase) / 2
    phrase_list = []
    phrase_list[:0] = phrase #converting string to list
    i = 0
    while i < half_length:
        reverse_index = -(i+1)
        end = phrase_list[reverse_index]
        phrase_list[reverse_index] = phrase_list[i]
        phrase_list[i] = end
        i += 1
    return ''.join(phrase_list)