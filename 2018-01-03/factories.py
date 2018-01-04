from data_structures import Stack


def stack_factory(content):
    stack = Stack()
    for el in content:
        stack.push(el)
    return stack
