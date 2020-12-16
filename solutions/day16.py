import re
from functools import reduce
from operator import mul
from tools.general import load_input

def parse_ticket_data(ticket_data):

    rule_pattern = re.compile(r"([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)")
    field_rules  = {}
    your_ticket  = None
    near_tickets = []
    parsing_mode = "rules"

    for line in ticket_data.split('\n'):

        if line == "your ticket:":
            parsing_mode = "yours"
        elif line == "nearby tickets:":
            parsing_mode = "nearby"
        elif parsing_mode == "rules":
            match = rule_pattern.match(line)
            if match:
                field_rules[match.group(1)] = tuple(int(match.group(i)) for i in range(2, 6))
        elif line != "":
            ticket = [int(i) for i in line.split(',')]
            if parsing_mode == "yours":
                your_ticket = ticket
            elif parsing_mode == "nearby":
                near_tickets.append(ticket)

    return (field_rules, your_ticket, near_tickets)

def valid_value_for_field(rule, value):
    lo1, hi1, lo2, hi2 = rule
    return (lo1 <= value <= hi1) or (lo2 <= value <= hi2)

def validate_tickets(rule_list, ticket_list):

    invalid_fields = []
    valid_tickets  = []

    for ticket in ticket_list:

        ticket_valid = True

        for field in ticket:

            for rule in rule_list:
                if valid_value_for_field(rule, field):
                    break
            else:
                invalid_fields.append(field)
                ticket_valid = False

        if ticket_valid:
            valid_tickets.append(ticket)

    return (valid_tickets, sum(invalid_fields))

def resolve_field_positions(field_rules, valid_ticket_list):

    field_positions       = {}
    field_valid_positions = {}

    for field, rule in field_rules.items():

        valid_positions = set(range(len(valid_ticket_list[0])))

        for ticket in valid_ticket_list:
            for position, value in enumerate(ticket):
                if not valid_value_for_field(rule, value):
                    valid_positions.remove(position)

        field_valid_positions[field] = valid_positions

    for field, valid_positions in sorted(field_valid_positions.items(), key = lambda x: len(x[1])):

        for position in valid_positions:
            if position not in field_positions.values():
                field_positions[field] = position
                break

    return field_positions

def check_departure_fields(field_map, ticket):
    return reduce(
        mul,
        (ticket[pos] for fld, pos in field_map.items() if fld.startswith("departure"))
    )

rules, own_ticket, nearby_tickets = parse_ticket_data(load_input("day16.txt"))

nearby_valid_tickets, invalid_fieldsum = validate_tickets(rules.values(), nearby_tickets)
print(f"Part 1 => {invalid_fieldsum}")

fld_positions = resolve_field_positions(rules, nearby_valid_tickets)
print(f"Part 2 => {check_departure_fields(fld_positions, own_ticket)}")
