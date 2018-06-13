# Implement two stack in one Arry

class TwoStack(object):
    def __init__(self, size = 10):
        self.arr= list(range(size))
        self.top1 = -1
        self.top2 = size
        self.size = size

    def push1(self,data):
        if self.top1 < self.top2-1 : #condition for overflow
            self.top1 +=1
            self.arr[self.top1] = data
        else:
            print('Stack OverFlow')

    def push2(self,data):
        if self.top2 > self.top1 +1:
            self.top2 -=1
            self.arr[self.top2] = data
        else:
            print('Stack OverFlow')

    def pop1(self):
        if self.top1 >=0:
            temp = self.arr[self.top1]
            self.top1 -=1
            return temp
        else:
            print("Stack 1 is empty")

    def pop2(self):
        if self.top2 < self.size:
            temp = self.arr[self.top2]
            self.top2 +=1
            return temp
        else:
            print("Stack2 is empty")

    def print_stack1(self):
        print(' Stack 1 : ',end='')
        if self.top1 >=0:
            print(' ,'.join([str(x) for x in self.arr[:self.top1+1]]))

    def print_stack2(self):
        print(' Stack 2 : ', end='')
        if self.top2 < self.size:
            stack2 = self.arr[self.top2:][::-1] #reverse to print
            print(' ,'.join([str(x) for x in stack2]))

if __name__ == '__main__':
    two_stack = TwoStack(5)
    two_stack.push1(1)
    two_stack.push1(2)
    two_stack.push1(3)

    two_stack.push2(5)
    two_stack.push2(4)
    two_stack.push2(3) #print stack over flow
    two_stack.push1(4) #print stack over flow

    two_stack.print_stack1()
    two_stack.print_stack2()

    two_stack.pop1()
    two_stack.pop1()
    two_stack.pop1()
    two_stack.pop1() # stack is empty

    two_stack.pop2()
    two_stack.pop2()
    two_stack.pop2() #stack is empty