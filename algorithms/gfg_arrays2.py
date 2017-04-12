def find_leaders(keys):
    """
    Write a function that prints all the LEADERS in the array. An element is leader 
    if it is greater than all the elements to its right side. And the rightmost 
    element is always a leader. For example int the array {16, 17, 4, 3, 5, 2}, 
    leaders are 17, 5 and 2.
    """
    keys_length = len(keys)
    all_leaders = []
    leader = 0
    for i in range(keys_length-1, -1, -1):
        if keys[i] > leader:
            leader = keys[i]
            all_leaders.append(leader)
    return all_leaders
