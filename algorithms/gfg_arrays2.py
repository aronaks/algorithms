def find_leaders(keys, keys_length):
    all_leaders = []
    leader = None
    for i in range(keys_length-1, -1, -1):
        if keys[i] > leader:
            leader = keys[i]
            all_leaders.append(leader)
    return all_leaders
