from abc import ABC, abstractmethod
from re import compile
from tools.general import load_input
from tools.lists import dict_from

class FieldValidator(ABC):

    @abstractmethod
    def valid(self, data: str):
        pass

class BoundedIntValidator(FieldValidator):

    def __init__(self, lower: int, upper: int):
        self._lower = lower
        self._upper = upper

    @property
    def lower(self):
        return self._lower
    
    @property
    def upper(self):
        return self._upper

    def valid(self, data: str):
    
        try:
            if self.lower <= int(data) <= self.upper:
                return True
        except ValueError:
            pass

        return False

class SimpleRegexValidator(FieldValidator):

    def __init__(self, pattern: str):
        self._pattern = compile(pattern)

    @property
    def pattern(self):
        return self._pattern

    def valid(self, data: str):
        return self.pattern.match(data) != None

class ValueListValidator(FieldValidator):

    def __init__(self, valid_values: list):
        self._valid_values = valid_values

    @property
    def valid_values(self):
        return self._valid_values

    def valid(self, data: str):
        return data in self.valid_values

class HeightValidator(FieldValidator):

    def __init__(self):
        self._pattern      = compile("^([0-9]+)(cm|in)$")
        self._cm_validator = BoundedIntValidator(150, 193)
        self._in_validator = BoundedIntValidator( 59,  76)

    def valid(self, data: str):

        m = self._pattern.match(data)

        if m:
            quant = int(m.group(1))
            units = m.group(2)

            if units == "cm":
                return self._cm_validator.valid(quant)
            elif units == "in":
                return self._in_validator.valid(quant)

        return False

input_data = load_input("day4.txt").split('\n\n')

validators = {
    'byr' : BoundedIntValidator(1920, 2002),
    'iyr' : BoundedIntValidator(2010, 2020),
    'ecl' : ValueListValidator(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
    'eyr' : BoundedIntValidator(2020, 2030),
    'hcl' : SimpleRegexValidator("^#[0-9a-f]{6}$"),
    'hgt' : HeightValidator(),
    'pid' : SimpleRegexValidator("^[0-9]{9}$")
}

valid1, valid2 = 0, 0

for passport in input_data:

    fields = dict_from(passport.split())

    if all(field in fields for field in validators):
        valid1 += 1
        for field in validators:
            if not validators[field].valid(fields[field]):
                break
        else:
            valid2 += 1

print(f"Part 1 => {valid1}")
print(f"Part 2 => {valid2}")
