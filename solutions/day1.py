from tools import general, lists

input_data = sorted(int(i) for i in general.load_input("day1.txt").split())
    
for i in input_data:
    j = 2020 - i
    if lists.contains(input_data, j, True):
        print(f"Part 1 => {i * j}")
        break
    
found_triple = False
for i in input_data:
    if found_triple:
        break
    d = 2020 - i
    for j in input_data:
        if i != j:
            k = d - j
            if k <= 0:
                break
            if lists.contains(input_data, k, True):
                print(f"Part 2 => {i * j * k}")
                found_triple = True
                break
