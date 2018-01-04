from data_structures import Queue
from factories import stack_factory


def interleave_stack(stack):
    '''
This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].
    '''

    stack_size = 0
    queue = Queue()
    while True:
        try:
            queue.enqueue(stack.pop())
            stack_size += 1
        except IndexError:
            break

    while True:
        try:
            stack.push(queue.dequeue())
        except IndexError:
            break

    while True:
        try:
            queue.enqueue(stack.pop())
        except IndexError:
            break

    while True:
        try:
            stack.push(queue.dequeue())
        except IndexError:
            break

    for regurgitation_size in range(stack_size - 1, 0, -1):
        for _ in range(regurgitation_size):
            queue.enqueue(stack.pop())
        for _ in range(regurgitation_size):
            stack.push(queue.dequeue())

    return stack


if __name__ == "__main__":
    assert interleave_stack(stack_factory([])) == stack_factory([])
    assert interleave_stack(stack_factory([1, 2, 3, 4, 5])) == stack_factory([1, 5, 2, 4, 3])
    assert interleave_stack(stack_factory([1])) == stack_factory([1])
    assert interleave_stack(stack_factory([1, 2, 3, 4])) == stack_factory([1, 4, 2, 3])
    assert interleave_stack(stack_factory([1, 2])) == stack_factory([1, 2])
