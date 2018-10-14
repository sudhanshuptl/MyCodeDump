# search in rotated sorted array
# example [4,5,6,7,1,2,3]

# step 1 find pivot point before that it is sorted and after that is sorted
#   # pivot point will be the point after that element is smaller
#   # compare neighbours in binary search way to minimize complexivity ot logn
import random


def find_pivot(arr, low, high):
    if high < low:  # termination case when there is no pivot point already sorted
        return -1

    if high == low: # if search exhausted consider any point as mid point
        return low

    mid = (low + high) // 2

    if mid < high and arr[mid] > arr[mid+1]:  # checking if next element in range then if next is smaller than mid
        return mid
    if mid > low and arr[mid-1] > arr[mid]:  # checking for pivot condition in previous space
        return mid-1

    if arr[low] >= arr[mid]: # then possibly this is our search domain
        return find_pivot(arr, low, mid-1)
    return find_pivot(arr, mid+1, high)


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


def search_in_sorted_rotated_array(arr, key):
    pivot = find_pivot(arr, 0, len(arr)-1)
    if pivot == -1:
        return binary_search(arr, 0, len(arr)-1, key )
    else:
        if arr[0] <= key <= arr[pivot]:
            return binary_search(arr, 0, pivot, key)
        else:
            return binary_search(arr, pivot+1, len(arr)-1,key)


if __name__ == '__main__':
    data = [random.randint(1, 100) for x in range(10)]
    data.sort()
    for i in range(5):
        data = data[i:] + data[:i]
        print(data)
        print(f'pivot point suppose to be {i} and calculated point :', find_pivot(data, 0, len(data)-1))
        for j in range(11):
            if j <10:
                print(f'Search value at index {j} , search indexed: ',search_in_sorted_rotated_array(data, data[j]))
            else:
                print('search non existed value :', search_in_sorted_rotated_array(data, 1000))



