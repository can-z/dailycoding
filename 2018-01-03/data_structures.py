class Stack:
    def __init__(self):
        self._content = []

    def pop(self):
        return self._content.pop()

    def push(self, el):
        self._content.append(el)

    def __eq__(self, other):
        return self._content == other._content


class Queue:
    def __init__(self):
        self._content = []

    def enqueue(self, el):
        self._content.append(el)

    def dequeue(self):
        return self._content.pop(0)

    def __eq__(self, other):
        return self._content == other._content
