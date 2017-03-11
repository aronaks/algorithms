def are_there_unique_characters(keys, keys_length):
    for i in range(keys_length):
        if keys[i] in keys[i + 1:keys_length - 1]:
            return "No"
    else:
        return "Yes"
