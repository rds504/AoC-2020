def find_binsearch(sorted_list: list, target):

    lower, upper = 0, len(sorted_list) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            lower = mid + 1
        else:
            upper = mid - 1

    return -1

def contains(haystack: list, needle, presorted=False):

    if presorted:
        return find_binsearch(haystack, needle) != -1
    
    return needle in haystack
