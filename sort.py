
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr.pop()
    low, high = [], []

    for item in arr:
        if item > pivot:
            high.append(item)
        else:
            low.append(item)

    return quick_sort(low) + [pivot] + quick_sort(high)



def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    #split
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]

    #recursion
    merge_sort(left_arr)
    merge_sort(right_arr)

    #merge
    i, j, k = 0, 0, 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    return arr

if __name__ == '__main__':
    arr = [0, 9, 3, 8, 2, 7, 5]
    print(merge_sort(arr))