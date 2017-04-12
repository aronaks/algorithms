def remove_spaces1(str_keys):
    """
    Given a string, remove all spaces from the string and return it.
    :param str_keys: a string object, e.g. "g  eeks   for ge  eeks  "
    :return: the string object without spaces, e.g. "geeksforgeeks"
    """
    new_str_list = [s for s in str_keys if s != ' ']
    return to_string(new_str_list)


def remove_spaces2(str_keys):
    new_str_list = str_keys.split(' ')
    return to_string(new_str_list)


def to_string(seq):
    return ''.join(seq)
