from stack import Stack

stack = Stack()
stack.push("test")
stack.push("Ala")
stack.push("has")
stack.push("a")
stack.push("cat")
print(stack.items)
print(stack.top())
print(stack.height())
print(stack.pop())
print(stack.height())
print(stack.items)

#empty stack
stack2 = Stack()
print(stack2.pop())
