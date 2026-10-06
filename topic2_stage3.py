def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            right = stack.pop()
            left = stack.pop()

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            elif token == "/":
                result = left / right

            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()


print(evaluate_postfix("3 4 +"))
print(evaluate_postfix("5 1 2 + 4 * + 3 -"))
print(evaluate_postfix("6 2 3 * - 4 +"))