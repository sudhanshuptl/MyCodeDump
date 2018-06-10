# Selection sort in python
__author__ ='Sudhashu Patel'

class SelectionSort:
    def __init__(self, ls=[5,3,6,2,4,7,4,3]):
        self.ls = ls
        self.length = len(self.ls)

    def find_min_index(self, base_index):
        '''
        :param base_index:
        :return: find index of minima from base index onword
        '''
        min_ = base_index
        for i in range(base_index+1,self.length):
            if self.ls[min_] > self.ls[i]:
                min_ = i
        return min_

    def find_max_index(self, base_index):
        '''
        :param base_index:
        :return: find index of minima from base index onword
        '''
        max_ = base_index
        for i in range(base_index+1,self.length):
            if self.ls[max_] < self.ls[i]:
                max_ = i
        return max_

    def sort(self, reverse=False):
        if not reverse:
            selecter = self.find_min_index
        else:
            selecter = self.find_max_index

        for i in range(0, self.length):
            selected_node = selecter(i)
            #swap data
            self.ls[i], self.ls[selected_node] = self.ls[selected_node], self.ls[i]

        if not reverse:
            print('List is Sorted :')
        else:
            print('List is reverse sorted')

    def print(self):
        print(", ".join([str(x) for x in self.ls]))

if __name__ == '__main__':
    selectionSort = SelectionSort([4, 5, 2, 5, 7, 5, 88, 55, 4, 3, 55, 45, 3, 4, 6, 99])
    selectionSort.print()
    selectionSort.sort(reverse=True) #reverse sort
    selectionSort.print()

    selectionSort.sort()
    selectionSort.print()
