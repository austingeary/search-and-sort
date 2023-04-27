#Binary, quicksort, mergesort

def binary_search(arr, target):
    l, r = 0, len(arr)-1

    while l <= r:
        m = (l + r) // 2

        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

if __name__ = '__main__':
    arr = [2, 5, 7, 8, 9, 13, 14, 27, 34, 66, 71, 98]
    binary_search(arr, 5)