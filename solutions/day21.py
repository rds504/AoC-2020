from tools.general import load_input_list

def parse_ingredients(ingredients_data):

    allergen_map      = {}
    ingredient_counts = {}

    for line in ingredients_data:

        contains = line.index(" (contains ")
        ingreds  = line[:contains].split(' ')
        allergs  = line[contains + len(" (contains "):-1].split(", ")

        for ingred in ingreds:
            if ingred in ingredient_counts:
                ingredient_counts[ingred] += 1
            else:
                ingredient_counts[ingred] = 1

        for allerg in allergs:
            if allerg in allergen_map:
                allergen_map[allerg].intersection_update(set(ingreds))
            else:
                allergen_map[allerg] = set(ingreds)

    return allergen_map, ingredient_counts

def safe_ingredients(allergen_map, ingredient_counts):
    return set(ingredient_counts.keys()).difference(set.union(*allergen_map.values()))

def resolve_allergens(allergen_map):

    resolved = {}

    while len(allergen_map) > 0:
        for allerg, ingreds in sorted(allergen_map.items(), key = lambda x: len(x[1])):
            possibilities = list(ingreds.difference(set(resolved.values())))
            if len(possibilities) == 1:
                resolved[allerg] = possibilities[0]
                allergen_map.pop(allerg)

    return resolved

allergens, ingredients = parse_ingredients(load_input_list("day21.txt"))
print(f"Part 1 => {sum(ingredients[i] for i in safe_ingredients(allergens, ingredients))}")

allergen_ingredient_map = resolve_allergens(allergens)
canonical = ','.join([allergen_ingredient_map[i] for i in sorted(allergen_ingredient_map)])
print(f"Part 2 => {canonical}")
