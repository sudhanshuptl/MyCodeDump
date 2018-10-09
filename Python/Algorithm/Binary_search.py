# Binary Search Only Applicable on sorted array

import random


def binary_search_recursive(arr, low, high, key):
    if high >= low:
        mid = int((low + high)/2)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search_recursive(arr, low, mid-1, key)
        else:
            return binary_search_recursive(arr, mid+1, high, key)
    else:
        return -1


def binary_search(arr, low, high, key):
    while high >= low:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid-1
        else:
            low = mid+1
    return -1


if __name__ == '__main__':
    data = [random.randint(1, 100) for x in range(10)]
    data.sort()
    print(data)
    for i in range(20):
        if i < 10:
            print(f'Searching data at {i}th location output position is :',binary_search_recursive(data,0,len(data)-1, data[i]))
        else:
            random_number = random.randint(100, 500)
            print(f'searching a number that is not available for sure, output position :',binary_search_recursive(data,0,len(data)-1, random_number))

    print('None Recursive binary search test')
    for i in range(20):
        if i < 10:
            print(f'Searching data at {i}th location output position is :',binary_search(data, 0, len(data)-1, data[i]))
        else:
            random_number = random.randint(100, 500)
            print(f'searching a number that is not available for sure, output position :',binary_search(data, 0, len(data)-1, random_number))
