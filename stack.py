word = "module"
stack = []

for char in word:
    stack.append(char)

reversed_word = ""
while stack:
     reversed_word += stack.pop()

print(reversed_word)