from tools.general import load_input

def summarise_answers(group_answers):

    sum_any, sum_all = 0, 0

    for group in group_answers:
        members = [set(i) for i in group.split('\n')]
        sum_any += len(set.union(*members))
        sum_all += len(set.intersection(*members))

    return sum_any, sum_all

answered_any, answered_all = summarise_answers(load_input("day6.txt").split("\n\n"))
print(f"Part 1 => {answered_any}")
print(f"Part 2 => {answered_all}")
