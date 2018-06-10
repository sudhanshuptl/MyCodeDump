# Bubble sort in python
__author__ ='Sudhashu Patel'

class BubbleSort:
    def __init__(self, ls=[5,3,6,2,4,7,4,3]):
        self.ls = ls
        self.length = len(self.ls)

    def sort(self, reverse=False):
        if reverse:
            selecter = lambda x, y: x < y
        else:
            selecter = lambda x, y: x > y

        for i in range(self.length-1):
            for j in range(self.length-1-i):
                if selecter(self.ls[j], self.ls[j+1]):
                    self.ls[j], self.ls[j+1] = self.ls[j+1], self.ls[j]

        if not reverse:
            print('List is Sorted :')
        else:
            print('List is reverse sorted')

    def print(self):
        print(", ".join([str(x) for x in self.ls]))

if __name__ == '__main__':
    bubbleSort = BubbleSort([4,5,2,5,7,5,88,55,4,3,55,45,3,4,6,99])
    bubbleSort.print()
    bubbleSort.sort(reverse=True)
    bubbleSort.print()

    bubbleSort.sort()
    bubbleSort.print()
