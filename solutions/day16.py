import re
from functools import reduce
from operator import mul
from tools.general import load_input

class ValidValues:

    def __init__(self, bounds):
        self._lo1, self._hi1, self._lo2, self._hi2 = [int(bound) for bound in bounds]

    def __contains__(self, value):
        return self._lo1 <= value <= self._hi1 or self._lo2 <= value <= self._hi2

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
                field, *bounds = match.groups()
                field_rules[field] = ValidValues(bounds)
        elif line != "":
            ticket = [int(i) for i in line.split(',')]
            if parsing_mode == "yours":
                your_ticket = ticket
            elif parsing_mode == "nearby":
                near_tickets.append(ticket)

    return (field_rules, your_ticket, near_tickets)

def validate_tickets(rule_list, ticket_list):

    invalid_fields = []
    valid_tickets  = []

    for ticket in ticket_list:

        ticket_valid = True

        for field in ticket:

            for valid_values in rule_list:
                if field in valid_values:
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

    for field, valid_values in field_rules.items():

        valid_positions = set(range(len(valid_ticket_list[0])))

        for ticket in valid_ticket_list:
            for position, value in enumerate(ticket):
                if value not in valid_values:
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
