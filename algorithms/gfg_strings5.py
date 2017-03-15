def remove_spaces1(str_keys):
    new_str_list = [s for s in str_keys if s != ' ']
    return to_string(new_str_list)


def remove_spaces2(str_keys):
    new_str_list = str_keys.split(' ')
    return to_string(new_str_list)


def to_string(seq):
    return ''.join(seq)
