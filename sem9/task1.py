expression = input().split()
stack1 = []
stack2 = []
output1 = []
output2 = []

for element in expression:
    if element.isdigit():
        output1.append(element)
    elif element in ["+", "-", "*", "/"]:
        while stack1 and stack1[-1] in ["*", "/"]:
            output1.append(stack1.pop())
        stack1.append(element)
    elif element == "(":
        stack1.append(element)
    elif element == ")":
        while stack1 and stack1[-1] != "(":
            output1.append(stack1.pop())
        stack1.pop()

while stack1:
    output1.append(stack1.pop())



print("Обратная польская запись")
print(' '.join(output1))
print(' '.join(output2))
