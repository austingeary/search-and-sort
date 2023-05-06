
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

def heap_sort(arr):
    if len(arr) <= 1:
        return arr
    
    for j in range((len(arr)-2)//2,-1,-1):
        siftdown(arr, j, len(arr))

    for end in range(len(arr)-1,0,-1):
        swap(arr, 0, end)
        siftdown(arr, 0, end)
    
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def siftdown(arr, i, upper):
    while True:
        l, r = i*2+1, i*2+2
        if max(l, r) < upper:
            if arr[i] >= max(arr[l], arr[r]):
                break
            elif arr[l] > arr[r]:
                swap(arr, i, l)
                i = l
            else:
                swap(arr, i, r)
                i = r
        elif l < upper:
            if arr[l] > arr[i]:
                swap(arr, i, l)
                i = l
            else:
                break
        elif r < upper:
            if arr[r] > arr[i]:
                swap(arr, i, r)
                i = r
            else:
                break
        else:
            break
    
if __name__ == '__main__':
    arr = [0, 9, 3, 8, 2, 7, 5]
    heap_sort(arr)
    print(arr)