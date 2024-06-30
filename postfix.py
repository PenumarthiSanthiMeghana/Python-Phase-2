s = input()
stack = []
for char in s:
    if char.isdigit():
        stack.append(int(char))
    else:
        operand2 = stack.pop()
        operand1 = stack.pop()
        if char == '+':
            stack.append(operand1 + operand2)
        elif char == '-':
            stack.append(operand1 - operand2)
        elif char == '*':
            stack.append(operand1 * operand2)
        elif char == '/':
            stack.append(operand1 / operand2)

print(stack[-1])