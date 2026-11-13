from math import sqrt, floor

alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
words = 'багатство не в грошах а в доброму серці'.split()


def hash_index(word, method):
    key = 0
    for letter in word:
        key += alphabet.index(letter) + 1

    if method == 'ділення':
        return key % 13

    A = (sqrt(5) - 1) / 2
    value = key * A
    return floor(16 * (value - floor(value)))


def build_open(words, size, method):
    table = []
    for i in range(size):
        table.append([])

    for word in words:
        index = hash_index(word, method)
        if word not in table[index]:
            table[index].append(word)
    return table


def build_closed(words, size, method):
    table = [None] * size
    for word in words:
        index = hash_index(word, method)
        while table[index] is not None and table[index] != word:
            index = (index + 1) % size
        table[index] = word
    return table


# Повертає кількість порівнянь під час пошуку слова.
def search(table, word, method, table_type):
    index = hash_index(word, method)
    count = 0

    if table_type == 'відкрита':
        for item in table[index]:
            count += 1
            if item == word:
                break
    else:
        while count < len(table) and table[index] is not None:
            count += 1
            if table[index] == word:
                break
            index = (index + 1) % len(table)
    return count


# Виведення таблиці та потрібних за завданням результатів пошуку.
def show_results(table, method, table_type):
    for i in range(len(table)):
        if table[i] is None or table[i] == []:
            print(i, '| NULL')
        elif table_type == 'відкрита':
            print(i, '|', ' -> '.join(table[i]))
        else:
            print(i, '|', table[i])

    checked = []
    total = 0
    maximum = 0
    worst = []
    for word in words:
        if word in checked:
            continue
        checked.append(word)
        count = search(table, word, method, table_type)
        print(word, ':', count)
        total += count
        if count > maximum:
            maximum = count
            worst = [word]
        elif count == maximum:
            worst.append(word)

    print('Максимум:', maximum, worst)
    print('Середнє:', round(total / len(checked), 4))


for method in ['ділення', 'множення']:
    if method == 'ділення':
        size = 13
    else:
        size = 16

    print('Розмір таблиці:', size)
    print('Відкрите хешування:')
    table = build_open(words, size, method)
    show_results(table, method, 'відкрита')

    print('Закрите хешування:')
    table = build_closed(words, size, method)
    show_results(table, method, 'закрита')
