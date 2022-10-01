def toPostFixExpression(source):
    OPERATORS = ('+', '-', '*', '/', '(', ')', '%')
    PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
    stack = []
    destination = []

    for character in source:
        if character not in OPERATORS:
            destination.append(character)
        elif character == '(':
            stack.append('(')
        elif character == ')':
            while stack and stack[-1] != '(':
                destination.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRIORITY[character] <= PRIORITY[stack[-1]]:
                destination.append(stack.pop())
            stack.append(character)
    while stack:
        destination.append(stack.pop())

    return destination
