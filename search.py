#Binary

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

def binary_search_recursion(arr, l, r, target):

    if l <= r:
        m = (l + r) // 2

        if arr[m] == target:
            return m
        elif arr[m] < target:
            return binary_search_recursion(arr, m+1, r, target)
        else:
            return binary_search_recursion(arr, l, m-1, target)
    else:
        return -1

if __name__ == '__main__':
    arr = [2, 5, 7, 8, 9, 13, 14, 27, 34, 66, 71, 98]
    print(binary_search_recursion(arr, 0, len(arr)-1, 98))