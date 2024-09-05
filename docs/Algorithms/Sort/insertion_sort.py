
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        curr_val = arr[i]
        idx = i - 1

        while idx >= 0 and curr_val < arr[idx]:
            arr[idx+1] = arr[idx]
            idx -= 1
        arr[idx+1] = curr_val 
    
    return arr


sorted_arr = insertion_sort([ 7, 12, 9, 11, 3])
print(sorted_arr)
