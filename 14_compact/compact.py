def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    truthy_list = []
    for item in lst:
        if item:
            truthy_list.append(item)
    return truthy_list