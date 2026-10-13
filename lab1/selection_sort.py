def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    for i in range(n - 1):
        min_index = i
        assignments += 1
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1
        comparisons += 1  # Перевірка if min_index != i
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3
    return arr, comparisons, assignments

my_list = [54, 65, 7, 33, 86, 29, 11, 91, 12]
sorted_list, comps, assigs = selection_sort(my_list.copy())