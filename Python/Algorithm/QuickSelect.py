
class QuickSelect:
    def __init__(self, data_list):
        if not isinstance(data_list, list):
            raise ValueError('Data should be in list format')
        self.arr = data_list

    def quick_select(self, target_index, base, end):
        if base > end:
            return
        pivot = self.partition(base, end)
        if pivot == target_index:
            return self.arr[target_index]
        
        if pivot > target_index:
            return self.quick_select(target_index, base, pivot - 1)
        else:
            return self.quick_select(target_index, pivot+1, end)

    def partition(self, base, end):
        pivot = base
        pivot_value = self.arr[end]

        for i in range(base, end):
            if self.arr[i] <= pivot_value:
                #swap
                temp = self.arr[i]
                self.arr[i] = self.arr[pivot]
                self.arr[pivot] = temp
                # Increment Pivot
                pivot += 1

        temp = self.arr[end]
        self.arr[end] = self.arr[pivot]
        self.arr[pivot] = temp

        return pivot

    def driver_function(self, nth_largest):
        # convert nth largest to index
        nth_largest_index = len(self.arr) - nth_largest

        if nth_largest_index < 0:
            return "INVALID"
        return self.quick_select(nth_largest_index, 0, len(self.arr)-1)


if __name__ == '__main__':
    data = [56,23,56,123,678,12,3,4,2,6,3,6,3,6,7,5,67,243,21,54,23,67,44]
    print('len data :',len(data))
    obj = QuickSelect(data)
    print(sorted(data))
    print('3rd Largest is :', obj.driver_function(14))
    print('current state : ', obj.arr)


