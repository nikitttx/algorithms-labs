from random import Random


def sink(a, k, n):
    comparisons = 0
    swaps = 0
    while True:
        j = 2 * k + 1
        if j >= n:
            break
        if j + 1 < n:
            comparisons += 1
            if a[j + 1] > a[j]:
                j += 1
        comparisons += 1
        if a[k] >= a[j]:
            break
        a[k], a[j] = a[j], a[k]
        swaps += 1
        k = j
    return comparisons, swaps


def heapsort(values):
    a = values.copy()
    comparisons = 0
    swaps = 0
    n = len(a)
    print("Початковий масив:", a)
    print("--- Фаза 1: Побудова максимальної купи ---")
    for i in range(n // 2 - 1, -1, -1):
        print("Занурюємо елемент з індексу", i, ":", a[i])
        c, s = sink(a, i, n)
        comparisons += c
        swaps += s
        print("Масив після кроку:", a)

    print("Масив після побудови купи:", a)
    print("--- Фаза 2: Сортування ---")
    for i in range(n - 1, 0, -1):
        print("Міняємо місцями корінь", a[0], "та елемент", a[i])
        a[0], a[i] = a[i], a[0]
        swaps += 1
        c, s = sink(a, 0, i)
        comparisons += c
        swaps += s
        print("Розмір купи:", i, ". Відновлюємо властивості купи.")
        print("Масив на поточному кроці:", a)

    print("Відсортований масив:", a)
    print("Порівнянь:", comparisons, "; обмінів:", swaps)
    return a, comparisons, swaps


def partition(a, left, right):
    comparisons = 0
    swaps = 0
    pivot = a[left]
    i = left - 1
    j = right + 1
    while True:
        i += 1
        comparisons += 1
        while a[i] < pivot:
            i += 1
            comparisons += 1
        j -= 1
        comparisons += 1
        while a[j] > pivot:
            j -= 1
            comparisons += 1
        if i >= j:
            return j, comparisons, swaps
        a[i], a[j] = a[j], a[i]
        swaps += 1


def quicksort(a, left, right):
    if left >= right:
        return 0, 0
    q, comparisons, swaps = partition(a, left, right)
    c1, s1 = quicksort(a, left, q)
    c2, s2 = quicksort(a, q + 1, right)
    return comparisons + c1 + c2, swaps + s1 + s2


def run_example():
    original = [54, 65, 7, 33, 86, 29, 11, 91, 12]
    result, hc, hs = heapsort(original)
    quick = original.copy()
    qc, qs = quicksort(quick, 0, len(quick) - 1)
    assert result == quick == sorted(original)
    print("Input:", original)
    print("Heapsort:", result)
    print("C =", hc, "S =", hs)
    print("Quicksort:", quick)
    print("C =", qc, "S =", qs)



if __name__ == '__main__':
    run_example()
