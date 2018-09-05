
def merge_sort(arr, base, end):
    print(base, end)
    if end > base:
        mid = int((base+(end-1))/2)
        merge_sort(arr, base, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, base, mid, end)


def merge(arr, base, mid, end):
    i = base
    j = mid+1
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            i += 1
        else:
            # swap arr[j] with arr[i] and j++
            temp = arr[j]
            for k in range(j,i,-1):
                arr[k] = arr[k-1]
            arr[i] = temp
            j+=1
    # way 2 create a new list add element there in shorted way
    # then overide sorted sublist to our sublist


if __name__ == '__main__':
    data = [34,6,12,446,8,6435,34,4343,768,8,65,446,54,7,68,76]
    merge_sort(data, 0, len(data)-1)
    print(data)
