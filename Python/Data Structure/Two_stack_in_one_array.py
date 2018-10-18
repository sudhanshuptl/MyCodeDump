class DoubleStack():
    def __init__(self, size=10):
        self.arr = list(range(10))
        self.top1 = -1
        self.top2 = size + 1
        self.size = size

    def push1(self, data):
        if self.top2 - 1 > self.top1:
            self.top1 += 1
            self.arr[self.top1] = data
        else:
            print('Stack1 is full')

    def push2(self, data):
        if self.top2 - 1 > self.top1:
            self.top2 -= 1
            self.arr[self.top2] = data
        else:
            print('Stack2 Overflow')

    def __str__(self):
        stack1 = 'Stack1 :' + str(self.arr[:self.top1 + 1])
        stack2 = '\nStack2 :' + str([self.arr[ind] for ind in range(self.size - 1, self.top2 - 1, -1)])
        return stack1 + stack2

    def pop1(self):
        if self.top1 < 0:
            print('Stack1 is Empty')
        else:
            temp = self.arr[self.top1]
            self.top1 -= 1
            return temp

    def pop2(self):
        if self.top2 >= self.size:
            print('stack2 is empty')
        else:
            temp = self.arr[self.top2]
            self.top2 += 1
            return temp

if __name__ =='__main__':
    stack = DoubleStack()
    stack.push1(5)
    stack.push1(4)
    stack.push1(3)
    print(stack)
    stack.push2(14)
    stack.push2(15)
    stack.push2(16)
    print(stack)
    print('Stack2 pop :',stack.pop2())
    print('Stack1 pop :', stack.pop1())
    print(stack)