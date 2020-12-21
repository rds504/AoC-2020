from tools.general import load_input_list

def eval_expression(expression, add_has_precedence = False):

    result = None
    paren_level = 0
    paren_expr = None
    operation = None
    add_result = 0

    for char in expression:

        if char == ' ':
            continue

        operand = None

        if paren_level > 0:
            if char == ')':
                paren_level -= 1
                if paren_level == 0:
                    if add_has_precedence:
                        add_result += eval_expression(paren_expr, True)
                    else:
                        operand = eval_expression(paren_expr)
                else:
                    paren_expr += char
            else:
                if char == '(':
                    paren_level += 1
                paren_expr += char
        elif char == '(':
            paren_expr = ""
            paren_level = 1
        elif char in ('+', '*'):
            operation = char
            if (char == '*') and add_result:
                operand = add_result
                add_result = 0
        else:
            if add_has_precedence:
                add_result += int(char)
            else:
                operand = int(char)

        if operand:
            if result is None:
                result = operand
            else:
                result = result + operand if operation == '+' else result * operand

    if add_result:
        if result is None:
            result = add_result
        else:
            result *= add_result

    return result

input_expressions = load_input_list("day18.txt")

print(f"Part 1 => {sum(eval_expression(expr) for expr in input_expressions)}")
print(f"Part 2 => {sum(eval_expression(expr, True) for expr in input_expressions)}")
