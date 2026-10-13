def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    for i in range(1, n):
        key = arr[i]
        assignments += 1
        j = i - 1
        assignments += 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1
        if j >= 0:
            comparisons += 1
        arr[j + 1] = key
        assignments += 1
    return arr, comparisons, assignments

my_list = [54, 65, 7, 33, 86, 29, 11, 91, 12]
sorted_list, comps, assigs = insertion_sort(my_list.copy())