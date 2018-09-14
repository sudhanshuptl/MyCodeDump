# Sort list with 0s,1s and 2s as data


def dutch_flag_problem(arr):
    low = 0
    mid = 0
    high = len(arr)-1

    while mid < high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]  # swap
            low += 1
            mid += 1
        elif arr[mid]==1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]  # swap
            high -=1
    return arr


if __name__ == '__main__':
    data = [0,1,2,1,0,0,0,1,1,2,1,2,1,2,1,2,1,2,0,0,0,1,2]
    print(dutch_flag_problem(data))
