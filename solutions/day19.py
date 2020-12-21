import re
from tools.general import load_input

def parse_input_data(input_data):

    msg_rules = {}
    msg_list  = []

    rule_pattern = re.compile(r"^([0-9]+): ([0-9ab\"\| ]+)$")
    msg_pattern  = re.compile(r"^[ab]+$")

    for line in input_data.split('\n'):
        rm = rule_pattern.match(line)
        if rm:
            msg_rules[int(rm.group(1))] = rm.group(2)
        elif msg_pattern.match(line):
            msg_list.append(line)

    return msg_rules, msg_list

def resolve_rule(all_rules, rule_id, custom_rules = None):

    if custom_rules and (rule_id in custom_rules):
        return custom_rules[rule_id]

    alterns = []

    for alt in all_rules[rule_id].split('|'):
        alt_body = ""
        for add in alt.strip().split(' '):
            add_body = add.strip('"')
            if add_body in ('a', 'b'):
                alt_body += add_body
            else:
                alt_body += resolve_rule(all_rules, int(add_body), custom_rules)
        alterns.append(alt_body)

    if len(alterns) == 1:
        return alterns[0]

    return '(' + '|'.join(alterns) + ')'

rules, messages = parse_input_data(load_input("day19.txt"))

pattern = re.compile("^" + resolve_rule(rules, 0) + "$")
print(f"Part 1 => {sum(1 for msg in messages if pattern.match(msg))}")

special_cases = {
    8  : resolve_rule(rules, 42) + '+',
    11 : '(' + '|'.join(
            resolve_rule(rules, 42)
            + '{' + str(i) + '}'
            + resolve_rule(rules, 31)
            + '{' + str(i) + '}'
            for i in range(1, 6)
        ) + ')'
}

pattern = re.compile("^" + resolve_rule(rules, 0, special_cases) + "$")
print(f"Part 2 => {sum(1 for msg in messages if pattern.match(msg))}")
