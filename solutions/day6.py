from tools.general import load_input

sum_any = 0
sum_all = 0

for group in load_input("day6.txt").split("\n\n"):

    members = [set(i) for i in group.split('\n')]
    sum_any += len(set.union(*members))
    sum_all += len(set.intersection(*members))

print(f"Part 1 => {sum_any}")
print(f"Part 2 => {sum_all}")
