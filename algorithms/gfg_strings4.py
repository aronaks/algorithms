def is_it_empty(key_str, sub_str):
    if len(key_str) == 0:
        return True

    ind = key_str.find(sub_str)
    if ind == -1:
        return False

    new_str = key_str[:ind] + key_str[ind+len(sub_str):]
    return is_it_empty(new_str, sub_str)
