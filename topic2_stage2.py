expression = "3 4 5"

tokens = expression.split()
stack = []

for token in tokens:
    stack.append(int(token))

print(stack)

