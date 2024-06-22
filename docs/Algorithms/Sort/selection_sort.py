
def selection_sort(arr: list):
    n = len(arr)
    for i in range(n-1):
        first = i
        for j in range(i+1, n):
            if arr[first] > arr[j]:
                first = j
        arr[i], arr[first] = arr[first], arr[i]
    
    return arr

arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))