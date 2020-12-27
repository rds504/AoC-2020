from typing import Dict, List

def find_binsearch(sorted_list: list, target) -> int:

    lower, upper = 0, len(sorted_list) - 1
    while lower <= upper:
        mid = (lower + upper) // 2

        if sorted_list[mid] == target:
            return mid

        if sorted_list[mid] < target:
            lower = mid + 1
        else:
            upper = mid - 1

    return -1

def contains(haystack: list, needle, presorted: bool = False) -> bool:

    if presorted:
        return find_binsearch(haystack, needle) != -1

    return needle in haystack

def dict_from(data: List[str], separator: str = ':') -> Dict[str, str]:

    dictified = {}

    for i in data:
        try:
            key, value = i.split(separator)
            dictified[key] = value
        except ValueError:
            pass

    return dictified
