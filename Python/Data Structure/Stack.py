class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print('Stack is empty')

    def __str__(self):
        return str(self.stack)


if __name__ == '__main__':
    stack = Stack()
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    print(stack)
    print('Pop :',stack.pop())
    print('current State :',stack)