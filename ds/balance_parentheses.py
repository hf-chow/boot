from stack import Stack

def is_valid_nesting(input):
    stack = Stack()
    for i in input:
        if i == "(":
            stack.push(i)
        elif i == ")":
            if stack.pop() == None:
                return False
    return stack.peek() == None
