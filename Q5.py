def is_consecutive (a_list):
    for i in range(len(a_list) - 1):
        if a_list[i] + 1 != a_list[i+1]:
            return False
    return True
