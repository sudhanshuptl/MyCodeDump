# Insertion sort in python
__author__ ='Sudhashu Patel'

class InsertionSort:
    def __init__(self, ls=[5,3,6,2,4,7,4,3]):
        self.ls = ls
        self.length = len(self.ls)

    def sort(self, reverse=False):
        if reverse:
            selecter = lambda x, y: x > y
        else:
            selecter = lambda x, y: x < y

        for i in range(1, self.length):
            key_index = i
            for j in range(0,i):
                if selecter(self.ls[j], self.ls[key_index]):
                    temp = self.ls.pop(key_index)
                    self.ls.insert(j, temp)
                    # insert at desired position

        if not reverse:
            print('List is Sorted :')
        else:
            print('List is reverse sorted')

    def print(self):
        print(", ".join([str(x) for x in self.ls]))

if __name__ == '__main__':
    insertionSort = InsertionSort([4, 5, 2, 5, 7, 5, 88, 55, 4, 3, 55, 45, 3, 4, 6, 99])
    insertionSort.print()
    insertionSort.sort(reverse=True)
    insertionSort.print()

    insertionSort.sort()
    insertionSort.print()
