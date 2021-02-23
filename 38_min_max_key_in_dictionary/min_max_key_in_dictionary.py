def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    max_key = None
    min_key = None
    for item in d.items():
        if max_key == None and min_key == None:
            max_key = item[0]
            min_key = item[0]
        elif item[0] > max_key:
            max_key = item[0]
        elif item[0] < min_key:
            min_key = item[0]
    return (min_key, max_key)