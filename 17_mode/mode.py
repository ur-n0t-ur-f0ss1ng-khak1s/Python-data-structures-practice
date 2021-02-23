def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    dict_of_nums = {}
    max_num = 0
    most_common_num = 0
    for num in nums:
        if str(num) in dict_of_nums:
            dict_of_nums[str(num)] += 1
        else:
            dict_of_nums[str(num)] = 1
    for key in dict_of_nums:
        if dict_of_nums[key] > max_num:
            max_num = dict_of_nums[key]
            most_common_num = key
    return int(most_common_num)